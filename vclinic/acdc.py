"""Cine cardiac magnetic resonance of ACDC, the Automated Cardiac Diagnosis Challenge.

ACDC holds the short-axis cine exams of 150 patients of the University Hospital
of Dijon in five groups of 30: normal subjects (NOR), dilated cardiomyopathy
(DCM), hypertrophic cardiomyopathy (HCM), previous myocardial infarction (MINF)
and abnormal right ventricle (RV) [Bernard et al., IEEE Transactions on Medical
Imaging 37(11):2514-2525, 2018, doi:10.1109/TMI.2018.2837502]. For every
patient, the end-diastolic (ED) and end-systolic (ES) frames come with expert
contours of the left ventricular cavity, the myocardium and the right
ventricular cavity.

The files are not part of the course repository. download() fetches them from
the public database of the Human Heart Project (CREATIS, Lyon), so every
participant receives the same files in Google Colab and in Jupyter. The data
are free of charge under CC BY-NC-SA 4.0 for non-commercial scientific
research only, and every use cites the article above.
"""

import concurrent.futures
import pathlib
import time
import urllib.request

import numpy as np
import pandas as pd
from scipy import ndimage

from .nifti import read_nifti

API = "https://humanheart-project.creatis.insa-lyon.fr/database/api/v1/item/{}/download"
CITATION = ("O. Bernard, A. Lalande, C. Zotti, F. Cervenansky, et al. Deep learning techniques for automatic MRI "
            "cardiac multi-structures segmentation and diagnosis: Is the problem solved? IEEE Transactions on "
            "Medical Imaging 37(11):2514-2525, 2018. doi:10.1109/TMI.2018.2837502")
GROUPS = {
    "NOR": "normal subjects",
    "DCM": "dilated cardiomyopathy: LV end-diastolic volume above 100 mL/m2 and LV ejection fraction below 40 %",
    "HCM": "hypertrophic cardiomyopathy: LV mass above 110 g/m2, several segments thicker than 15 mm in diastole, normal ejection fraction",
    "MINF": "previous myocardial infarction: LV ejection fraction below 40 % and several segments with abnormal contraction",
    "RV": "abnormal right ventricle: RV cavity volume above 110 mL/m2 or RV ejection fraction below 40 %",
}
LABELS = {0: "background", 1: "RV cavity", 2: "myocardium", 3: "LV cavity"}

# patient, split (tr training, te testing), group, ED frame, ES frame, the server ids of
# Info.cfg, ED image, ED contours, ES image, ES contours, and the sizes of these files
_MANIFEST = """
001 tr DCM 1 12 63721d7073e9f0047faa052b 63721d7473e9f0047faa0533 63721d7473e9f0047faa0537 63721d7473e9f0047faa053b 63721d7473e9f0047faa053f 63 551178 6596 552456 6017
002 tr DCM 1 12 63721d7573e9f0047faa0548 63721d7573e9f0047faa0550 63721d7573e9f0047faa0554 63721d7573e9f0047faa0558 63721d7573e9f0047faa055c 63 612701 7259 614016 6485
003 tr DCM 1 15 63721d7573e9f0047faa0565 63721d7573e9f0047faa056d 63721d7573e9f0047faa0571 63721d7573e9f0047faa0575 63721d7573e9f0047faa0579 63 573937 7551 575171 7354
004 tr DCM 1 15 63721d7573e9f0047faa0582 63721d7573e9f0047faa058a 63721d7673e9f0047faa058e 63721d7673e9f0047faa0592 63721d7673e9f0047faa0596 63 744821 6956 747940 6805
005 tr DCM 1 13 63721d7673e9f0047faa059f 63721d7673e9f0047faa05a7 63721d7673e9f0047faa05ab 63721d7673e9f0047faa05af 63721d7673e9f0047faa05b3 63 553454 7857 551539 7180
006 tr DCM 1 16 63721d7673e9f0047faa05bc 63721d7673e9f0047faa05c4 63721d7673e9f0047faa05c8 63721d7673e9f0047faa05cc 63721d7673e9f0047faa05d0 63 785597 6803 788545 6344
007 tr DCM 1 7 63721d7773e9f0047faa05d9 63721d7773e9f0047faa05e1 63721d7773e9f0047faa05e5 63721d7773e9f0047faa05e9 63721d7773e9f0047faa05ed 63 516920 6052 516940 5950
008 tr DCM 1 13 63721d7773e9f0047faa05f6 63721d7773e9f0047faa05fe 63721d7773e9f0047faa0602 63721d7773e9f0047faa0606 63721d7773e9f0047faa060a 64 626172 6115 626731 5831
009 tr DCM 1 13 63721d7773e9f0047faa0613 63721d7773e9f0047faa061b 63721d7773e9f0047faa061f 63721d7773e9f0047faa0623 63721d7773e9f0047faa0627 63 677795 6889 672072 6668
010 tr DCM 1 13 63721d7873e9f0047faa0630 63721d7873e9f0047faa0638 63721d7873e9f0047faa063c 63721d7873e9f0047faa0640 63721d7873e9f0047faa0644 63 643759 6648 658881 6085
011 tr DCM 1 8 63721d7873e9f0047faa064d 63721d7873e9f0047faa0655 63721d7873e9f0047faa0659 63721d7873e9f0047faa065d 63721d7873e9f0047faa0661 62 559070 6144 561598 5958
012 tr DCM 1 13 63721d7873e9f0047faa066a 63721d7873e9f0047faa0672 63721d7873e9f0047faa0676 63721d7873e9f0047faa067a 63721d7873e9f0047faa067e 63 533968 6101 537232 5515
013 tr DCM 1 14 63721d7873e9f0047faa0687 63721d7973e9f0047faa068f 63721d7973e9f0047faa0693 63721d7973e9f0047faa0697 63721d7973e9f0047faa069b 63 520839 7452 523019 7164
014 tr DCM 1 13 63721d7973e9f0047faa06a4 63721d7973e9f0047faa06ac 63721d7973e9f0047faa06b0 63721d7973e9f0047faa06b4 63721d7973e9f0047faa06b8 63 629892 7686 633720 7440
015 tr DCM 1 10 63721d7973e9f0047faa06c1 63721d7973e9f0047faa06c9 63721d7973e9f0047faa06cd 63721d7973e9f0047faa06d1 63721d7973e9f0047faa06d5 63 546805 6053 543792 5705
016 tr DCM 1 12 63721d7973e9f0047faa06de 63721d7a73e9f0047faa06e6 63721d7a73e9f0047faa06ea 63721d7a73e9f0047faa06ee 63721d7a73e9f0047faa06f2 63 508641 7703 510060 7033
017 tr DCM 1 9 63721d7a73e9f0047faa06fb 63721d7a73e9f0047faa0703 63721d7a73e9f0047faa0707 63721d7a73e9f0047faa070b 63721d7a73e9f0047faa070f 58 524148 6973 527189 6893
018 tr DCM 1 10 63721d7a73e9f0047faa0718 63721d7b73e9f0047faa0720 63721d7b73e9f0047faa0724 63721d7b73e9f0047faa0728 63721d7b73e9f0047faa072c 59 515296 6077 517307 5628
019 tr DCM 1 11 63721d7b73e9f0047faa0735 63721d7b73e9f0047faa073d 63721d7b73e9f0047faa0741 63721d7b73e9f0047faa0745 63721d7b73e9f0047faa0749 59 715429 7625 716278 7166
020 tr DCM 1 11 63721d7b73e9f0047faa0752 63721d7b73e9f0047faa075a 63721d7b73e9f0047faa075e 63721d7b73e9f0047faa0762 63721d7b73e9f0047faa0766 60 563402 4924 565779 4675
021 tr HCM 1 13 63721d7b73e9f0047faa076f 63721d7c73e9f0047faa0777 63721d7c73e9f0047faa077b 63721d7c73e9f0047faa077f 63721d7c73e9f0047faa0783 64 586770 6206 586476 5402
022 tr HCM 1 11 63721d7c73e9f0047faa078c 63721d7c73e9f0047faa0794 63721d7c73e9f0047faa0798 63721d7c73e9f0047faa079c 63721d7c73e9f0047faa07a0 63 405258 3691 405343 3243
023 tr HCM 1 9 63721d7c73e9f0047faa07a9 63721d7c73e9f0047faa07b1 63721d7c73e9f0047faa07b5 63721d7c73e9f0047faa07b9 63721d7c73e9f0047faa07bd 62 527827 5064 528272 4552
024 tr HCM 1 9 63721d7c73e9f0047faa07c6 63721d7c73e9f0047faa07ce 63721d7c73e9f0047faa07d2 63721d7c73e9f0047faa07d6 63721d7c73e9f0047faa07da 62 538180 4415 538953 4022
025 tr HCM 1 9 63721d7c73e9f0047faa07e3 63721d7d73e9f0047faa07eb 63721d7d73e9f0047faa07ef 63721d7d73e9f0047faa07f3 63721d7d73e9f0047faa07f7 62 597855 6957 598754 5498
026 tr HCM 1 12 63721d7d73e9f0047faa0800 63721d7d73e9f0047faa0808 63721d7d73e9f0047faa080c 63721d7d73e9f0047faa0810 63721d7d73e9f0047faa0814 63 519690 7222 518152 6169
027 tr HCM 1 11 63721d7d73e9f0047faa081d 63721d7d73e9f0047faa0825 63721d7d73e9f0047faa0829 63721d7d73e9f0047faa082d 63721d7d73e9f0047faa0831 63 551794 6637 550314 5537
028 tr HCM 1 9 63721d7d73e9f0047faa083a 63721d7d73e9f0047faa0842 63721d7d73e9f0047faa0846 63721d7d73e9f0047faa084a 63721d7d73e9f0047faa084e 62 482731 6020 482527 5187
029 tr HCM 1 12 63721d7d73e9f0047faa0857 63721d7d73e9f0047faa085f 63721d7d73e9f0047faa0863 63721d7d73e9f0047faa0867 63721d7d73e9f0047faa086b 63 492621 6823 492316 5220
030 tr HCM 1 12 63721d7e73e9f0047faa0874 63721d7e73e9f0047faa087c 63721d7e73e9f0047faa0880 63721d7e73e9f0047faa0884 63721d7e73e9f0047faa0888 63 550995 5442 551602 4356
031 tr HCM 1 10 63721d7e73e9f0047faa0891 63721d7e73e9f0047faa0899 63721d7e73e9f0047faa089d 63721d7e73e9f0047faa08a1 63721d7e73e9f0047faa08a5 63 524734 6333 527767 5047
032 tr HCM 1 12 63721d7e73e9f0047faa08ae 63721d7e73e9f0047faa08b6 63721d7e73e9f0047faa08ba 63721d7e73e9f0047faa08be 63721d7f73e9f0047faa08c2 64 609009 6635 608207 5251
033 tr HCM 1 14 63721d7f73e9f0047faa08cb 63721d7f73e9f0047faa08d3 63721d7f73e9f0047faa08d7 63721d7f73e9f0047faa08db 63721d7f73e9f0047faa08df 63 571564 5509 571300 4541
034 tr HCM 1 16 63721d8073e9f0047faa08e8 63721d8073e9f0047faa08f0 63721d8073e9f0047faa08f4 63721d8073e9f0047faa08f8 63721d8073e9f0047faa08fc 63 657063 6274 657188 5540
035 tr HCM 1 11 63721d8173e9f0047faa0905 63721d8173e9f0047faa090d 63721d8173e9f0047faa0911 63721d8173e9f0047faa0915 63721d8273e9f0047faa0919 63 969855 7735 969554 6861
036 tr HCM 1 12 63721d8273e9f0047faa0922 63721d8273e9f0047faa092a 63721d8273e9f0047faa092e 63721d8273e9f0047faa0932 63721d8273e9f0047faa0936 63 509772 5498 511649 4530
037 tr HCM 1 12 63721d8273e9f0047faa093f 63721d8273e9f0047faa0947 63721d8273e9f0047faa094b 63721d8273e9f0047faa094f 63721d8273e9f0047faa0953 64 393983 3320 395789 3235
038 tr HCM 1 11 63721d8273e9f0047faa095c 63721d8373e9f0047faa0964 63721d8373e9f0047faa0968 63721d8373e9f0047faa096c 63721d8373e9f0047faa0970 63 1096245 10593 1093967 9130
039 tr HCM 1 10 63721d8373e9f0047faa0979 63721d8373e9f0047faa0981 63721d8373e9f0047faa0985 63721d8373e9f0047faa0989 63721d8373e9f0047faa098d 64 658534 5476 660996 4562
040 tr HCM 1 13 63721d8373e9f0047faa0996 63721d8373e9f0047faa099e 63721d8373e9f0047faa09a2 63721d8373e9f0047faa09a6 63721d8373e9f0047faa09aa 63 722777 6431 722684 5798
041 tr MINF 1 11 63721d8473e9f0047faa09b3 63721d8473e9f0047faa09bb 63721d8473e9f0047faa09bf 63721d8473e9f0047faa09c3 63721d8473e9f0047faa09c7 64 297471 2863 297132 2690
042 tr MINF 1 16 63721d8473e9f0047faa09d0 63721d8473e9f0047faa09d8 63721d8473e9f0047faa09dc 63721d8473e9f0047faa09e0 63721d8473e9f0047faa09e4 64 560547 5319 560528 5064
043 tr MINF 1 7 63721d8473e9f0047faa09ed 63721d8473e9f0047faa09f5 63721d8473e9f0047faa09f9 63721d8473e9f0047faa09fd 63721d8473e9f0047faa0a01 63 627708 5540 625278 4902
044 tr MINF 1 11 63721d8473e9f0047faa0a0a 63721d8473e9f0047faa0a12 63721d8473e9f0047faa0a16 63721d8473e9f0047faa0a1a 63721d8573e9f0047faa0a1e 64 443658 5230 442619 4799
045 tr MINF 1 13 63721d8573e9f0047faa0a27 63721d8573e9f0047faa0a2f 63721d8573e9f0047faa0a33 63721d8573e9f0047faa0a37 63721d8573e9f0047faa0a3b 64 566246 5240 559868 4943
046 tr MINF 1 10 63721d8573e9f0047faa0a44 63721d8573e9f0047faa0a4c 63721d8573e9f0047faa0a50 63721d8573e9f0047faa0a54 63721d8573e9f0047faa0a58 64 484002 5996 484086 5367
047 tr MINF 1 9 63721d8573e9f0047faa0a61 63721d8573e9f0047faa0a69 63721d8573e9f0047faa0a6d 63721d8673e9f0047faa0a71 63721d8673e9f0047faa0a75 63 606749 5535 603478 5033
048 tr MINF 1 8 63721d8673e9f0047faa0a7e 63721d8673e9f0047faa0a86 63721d8673e9f0047faa0a8a 63721d8673e9f0047faa0a8e 63721d8673e9f0047faa0a92 63 560719 4853 562341 4535
049 tr MINF 1 11 63721d8773e9f0047faa0a9b 63721d8773e9f0047faa0aa3 63721d8773e9f0047faa0aa7 63721d8773e9f0047faa0aab 63721d8773e9f0047faa0aaf 64 418033 4202 419215 3945
050 tr MINF 1 12 63721d8873e9f0047faa0ab8 63721d8873e9f0047faa0ac0 63721d8873e9f0047faa0ac4 63721d8873e9f0047faa0ac8 63721d8873e9f0047faa0acc 64 617184 7023 616704 6685
051 tr MINF 1 11 63721d8873e9f0047faa0ad5 63721d8873e9f0047faa0add 63721d8873e9f0047faa0ae1 63721d8873e9f0047faa0ae5 63721d8873e9f0047faa0ae9 64 640156 6140 642039 5278
052 tr MINF 1 9 63721d8873e9f0047faa0af2 63721d8873e9f0047faa0afa 63721d8873e9f0047faa0afe 63721d8873e9f0047faa0b02 63721d8973e9f0047faa0b06 63 551295 5478 552763 4967
053 tr MINF 1 12 63721d8973e9f0047faa0b0f 63721d8973e9f0047faa0b17 63721d8973e9f0047faa0b1b 63721d8973e9f0047faa0b1f 63721d8973e9f0047faa0b23 64 488584 4989 489851 4740
054 tr MINF 1 12 63721d8973e9f0047faa0b2c 63721d8973e9f0047faa0b34 63721d8973e9f0047faa0b38 63721d8973e9f0047faa0b3c 63721d8973e9f0047faa0b40 64 478995 5210 481741 4670
055 tr MINF 1 10 63721d8973e9f0047faa0b49 63721d8a73e9f0047faa0b51 63721d8a73e9f0047faa0b55 63721d8a73e9f0047faa0b59 63721d8a73e9f0047faa0b5d 64 560646 5839 560769 5543
056 tr MINF 1 12 63721d8a73e9f0047faa0b66 63721d8a73e9f0047faa0b6e 63721d8a73e9f0047faa0b72 63721d8a73e9f0047faa0b76 63721d8a73e9f0047faa0b7a 60 524494 6382 525248 5373
057 tr MINF 1 9 63721d8a73e9f0047faa0b83 63721d8b73e9f0047faa0b8b 63721d8b73e9f0047faa0b8f 63721d8b73e9f0047faa0b93 63721d8b73e9f0047faa0b97 59 1832178 16271 1837024 14866
058 tr MINF 1 14 63721d8b73e9f0047faa0ba0 63721d8b73e9f0047faa0ba8 63721d8b73e9f0047faa0bac 63721d8b73e9f0047faa0bb0 63721d8b73e9f0047faa0bb4 60 568514 5861 569076 5186
059 tr MINF 1 9 63721d8b73e9f0047faa0bbd 63721d8b73e9f0047faa0bc5 63721d8b73e9f0047faa0bc9 63721d8b73e9f0047faa0bcd 63721d8b73e9f0047faa0bd1 59 526292 6226 527589 5361
060 tr MINF 1 14 63721d8b73e9f0047faa0bda 63721d8c73e9f0047faa0be2 63721d8c73e9f0047faa0be6 63721d8c73e9f0047faa0bea 63721d8c73e9f0047faa0bee 60 563900 5413 565073 4759
061 tr NOR 1 10 63721d8c73e9f0047faa0bf7 63721d8c73e9f0047faa0bff 63721d8c73e9f0047faa0c03 63721d8c73e9f0047faa0c07 63721d8c73e9f0047faa0c0b 63 503824 5877 504757 4596
062 tr NOR 1 9 63721d8c73e9f0047faa0c14 63721d8c73e9f0047faa0c1c 63721d8c73e9f0047faa0c20 63721d8c73e9f0047faa0c24 63721d8c73e9f0047faa0c28 62 466706 6844 469888 5981
063 tr NOR 1 16 63721d8c73e9f0047faa0c31 63721d8c73e9f0047faa0c39 63721d8c73e9f0047faa0c3d 63721d8c73e9f0047faa0c41 63721d8c73e9f0047faa0c45 63 470176 4119 473119 3251
064 tr NOR 1 12 63721d8c73e9f0047faa0c4e 63721d8d73e9f0047faa0c56 63721d8d73e9f0047faa0c5a 63721d8d73e9f0047faa0c5e 63721d8d73e9f0047faa0c62 63 551345 5924 552564 5467
065 tr NOR 1 14 63721d8d73e9f0047faa0c6b 63721d8d73e9f0047faa0c73 63721d8d73e9f0047faa0c77 63721d8d73e9f0047faa0c7b 63721d8d73e9f0047faa0c7f 63 374592 4018 376110 3356
066 tr NOR 1 11 63721d8d73e9f0047faa0c88 63721d8d73e9f0047faa0c90 63721d8d73e9f0047faa0c94 63721d8d73e9f0047faa0c98 63721d8d73e9f0047faa0c9c 63 577320 6196 578302 5144
067 tr NOR 1 10 63721d8d73e9f0047faa0ca5 63721d8d73e9f0047faa0cad 63721d8d73e9f0047faa0cb1 63721d8d73e9f0047faa0cb5 63721d8d73e9f0047faa0cb9 63 458680 6657 468762 5407
068 tr NOR 1 12 63721d8d73e9f0047faa0cc2 63721d8e73e9f0047faa0cca 63721d8e73e9f0047faa0cce 63721d8e73e9f0047faa0cd2 63721d8e73e9f0047faa0cd6 63 404866 4050 404431 3546
069 tr NOR 1 12 63721d8e73e9f0047faa0cdf 63721d8e73e9f0047faa0ce7 63721d8e73e9f0047faa0ceb 63721d8e73e9f0047faa0cef 63721d8e73e9f0047faa0cf3 63 387987 3649 387652 3329
070 tr NOR 1 10 63721d8e73e9f0047faa0cfc 63721d8e73e9f0047faa0d04 63721d8e73e9f0047faa0d08 63721d8e73e9f0047faa0d0c 63721d8e73e9f0047faa0d10 63 447923 3672 448345 3030
071 tr NOR 1 9 63721d8e73e9f0047faa0d19 63721d8e73e9f0047faa0d21 63721d8e73e9f0047faa0d25 63721d8e73e9f0047faa0d29 63721d8e73e9f0047faa0d2d 62 421002 5643 424213 4511
072 tr NOR 1 11 63721d8e73e9f0047faa0d36 63721d8f73e9f0047faa0d3e 63721d8f73e9f0047faa0d42 63721d8f73e9f0047faa0d46 63721d8f73e9f0047faa0d4a 63 454823 4694 455265 3993
073 tr NOR 1 10 63721d8f73e9f0047faa0d53 63721d8f73e9f0047faa0d5b 63721d8f73e9f0047faa0d5f 63721d8f73e9f0047faa0d63 63721d8f73e9f0047faa0d67 63 490241 4109 491879 3682
074 tr NOR 1 12 63721d8f73e9f0047faa0d70 63721d8f73e9f0047faa0d78 63721d8f73e9f0047faa0d7c 63721d8f73e9f0047faa0d80 63721d8f73e9f0047faa0d84 63 582887 5399 586501 4548
075 tr NOR 1 6 63721d8f73e9f0047faa0d8d 63721d8f73e9f0047faa0d95 63721d8f73e9f0047faa0d99 63721d8f73e9f0047faa0d9d 63721d8f73e9f0047faa0da1 62 757901 6938 755320 6106
076 tr NOR 1 12 63721d9073e9f0047faa0daa 63721d9073e9f0047faa0db2 63721d9073e9f0047faa0db6 63721d9073e9f0047faa0dba 63721d9073e9f0047faa0dbe 59 582887 5471 586501 4648
077 tr NOR 1 9 63721d9073e9f0047faa0dc7 63721d9073e9f0047faa0dcf 63721d9073e9f0047faa0dd3 63721d9073e9f0047faa0dd7 63721d9073e9f0047faa0ddb 58 487552 5409 490238 4366
078 tr NOR 1 9 63721d9073e9f0047faa0de4 63721d9073e9f0047faa0dec 63721d9073e9f0047faa0df0 63721d9073e9f0047faa0df4 63721d9073e9f0047faa0df8 58 526595 6144 532577 5130
079 tr NOR 1 11 63721d9073e9f0047faa0e01 63721d9173e9f0047faa0e09 63721d9173e9f0047faa0e0d 63721d9173e9f0047faa0e11 63721d9173e9f0047faa0e15 59 580103 5764 581523 4984
080 tr NOR 1 10 63721d9173e9f0047faa0e1e 63721d9173e9f0047faa0e26 63721d9173e9f0047faa0e2a 63721d9173e9f0047faa0e2e 63721d9173e9f0047faa0e32 59 349558 3621 348987 3140
081 tr RV 1 7 63721d9173e9f0047faa0e3b 63721d9173e9f0047faa0e43 63721d9173e9f0047faa0e47 63721d9173e9f0047faa0e4b 63721d9173e9f0047faa0e4f 61 809736 8918 806384 7288
082 tr RV 1 7 63721d9173e9f0047faa0e58 63721d9173e9f0047faa0e60 63721d9173e9f0047faa0e64 63721d9173e9f0047faa0e68 63721d9273e9f0047faa0e6c 61 765541 8223 763343 7011
083 tr RV 1 8 63721d9273e9f0047faa0e75 63721d9273e9f0047faa0e7d 63721d9273e9f0047faa0e81 63721d9273e9f0047faa0e85 63721d9273e9f0047faa0e89 61 415277 3613 413284 3421
084 tr RV 1 10 63721d9273e9f0047faa0e92 63721d9273e9f0047faa0e9a 63721d9373e9f0047faa0e9e 63721d9373e9f0047faa0ea2 63721d9373e9f0047faa0ea6 62 718408 7659 721720 6396
085 tr RV 1 9 63721d9373e9f0047faa0eaf 63721d9473e9f0047faa0eb7 63721d9473e9f0047faa0ebb 63721d9473e9f0047faa0ebf 63721d9473e9f0047faa0ec3 61 945837 10309 958918 9336
086 tr RV 1 8 63721d9473e9f0047faa0ecc 63721d9573e9f0047faa0ed4 63721d9573e9f0047faa0ed8 63721d9573e9f0047faa0edc 63721d9573e9f0047faa0ee0 61 486808 4418 486011 4298
087 tr RV 1 10 63721d9573e9f0047faa0ee9 63721d9673e9f0047faa0ef1 63721d9673e9f0047faa0ef5 63721d9673e9f0047faa0ef9 63721d9673e9f0047faa0efd 62 498635 5513 499553 4861
088 tr RV 1 12 63721d9673e9f0047faa0f06 63721d9773e9f0047faa0f0e 63721d9773e9f0047faa0f12 63721d9773e9f0047faa0f16 63721d9773e9f0047faa0f1a 62 755184 8200 751227 6647
089 tr RV 1 10 63721d9773e9f0047faa0f23 63721d9773e9f0047faa0f2b 63721d9773e9f0047faa0f2f 63721d9773e9f0047faa0f33 63721d9773e9f0047faa0f37 63 530092 4157 529557 3936
090 tr RV 4 11 63721d9773e9f0047faa0f40 63721d9773e9f0047faa0f48 63721d9773e9f0047faa0f4c 63721d9773e9f0047faa0f50 63721d9773e9f0047faa0f54 62 203002 3318 203753 2824
091 tr RV 1 9 63721d9773e9f0047faa0f5d 63721d9773e9f0047faa0f65 63721d9773e9f0047faa0f69 63721d9773e9f0047faa0f6d 63721d9773e9f0047faa0f71 61 311629 4360 319642 3599
092 tr RV 1 6 63721d9873e9f0047faa0f7a 63721d9873e9f0047faa0f82 63721d9873e9f0047faa0f86 63721d9873e9f0047faa0f8a 63721d9873e9f0047faa0f8e 61 648707 7703 648736 6455
093 tr RV 1 14 63721d9873e9f0047faa0f97 63721d9873e9f0047faa0f9f 63721d9873e9f0047faa0fa3 63721d9873e9f0047faa0fa7 63721d9873e9f0047faa0fab 58 418884 5398 423604 4368
094 tr RV 1 7 63721d9873e9f0047faa0fb4 63721d9873e9f0047faa0fbc 63721d9873e9f0047faa0fc0 63721d9873e9f0047faa0fc4 63721d9873e9f0047faa0fc8 61 310054 4465 313485 3896
095 tr RV 1 12 63721d9873e9f0047faa0fd1 63721d9873e9f0047faa0fd9 63721d9973e9f0047faa0fdd 63721d9973e9f0047faa0fe1 63721d9973e9f0047faa0fe5 62 690994 7904 698972 6878
096 tr RV 1 8 63721d9973e9f0047faa0fee 63721d9973e9f0047faa0ff6 63721d9973e9f0047faa0ffa 63721d9973e9f0047faa0ffe 63721d9973e9f0047faa1002 57 702093 10226 703777 8700
097 tr RV 1 11 63721d9973e9f0047faa100b 63721d9973e9f0047faa1013 63721d9973e9f0047faa1017 63721d9973e9f0047faa101b 63721d9973e9f0047faa101f 58 495001 5644 497924 4713
098 tr RV 1 9 63721d9973e9f0047faa1028 63721d9973e9f0047faa1030 63721d9973e9f0047faa1034 63721d9973e9f0047faa1038 63721d9973e9f0047faa103c 57 413347 5419 413756 5235
099 tr RV 1 9 63721d9973e9f0047faa1045 63721d9a73e9f0047faa104d 63721d9a73e9f0047faa1051 63721d9a73e9f0047faa1055 63721d9a73e9f0047faa1059 57 772913 7961 773194 6798
100 tr RV 1 13 63721d9a73e9f0047faa1062 63721d9a73e9f0047faa106a 63721d9a73e9f0047faa106e 63721d9a73e9f0047faa1072 63721d9a73e9f0047faa1076 58 707509 5656 711320 4794
101 te DCM 1 14 6372204873e9f0047faa160c 6372204873e9f0047faa1618 6372204873e9f0047faa1610 6372204873e9f0047faa161c 6372204873e9f0047faa1620 63 663909 6251 667156 5616
102 te NOR 1 13 6372203b73e9f0047faa11be 6372203c73e9f0047faa11ce 6372203c73e9f0047faa11d2 6372203b73e9f0047faa11c2 6372203c73e9f0047faa11ca 63 527504 4349 527215 3769
103 te MINF 1 11 6372204c73e9f0047faa16ba 6372204d73e9f0047faa16ca 6372204c73e9f0047faa16be 6372204d73e9f0047faa16c2 6372204d73e9f0047faa16c6 65 576604 5694 578195 5392
104 te HCM 1 11 6372204073e9f0047faa131a 6372204073e9f0047faa132a 6372204073e9f0047faa1322 6372204073e9f0047faa131e 6372204073e9f0047faa132e 63 530800 6089 532809 4524
105 te HCM 1 10 6372204073e9f0047faa12e0 6372204073e9f0047faa12f0 6372204073e9f0047faa12e8 6372204073e9f0047faa12f4 6372204073e9f0047faa12e4 63 700708 5852 703691 4846
106 te DCM 1 13 6372204b73e9f0047faa169d 6372204c73e9f0047faa16ad 6372204b73e9f0047faa16a5 6372204c73e9f0047faa16a9 6372204b73e9f0047faa16a1 63 567795 6804 569839 6586
107 te NOR 1 10 6372204973e9f0047faa1680 6372204a73e9f0047faa1684 6372204a73e9f0047faa1690 6372204a73e9f0047faa168c 6372204a73e9f0047faa1688 63 470216 5741 474391 4711
108 te HCM 1 9 6372204173e9f0047faa1354 6372204173e9f0047faa1360 6372204173e9f0047faa1368 6372204173e9f0047faa1358 6372204173e9f0047faa1364 62 718191 6899 721817 4811
109 te RV 1 10 6372204e73e9f0047faa1711 6372204e73e9f0047faa1715 6372204e73e9f0047faa1725 6372204e73e9f0047faa1719 6372204e73e9f0047faa1721 62 333704 4904 334415 3962
110 te NOR 1 11 6372204e73e9f0047faa16f4 6372204e73e9f0047faa16f8 6372204e73e9f0047faa1704 6372204e73e9f0047faa1708 6372204e73e9f0047faa1700 64 587109 5573 588351 4701
111 te HCM 1 7 6372204573e9f0047faa1524 6372204573e9f0047faa1530 6372204573e9f0047faa1534 6372204573e9f0047faa1528 6372204573e9f0047faa152c 62 418348 4156 418499 3624
112 te MINF 1 12 6372204773e9f0047faa15b5 6372204773e9f0047faa15bd 6372204773e9f0047faa15c1 6372204773e9f0047faa15c9 6372204773e9f0047faa15c5 64 744412 7838 746844 6369
113 te DCM 1 8 6372204373e9f0047faa1402 6372204373e9f0047faa140e 6372204373e9f0047faa140a 6372204373e9f0047faa1412 6372204373e9f0047faa1416 62 399033 5817 399585 5172
114 te HCM 1 11 6372204673e9f0047faa157b 6372204673e9f0047faa158b 6372204673e9f0047faa158f 6372204673e9f0047faa1583 6372204673e9f0047faa1587 63 666570 8424 667751 7232
115 te MINF 1 13 6372204573e9f0047faa1541 6372204673e9f0047faa1555 6372204573e9f0047faa1545 6372204673e9f0047faa1551 6372204673e9f0047faa154d 64 695696 7033 699113 6510
116 te HCM 1 9 6372203e73e9f0047faa1263 6372203e73e9f0047faa125b 6372203d73e9f0047faa124f 6372203d73e9f0047faa1257 6372203e73e9f0047faa125f 62 652426 6158 655232 4809
117 te DCM 1 13 6372204273e9f0047faa13ab 6372204273e9f0047faa13af 6372204273e9f0047faa13bf 6372204273e9f0047faa13b3 6372204273e9f0047faa13bb 63 569749 8045 571199 7193
118 te MINF 1 10 6372204273e9f0047faa13e5 6372204273e9f0047faa13e9 6372204373e9f0047faa13f1 6372204373e9f0047faa13f5 6372204373e9f0047faa13f9 64 560657 5674 560780 5515
119 te RV 1 9 6372204373e9f0047faa143c 6372204373e9f0047faa1450 6372204373e9f0047faa1440 6372204373e9f0047faa1448 6372204373e9f0047faa144c 61 609906 8980 614447 6742
120 te MINF 1 8 6372204773e9f0047faa15d2 6372204773e9f0047faa15e2 6372204773e9f0047faa15d6 6372204773e9f0047faa15da 6372204773e9f0047faa15e6 63 537895 5037 542038 4877
121 te RV 1 10 6372204673e9f0047faa155e 6372204673e9f0047faa1566 6372204673e9f0047faa156a 6372204673e9f0047faa1572 6372204673e9f0047faa156e 62 332975 4956 334320 3949
122 te DCM 1 6 6372203b73e9f0047faa1198 6372203a73e9f0047faa118c 6372203a73e9f0047faa1184 6372203b73e9f0047faa1194 6372203a73e9f0047faa1188 62 497800 5174 497069 4550
123 te NOR 1 11 6372204d73e9f0047faa16d7 6372204d73e9f0047faa16eb 6372204d73e9f0047faa16df 6372204d73e9f0047faa16e7 6372204d73e9f0047faa16db 63 534144 4788 534355 4305
124 te RV 1 7 6372204573e9f0047faa1507 6372204573e9f0047faa151b 6372204573e9f0047faa150f 6372204573e9f0047faa1513 6372204573e9f0047faa1517 61 712674 9837 712841 8609
125 te NOR 1 7 6372204473e9f0047faa1476 6372204473e9f0047faa147e 6372204473e9f0047faa147a 6372204473e9f0047faa148a 6372204473e9f0047faa1486 62 565878 7301 569614 6136
126 te RV 1 7 6372204473e9f0047faa14cd 6372204473e9f0047faa14d9 6372204473e9f0047faa14d5 6372204473e9f0047faa14d1 6372204573e9f0047faa14e1 61 443012 7739 448450 6189
127 te RV 1 7 6372204773e9f0047faa15ef 6372204873e9f0047faa15ff 6372204873e9f0047faa15fb 6372204773e9f0047faa15f3 6372204773e9f0047faa15f7 61 676099 9103 683094 7317
128 te NOR 1 11 6372204173e9f0047faa1385 6372204173e9f0047faa1379 6372204173e9f0047faa1371 6372204173e9f0047faa1381 6372204173e9f0047faa137d 63 570526 5894 572554 4837
129 te RV 1 8 6372204173e9f0047faa134b 6372204173e9f0047faa1343 6372204073e9f0047faa1337 6372204073e9f0047faa133b 6372204173e9f0047faa1347 61 833318 9193 832006 7403
130 te NOR 1 11 6372204473e9f0047faa14a7 6372204473e9f0047faa1493 6372204473e9f0047faa1497 6372204473e9f0047faa149f 6372204473e9f0047faa149b 63 649019 7201 653179 6038
131 te DCM 1 9 6372203f73e9f0047faa129d 6372203f73e9f0047faa1291 6372203f73e9f0047faa1299 6372203f73e9f0047faa1289 6372203f73e9f0047faa128d 62 558605 6919 559904 6760
132 te DCM 1 15 6372204973e9f0047faa1646 6372204973e9f0047faa1652 6372204973e9f0047faa164e 6372204973e9f0047faa165a 6372204973e9f0047faa1656 63 620453 7324 620913 7029
133 te DCM 1 10 6372204073e9f0047faa1311 6372204073e9f0047faa12fd 6372204073e9f0047faa1309 6372204073e9f0047faa1305 6372204073e9f0047faa1301 64 653856 7080 655232 6719
134 te HCM 1 15 6372204373e9f0047faa146d 6372204373e9f0047faa1459 6372204373e9f0047faa1461 6372204373e9f0047faa1465 6372204373e9f0047faa1469 64 654954 6324 655167 5339
135 te MINF 1 10 6372203c73e9f0047faa120c 6372203c73e9f0047faa1204 6372203c73e9f0047faa11f8 6372203c73e9f0047faa11fc 6372203c73e9f0047faa1208 64 524080 5762 524054 5277
136 te DCM 1 12 6372204273e9f0047faa13dc 6372204273e9f0047faa13cc 6372204273e9f0047faa13d4 6372204273e9f0047faa13d0 6372204273e9f0047faa13d8 63 620882 6297 621170 5611
137 te MINF 1 11 6372204873e9f0047faa1629 6372204873e9f0047faa1635 6372204973e9f0047faa1639 6372204873e9f0047faa1631 6372204973e9f0047faa163d 64 573732 6724 578467 5749
138 te HCM 1 10 6372203f73e9f0047faa12ba 6372203f73e9f0047faa12b6 6372203f73e9f0047faa12aa 6372203f73e9f0047faa12ae 6372203f73e9f0047faa12a6 63 561673 6209 561802 5463
139 te NOR 1 8 6372204973e9f0047faa1663 6372204973e9f0047faa1677 6372204973e9f0047faa166f 6372204973e9f0047faa166b 6372204973e9f0047faa1667 62 687340 8596 689632 6574
140 te RV 1 9 6372204473e9f0047faa14c4 6372204473e9f0047faa14bc 6372204473e9f0047faa14b0 6372204473e9f0047faa14c0 6372204473e9f0047faa14b4 61 750837 10247 756309 8636
141 te RV 1 11 6372203f73e9f0047faa12d7 6372203f73e9f0047faa12cb 6372203f73e9f0047faa12d3 6372203f73e9f0047faa12c7 6372203f73e9f0047faa12cf 62 578878 6636 577259 5395
142 te HCM 1 12 6372203d73e9f0047faa1246 6372203d73e9f0047faa1242 6372203d73e9f0047faa123e 6372203c73e9f0047faa1232 6372203d73e9f0047faa1236 63 528216 5764 527946 4387
143 te MINF 1 12 6372204273e9f0047faa13a2 6372204173e9f0047faa138e 6372204273e9f0047faa139e 6372204173e9f0047faa1392 6372204273e9f0047faa139a 64 672118 7016 675195 6292
144 te NOR 1 9 6372204573e9f0047faa14fe 6372204573e9f0047faa14fa 6372204573e9f0047faa14ee 6372204573e9f0047faa14ea 6372204573e9f0047faa14f2 62 527387 4717 528440 3882
145 te MINF 1 13 6372203f73e9f0047faa1280 6372203f73e9f0047faa127c 6372203e73e9f0047faa126c 6372203e73e9f0047faa1270 6372203e73e9f0047faa1278 64 506917 5849 507850 5607
146 te HCM 1 10 6372203c73e9f0047faa11ef 6372203c73e9f0047faa11df 6372203c73e9f0047faa11e3 6372203c73e9f0047faa11db 6372203c73e9f0047faa11e7 64 549489 5671 554315 4682
147 te RV 1 9 6372203c73e9f0047faa1229 6372203c73e9f0047faa1225 6372203c73e9f0047faa1215 6372203c73e9f0047faa1219 6372203c73e9f0047faa1221 62 1029526 10155 1029139 8532
148 te MINF 1 10 6372204773e9f0047faa15ac 6372204673e9f0047faa1598 6372204673e9f0047faa159c 6372204673e9f0047faa15a0 6372204673e9f0047faa15a8 64 525705 4613 526644 4317
149 te DCM 1 12 6372203b73e9f0047faa11b5 6372203b73e9f0047faa11a9 6372203b73e9f0047faa11ad 6372203b73e9f0047faa11a5 6372203b73e9f0047faa11a1 63 634690 7266 635200 5913
150 te NOR 1 12 6372204373e9f0047faa1433 6372204373e9f0047faa1423 6372204373e9f0047faa142f 6372204373e9f0047faa141f 6372204373e9f0047faa142b 63 500315 5193 504380 4160
"""


def manifest():
    """The 150 patients of ACDC: split, group, frames, file ids and sizes."""
    rows = []
    for line in _MANIFEST.strip().splitlines():
        p = line.split()
        rows.append({"patient": "patient" + p[0], "split": "training" if p[1] == "tr" else "testing",
                     "group": p[2], "ed_frame": int(p[3]), "es_frame": int(p[4]),
                     "ids": p[5:10], "sizes": [int(s) for s in p[10:15]]})
    return rows


def default_folder():
    """The folder data/acdc of the course folder (next to the package vclinic)."""
    return pathlib.Path(__file__).resolve().parents[1] / "data" / "acdc"


def _files(row):
    pid, ed, es = row["patient"], row["ed_frame"], row["es_frame"]
    return ["Info.cfg", f"{pid}_frame{ed:02d}.nii.gz", f"{pid}_frame{ed:02d}_gt.nii.gz",
            f"{pid}_frame{es:02d}.nii.gz", f"{pid}_frame{es:02d}_gt.nii.gz"]


def _fetch(item_id, target, size, tries=5):
    if target.exists() and target.stat().st_size == size:
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(API.format(item_id), timeout=120) as r:
                data = r.read()
            if len(data) != size:
                raise IOError(f"{target.name}: {len(data)} of {size} bytes")
            tmp = target.with_suffix(target.suffix + ".part")
            tmp.write_bytes(data)
            tmp.replace(target)
            return size
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(2 + 3 * attempt)
    return 0


def download(groups=("NOR", "DCM", "HCM"), folder=None, workers=8, verbose=True):
    """Download the ED and ES frames, their contours and Info.cfg of the chosen groups.

    Files that are already complete are skipped, so the function can be run again
    after an interruption. Returns the folder of the data.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    rows = [r for r in manifest() if r["group"] in groups]
    jobs = []
    for r in rows:
        for name, item_id, size in zip(_files(r), r["ids"], r["sizes"]):
            jobs.append((item_id, folder / r["patient"] / name, size))
    total = sum(j[2] for j in jobs)
    todo = [j for j in jobs if not (j[1].exists() and j[1].stat().st_size == j[2])]
    if verbose:
        print(f"ACDC: {len(rows)} patients, {len(jobs)} files, {total / 1e6:.0f} MB; "
              f"{len(jobs) - len(todo)} files already present.")
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_fetch, *j) for j in todo]
        for k, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            done += fut.result()
            if verbose and (k % max(1, len(todo) // 10) == 0 or k == len(todo)):
                print(f"  {k} of {len(todo)} files, {done / 1e6:.0f} MB")
    if verbose:
        print("ACDC data in", folder)
        print("Citation:", CITATION)
    return folder


def read_info(path):
    """Info.cfg of a patient as a dictionary."""
    info = {}
    for line in pathlib.Path(path).read_text().strip().splitlines():
        key, value = line.split(":", 1)
        info[key.strip()] = value.strip()
    return info


def _volume_ml(mask, spacing):
    return float(mask.sum()) * spacing[0] * spacing[1] * spacing[2] / 1000.0


def wall_by_slice(gt, spacing):
    """Thickest point of the left ventricular wall on each slice of a label volume, in mm.

    For every pixel of the cavity that borders the myocardium, the distance to the
    nearest pixel outside the wall (epicardial side or right ventricle) is measured.
    These distances run from the centre of a border pixel to the centre of the first
    pixel beyond the wall, one pixel more than the wall itself, so one pixel is
    subtracted. Slices with fewer than 20 pixels of myocardium are skipped.
    """
    walls = {}
    for k in range(gt.shape[2]):
        cav, myo = gt[:, :, k] == 3, gt[:, :, k] == 2
        if myo.sum() < 20 or not cav.any():
            continue
        dist = ndimage.distance_transform_edt(cav | myo, sampling=spacing[:2])
        border = cav & ~ndimage.binary_erosion(cav) & ndimage.binary_dilation(myo)
        if border.any():
            walls[k] = float(dist[border].max()) - float(spacing[0])
    return walls


def walls(patient, folder=None):
    """Thickest wall of every slice of a patient at ED in mm, from the base (slice 0) to the apex."""
    folder = pathlib.Path(folder) if folder else default_folder()
    d = folder / patient
    info = read_info(d / "Info.cfg")
    gt, sp = read_nifti(d / f"{patient}_frame{int(info['ED']):02d}_gt.nii.gz")
    return {k: round(v, 1) for k, v in wall_by_slice(gt, sp).items()}


def measure(patient, folder=None):
    """Volumes, ejection fractions, mass and wall thickness of one patient from the expert contours."""
    folder = pathlib.Path(folder) if folder else default_folder()
    d = folder / patient
    info = read_info(d / "Info.cfg")
    ed, es = int(info["ED"]), int(info["ES"])
    gt_ed, sp = read_nifti(d / f"{patient}_frame{ed:02d}_gt.nii.gz")
    gt_es, _ = read_nifti(d / f"{patient}_frame{es:02d}_gt.nii.gz")
    height, weight = float(info["Height"]), float(info["Weight"])
    bsa = (height * weight / 3600.0) ** 0.5
    lv_edv, lv_esv = _volume_ml(gt_ed == 3, sp), _volume_ml(gt_es == 3, sp)
    rv_edv, rv_esv = _volume_ml(gt_ed == 1, sp), _volume_ml(gt_es == 1, sp)
    mass = 1.05 * _volume_ml(gt_ed == 2, sp)
    walls = wall_by_slice(gt_ed, sp)
    wall = max(walls.values()) if walls else 0.0
    return {"patient": patient, "group": info["Group"], "height_cm": height, "weight_kg": weight,
            "bsa_m2": round(bsa, 3), "ed_frame": ed, "es_frame": es, "n_slices": int(gt_ed.shape[2]),
            "pixel_mm": round(sp[0], 3), "slice_mm": round(sp[2], 2),
            "lv_edv_ml": round(lv_edv, 1), "lv_esv_ml": round(lv_esv, 1),
            "lv_ef": round(100 * (lv_edv - lv_esv) / lv_edv, 1), "lv_edvi": round(lv_edv / bsa, 1),
            "rv_edv_ml": round(rv_edv, 1), "rv_esv_ml": round(rv_esv, 1),
            "rv_ef": round(100 * (rv_edv - rv_esv) / rv_edv, 1), "rv_edvi": round(rv_edv / bsa, 1),
            "lv_mass_g": round(mass, 1), "lv_mass_index": round(mass / bsa, 1), "max_wall_mm": round(wall, 1)}


def table(groups=("NOR", "DCM", "HCM"), folder=None, verbose=False):
    """One row per patient: split, group and the measurements of measure()."""
    folder = download(groups, folder, verbose=verbose)
    rows = []
    for r in manifest():
        if r["group"] in groups:
            m = measure(r["patient"], folder)
            m["split"] = r["split"]
            rows.append(m)
    cols = ["patient", "split", "group"] + [c for c in rows[0] if c not in ("patient", "split", "group")]
    return pd.DataFrame(rows)[cols]


def _crop(image, mask, spacing, center, size, fov_mm):
    """Resample a square of fov_mm around center to size x size pixels."""
    step = fov_mm / size
    offs = (np.arange(size) - (size - 1) / 2) * step
    rows = center[0] + offs[:, None] / spacing[1]
    cols = center[1] + offs[None, :] / spacing[0]
    rr, cc = np.broadcast_arrays(rows, cols)
    img = ndimage.map_coordinates(image, [rr, cc], order=1, mode="constant", cval=0.0)
    msk = ndimage.map_coordinates(mask, [rr, cc], order=0, mode="constant", cval=0)
    return img.astype(np.float32), msk.astype(np.uint8)


def slices(groups=("NOR", "DCM", "HCM"), size=64, fov_mm=128, n_slices=3, folder=None, verbose=False):
    """Mid-ventricular short-axis slices at ED and ES, centred on the left ventricle.

    Returns a dictionary of arrays with one entry per slice: images (values 0 to 1),
    masks (0 background, 1 RV cavity, 2 myocardium, 3 LV cavity), group, label,
    patient, phase ("ED" or "ES") and split, and the list classes.
    """
    folder = download(groups, folder, verbose=verbose)
    classes = [g for g in ("NOR", "DCM", "HCM", "MINF", "RV") if g in groups]
    out = {k: [] for k in ("images", "masks", "group", "label", "patient", "phase", "split")}
    for r in manifest():
        if r["group"] not in groups:
            continue
        d, pid = folder / r["patient"], r["patient"]
        gt_ed, sp = read_nifti(d / f"{pid}_frame{r['ed_frame']:02d}_gt.nii.gz")
        lv_slices = [k for k in range(gt_ed.shape[2]) if (gt_ed[:, :, k] == 3).sum() > 0]
        mid = lv_slices[len(lv_slices) // 2]
        chosen = sorted(lv_slices, key=lambda k: (abs(k - mid), k))[:n_slices]
        for phase, frame in (("ED", r["ed_frame"]), ("ES", r["es_frame"])):
            vol, sp = read_nifti(d / f"{pid}_frame{frame:02d}.nii.gz")
            gt, _ = read_nifti(d / f"{pid}_frame{frame:02d}_gt.nii.gz")
            for k in sorted(chosen):
                img2d = vol[:, :, k].T.astype(np.float32)
                ref = gt_ed[:, :, k].T
                heart = (ref == 2) | (ref == 3)
                center = ndimage.center_of_mass(heart)
                img, msk = _crop(img2d, gt[:, :, k].T, sp, center, size, fov_mm)
                lo, hi = np.percentile(img[img > 0], [1, 99]) if (img > 0).any() else (0.0, 1.0)
                img = np.clip((img - lo) / max(hi - lo, 1e-6), 0, 1)
                out["images"].append(img)
                out["masks"].append(msk)
                out["group"].append(r["group"])
                out["label"].append(classes.index(r["group"]))
                out["patient"].append(pid)
                out["phase"].append(phase)
                out["split"].append(r["split"])
    data = {k: np.array(v) for k, v in out.items()}
    data["images"] = data["images"].astype(np.float32)
    data["classes"] = classes
    data["pixel_mm"] = fov_mm / size
    return data


def pairs(groups=("NOR", "DCM", "HCM"), n_val=5, seed=2026, n_slices=3, folder=None, verbose=False):
    """The input of the network of the course: the ED and ES frame of each slice as two channels.

    Returns a dictionary: X (n, 2, 64, 64), y (class index), patient, set ("train",
    "val" or "test") and classes, with n_slices middle slices per patient. The 30 testing patients of ACDC form the test set;
    n_val patients per class of the ACDC training set form the validation set.
    """
    S = slices(groups, n_slices=n_slices, folder=folder, verbose=verbose)
    ed = S["phase"] == "ED"
    X = np.stack([S["images"][ed], S["images"][~ed]], axis=1).astype(np.float32)
    y, patient, split = S["label"][ed], S["patient"][ed], S["split"][ed]
    rng = np.random.RandomState(seed)
    val = set()
    for k in range(len(S["classes"])):
        names = sorted(set(patient[(y == k) & (split == "training")]))
        val |= set(rng.choice(names, n_val, replace=False))
    sets = np.array(["test" if s == "testing" else ("val" if p in val else "train") for p, s in zip(patient, split)])
    return {"X": X, "y": y, "patient": patient, "set": sets, "classes": S["classes"]}

# Skeleton-based-Human-Action-Recognition
This is partial implementation of PR 2017 and CVPR 2018 papers

Matlab R2015b, Python 2.7.14, and Pytorch 0.3.0 are used.

1. $ git clone https://github.com/nkliuyifang/Skeleton-based-Human-Action-Recognition.git

2. download and unzip dataset: https://pan.baidu.com/s/1f7hWElp3_u5Wen8qVGfB8Q

3. open Matlab, and run "run.m"

4. $ python run.py

5. $ python show.py

6. The result:

Method | Northwestern-UCLA dataset
------ | -------------------------
Type 1 | 0.7478 (Baseline)
Type 2 | 0.8152 (Baseline + View Transform, the method in PR 2017)
Type 3 | 0.8717 (Baseline + Point Insert, the method in CVPR 2018)
Type 4 | 0.8630 (Baseline + View Transform + Point Insert)

## Citation
Please cite the following paper if you use this repository in your reseach.
```
@article{
    title={Enhanced skeleton visualization for view invariant human action recognition},
    author={Liu, Mengyuan and Liu, Hong and Chen, Chen},
    journal={Pattern Recognition (PR)},
    volume={68},
    pages={346--362},
    year={2017}
}

@inproceedings{CVPR2018,
    title={Recognizing Human Actions as the Evolution of Pose Estimation Maps},
    author={Liu, Mengyuan and Yuan, Junsong},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    pages={1159--1168},
    year={2018}
}

# Skeleton-based-Human-Action-Recognition
This is partial implementations of our PR 2017 and CVPR 2018 papers.

## Prerequisites
The following code is based on Matlab R2015b, Python 2.7.14, and Pytorch 0.3.0.

## Installation
```
1. $ git clone https://github.com/nkliuyifang/Skeleton-based-Human-Action-Recognition.git
```

2. Download and unzip datasets: 
- [UTD-MHAD](https://pan.baidu.com/s/1hc3AYngGxCXk49ihW-EbuA)
- [Northwestern-UCLA](https://pan.baidu.com/s/1f7hWElp3_u5Wen8qVGfB8Q)
- [NTU RGB+D]()

3. Open Matlab, and run "run.m"

```
4. $ python run.py
```
```
5. $ python show.py
```
6. Average accuracy over 10 times of running:

Method | UTD-MHAD (Cross Subject)
------ | -------------------------
Type 1 | 0.8763 (Baseline)
Type 2 | 0.8974 (Baseline + View Transform, the method in PR 2017)
Type 3 | 0.8884 (Baseline + Point Insert, the method in CVPR 2018)
Type 4 | 0.8814 (Baseline + View Transform + Point Insert)

Method | Northwestern-UCLA (Cross View)
------ | -------------------------
Type 1 | 0. (Baseline)
Type 2 | 0. (Baseline + View Transform, the method in PR 2017)
Type 3 | 0. (Baseline + Point Insert, the method in CVPR 2018)
Type 4 | 0. (Baseline + View Transform + Point Insert)

Method | NTU RGB+D (Cross View)
------ | -------------------------
Type 1 | 0.8342 (Baseline)
Type 2 | 0.8713 (Baseline + View Transform, the method in PR 2017)
Type 3 | 0.8472 (Baseline + Point Insert, the method in CVPR 2018)
Type 4 | 0.8638 (Baseline + View Transform + Point Insert)

## Citation
Please cite the following paper if you use this repository in your research.
```
@article{PR2017
    title={Enhanced Skeleton Visualization for View Invariant Human Action Recognition},
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

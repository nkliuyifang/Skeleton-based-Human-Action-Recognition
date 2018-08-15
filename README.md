# Skeleton-based-Human-Action-Recognition
This is partial implementations of our PR 2017 and CVPR 2018 papers.

## Prerequisites
The following code is based on Matlab R2015b, Python 2.7.14, and Pytorch 0.3.0.

## Installation
1. $ git clone https://github.com/nkliuyifang/Skeleton-based-Human-Action-Recognition.git

2. Download and unzip datasets: 
    * [UTD-MHAD](https://pan.baidu.com/s/1hc3AYngGxCXk49ihW-EbuA)
    * [Northwestern-UCLA](https://pan.baidu.com/s/1f7hWElp3_u5Wen8qVGfB8Q)
    * [NTU RGB+D](https://pan.baidu.com/s/1lJ1-kfrvfk-XZiqO-4cmlQ)

3. Open Matlab, and run "run.m"

4. $ python run.py

5. $ python show.py

## Results
We report average recognition accuracy over ten times of running:

| Method | UTD-MHAD<br>Cross Subject (%)|Northwestern-UCLA<br>Cross View (%) |NTU RGB+D<br>Cross View (%) |
| :------:| :------: | :------: | :------: |
CNN (PR 2017)                             | 87.63     | 73.98      | 83.42
CNN + View Transform (PR 2017)            | **89.74** | 84.30      | **87.13**
Pose Evolution Image (CVPR 2018)          | 88.84     | 75.65      | 84.72
Pose Evolution Image + View Transform     | 88.14     | **86.61**  | 86.38

## Citation
Please cite the following paper if you use this repository in your research.
```
@article{PR 2017
    title={Enhanced Skeleton Visualization for View Invariant Human Action Recognition},
    author={Liu, Mengyuan and Liu, Hong and Chen, Chen},
    journal={Pattern Recognition (PR)},
    volume={68},
    pages={346--362},
    year={2017}
}

@inproceedings{CVPR 2018,
    title={Recognizing Human Actions as the Evolution of Pose Estimation Maps},
    author={Liu, Mengyuan and Yuan, Junsong},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    pages={1159--1168},
    year={2018}
}

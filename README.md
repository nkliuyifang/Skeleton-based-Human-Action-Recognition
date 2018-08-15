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
We report average recognition accuracy over 10 times of running:

| Model| UTD-<br>MHAD (%)|Northwestern-<br>UCLA (%) |NTU RGB+D <br> Cross View (%) |
| :------| :------: | :------: | :------: |
Baseline                                  | 0.8763     | 0.7398      | 0.8342
Baseline + View Transform (PR 2017)       | **0.8974** | 0.8430      | **0.8713**
Baseline + Point Insert (CVPR 2018)       | 0.8884     | 0.7565      | 0.8472
Baseline + View Transform + Point Insert  | 0.8814     | **0.8661**  | 0.8638

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

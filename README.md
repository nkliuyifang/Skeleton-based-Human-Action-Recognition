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
Type 1 | 0.7370 (Baseline)
Type 2 | 0.8652 (Bseline + View Transform, the method in PR 2017)
Type 3 | 0.7891 (Baseline + Point Insert, the method in CVPR 2018)
Type 4 | 0.8630 (Bseline + View Transform + Point Insert)

## Citation
Please cite the following paper if you use this repository in your reseach.
```
@article{<br>
    title={Enhanced skeleton visualization for view invariant human action recognition},<br>
    author={Liu, Mengyuan and Liu, Hong and Chen, Chen},<br>
    journal={Pattern Recognition (PR)},<br>
    volume={68},<br>
    pages={346--362},<br>
    year={2017}<br>
}

@inproceedings{CVPR2018,<br>
    title={Recognizing Human Actions as the Evolution of Pose Estimation Maps},<br>
    author={Liu, Mengyuan and Yuan, Junsong},<br>
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},<br>
    pages={1159--1168},<br>
    year={2018}<br>
}
'''

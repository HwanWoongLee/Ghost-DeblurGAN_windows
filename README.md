# Ghost-DeblurGAN_windows
original project : https://github.com/York-SDCNLab/Ghost-DeblurGAN

위 프로젝틀 코드를 windows 환경에 맞게 구성한 프로젝트.

<br/>


## Environment
- Windows 11
- CUDA 11.3
<br/>

## Installation
git clone:
```
git clone https://github.com/HwanWoongLee/Ghost-DeblurGAN_windows.git
```
<br/>

create conda env:
```
conda create -n deblur python=3.8
```
```
conda activate deblur
```
<br/>

install requirements:
```
pip install -r requirements.txt
```
<br/>



## Test
이미지 한 장을 Deblurring:
```
python predict.py test_image.png None trained_weights/fpn_ghostnet_gm_hin.h5
```

## Train
config 폴더의 config.yaml을 수정

![image](https://github.com/HwanWoongLee/Ghost-DeblurGAN_windows/assets/20108771/f35d9243-6f23-478e-a6fc-211df75f83a9)

```
train:  
  files_a: &FILES_A {train blur path}  
  files_b: &FILES_B {train sharp path}  

val:
  files_a: {test blur path}
  files_b: {test sharp path}
```
<br/>

config 설정 후 training:
```
python train.py
```

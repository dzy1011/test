# test-readme
论文名字  
链接
## Introduction  
好多介绍
## Architecture
![DGM_model](https://www.baidu.com/img/bd_logo1.png)  
## Requirement 
* python >= 3.6  
* pytorch >= 1.4  
### How to Run it   
```
# MixATIS dataset
python train.py -g -bs=16 -ne=100 -dd=./data/MixATIS -lod=./log/MixATIS -sd=./save/MixATIS -nh=4 -wed=32 -sed=128 -ied=64 -sdhd=64 -dghd=64 -ln=MixATIS.txt

# MixSNIPS dataset
python train.py -g -bs=64 -ne=50 -dd=./data/MixSNIPS -lod=./log/MixSNIPS -sd=./save/MixSNIPS -nh=8 -wed=32 -ied=64 -sdhd=64 -ln=MixSNIPS.txt

# ATIS dataset
python train.py -g -bs=16 -ne=300 -dd=./data/ATIS -lod=./log/ATIS -sd=./save/ATIS -nh=4 -wed=64 -ied=128 -sdhd=128 -ln=ATIS.txt

# SNIPS dataset
python train.py -g -bs=16 -ne=200 -dd=./data/SNIPS -lod=./log/SNIPS -sd=./save/SNIPS -nh=8 -wed=64 -ied=64 -sdhd=64 -ln=SNIPS.txt 
```  
Due to some stochastic factors(e.g., GPU and environment), it maybe need to slightly tune the hyper-parameters using grid search to reproduce the results reported in our paper.  
## Citation 
When you use the our paper, we would appreciate it if you cite the following:  
```
@Override
protected void onDestroy() {
    EventBus.getDefault().unregister(this);
    super.onDestroy();
}
```  
## Acknowledgement
> A Stack-Propagation Framework with Token-Level Intent Detection for Spoken Language Understanding. Libo Qin,Wanxiang Che, Yangming Li, Haoyang Wen and Ting Liu. (EMNLP 2019). Long paper. [baidu](https://www.baidu.com/)  
> This code is based SOM-DST. We thank the authors for their wonderful open-source efforts.  
```
We are highly grateful for the public code of Stack-Propagation!
```  

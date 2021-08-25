# test-readme
[Focus on Interaction: A Novel Dynamic Graph Model for Joint Multiple Intent Detection and Slot Filling](https://ijcai.org/proceedings/2021/0523.pdf)
## Introduction  
Intent detection and slot filling are two main tasks for building a spoken language understanding (SLU) system. Since the two tasks are closely related, the joint models for the two tasks always outperform the pipeline models in SLU. However, most joint models directly incorporate multiple intent information for each token, which introduces intent noise into the sentence semantics, causing a decrease in the performance of the joint model. In this paper, we propose a Dynamic Graph Model (DGM) for joint multiple intent detection and slot filling, in which we adopt a sentence-level intent-slot interactive graph to model the correlation between the intents and slot. Besides, we design a novel method of constructing the graph, which can dynamically update the interactive graph and further alleviate the error propagation.
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
@inproceedings{ijcai2021-523,
  title     = {Focus on Interaction: A Novel Dynamic Graph Model for Joint Multiple Intent Detection and Slot Filling},
  author    = {Ding, Zeyuan and Yang, Zhihao and Lin, Hongfei and Wang, Jian},
  booktitle = {Proceedings of the Thirtieth International Joint Conference on
               Artificial Intelligence, {IJCAI-21}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  editor    = {Zhi-Hua Zhou},
  pages     = {3801--3807},
  year      = {2021},
  month     = {8},
  note      = {Main Track}
  doi       = {10.24963/ijcai.2021/523},
  url       = {https://doi.org/10.24963/ijcai.2021/523},
}
```  
## Acknowledgement
> AGIF: An Adaptive Graph-Interactive Framework for Joint Multiple Intent Detection and Slot Filling. Libo Qin, Xiao Xu, Wanxiang Che, Ting Liu. EMNLP 2020 Accept-Findings. [[paper]](https://www.aclweb.org/anthology/2020.findings-emnlp.163/)  
> This code is based [AGIF](https://github.com/LooperXX/AGIF). We thank the authors for their wonderful open-source efforts.  


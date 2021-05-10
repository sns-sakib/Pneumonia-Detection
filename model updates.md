Resnet101 model male(5000) female(4000) of RSNA (both pa and ap): 
      class: lung opacity : 4400, normal: 2200, not normal:2200
      ![resnet101 male female(total) rsna equal balance binary class test acc 71%, training 86%](https://user-images.githubusercontent.com/52566550/100654194-a8222e00-3373-11eb-9507-d866d02258fb.png)
      

Resnet101 model on male(7547) female(5653) rsna data
      class: lung opacity : 4400, normal: 4400, not normal:4400
      ![resnet101 male female(total) rsna equal balance 3 classes test acc 53%, training 83%](https://user-images.githubusercontent.com/52566550/100654220-afe1d280-3373-11eb-8fb2-595dd80bd21a.png)
      
Resnet101 on male female  rsna(only PA) 
       class: lung op-1000, normal-500, not normal-500,  validation accuracy and loss decreasing, model underfits.
      --instead of rmsprop, if we use adam, training acc is less, validation acc and loss increases and decreases (fluctuates)
      ![resnet101 male female pa rsna  25 ,384,  10 epochs ,  auc train test curve (class-not normal 500, normal 500, lung op-1000)](https://user-images.githubusercontent.com/52566550/100654416-f59e9b00-3373-11eb-9eea-0f70447ee94b.png)
      
      
   class: lung op-1000, normal-500, not normal-1000
      model underfitting, 73% test, 79% training acc, validation curve doesnt fluctuate.
      
   ![resnet101 male female pa rsna normal 500, not normal 1000, lung 1000, test acc 73%, training 79% curve 10 epochs, rmsprop dropout  25 , 384](https://user-images.githubusercontent.com/52566550/101233931-82838480-36e5-11eb-8892-febed48ec7ee.png)
   
   
 resnet101 on rsna ( male-female pa)
 class: lung op : 1076, normal: 1076
 train validation curve:
![resnet101 male female rsna pa 224  25 10 epochs normal 1076 pneumonia 1076 split 0 2 train auc 90% test auc 55% ](https://user-images.githubusercontent.com/52566550/102318028-d83c1480-3fa2-11eb-9a47-1e5f581fb242.png)

train auc score: 90%
local test data auc score: 55%

male pa: class: lung opacity: 620, normal: 620
train-validation curve:
![resnet101 male pa rsna normal  620 and pneumonea 620 10 epochs train auc 89% test auc 66%](https://user-images.githubusercontent.com/52566550/102318238-3668f780-3fa3-11eb-9f9c-d5032bf96a58.png)

train auc score: 89%
local test data auc score: 66%

female pa: lung opacity: 400, normal: 400
train-validation curve:
![resnet101  female rsna pa 224  25 10 epochs normal 400 pneumonia 400 train auc 93% test auc 55% ](https://user-images.githubusercontent.com/52566550/102318408-792acf80-3fa3-11eb-8190-f56e3f426397.png)


train auc score: 93%
local test data auc score: 55%


Densenet121 on rsna ( male-female pa)
 class: lung op : 1076, normal: 1076
 train validation curve:
![densenet121 male female rsna pa 224  25 10 epochs normal 1076 pneumonia 1076 split 0 2 train auc 89% test auc 59% ](https://user-images.githubusercontent.com/52566550/102318532-aaa39b00-3fa3-11eb-98ae-82927e402580.png)

train auc score: 89%
local test data auc score: 59%

male pa: class: lung opacity: 620, normal: 620
train-validation curve:
![densenet121 male pa rsna normal 620  and pneumonea 620 ( 20 split) 10 epochs train auc 90% test auc 64%](https://user-images.githubusercontent.com/52566550/102318570-bb541100-3fa3-11eb-8169-faeaeb3223e5.png)

train auc score: 90%
local test data auc score: 64%

female pa: lung opacity: 400, normal: 400
train-validation curve:
![densenet121 female pa rsna normal and pneumonea 10 epochs train auc 90% test auc 55%](https://user-images.githubusercontent.com/52566550/102318587-c4dd7900-3fa3-11eb-858d-9fd1ed82d54e.png)

train auc score: 90%
local test data auc score: 55%


  
 
 
Train Validation curves used in paper so far:

1 Resnet101 model male(5000) female(4000) of RSNA (both pa and ap) class lung opacity  4400, normal 2200, not normal 2200:
![1 Resnet101 model male(5000) female(4000) of RSNA (both pa and ap) class lung opacity  4400, normal 2200, not normal 2200](https://user-images.githubusercontent.com/52566550/117692534-ee12d600-b1de-11eb-970f-526f3e92cb1d.png)


2 Resnet101 on male female rsna(only PA) class lung op-1000, normal-500, not normal-500:

![2 Resnet101 on male female rsna(only PA) class lung op-1000, normal-500, not normal-500,](https://user-images.githubusercontent.com/52566550/117692148-8e1c2f80-b1de-11eb-96bb-9cd8ef454913.png)



3 resnet101 on rsna ( male-female pa) class lung op  1076, normal 1076 train validation curve:

![3 resnet101 on rsna ( male-female pa) class lung op  1076, normal 1076 train validation curve](https://user-images.githubusercontent.com/52566550/117692157-907e8980-b1de-11eb-8743-eee4d5827fd0.png)

4 male pa class  lung opacity 620, normal 620 train-validation curve:
![4 male pa class  lung opacity 620, normal 620 train-validation curve](https://user-images.githubusercontent.com/52566550/117692162-91afb680-b1de-11eb-8651-2631e175703b.png)


5 female pa lung opacity 400, normal 400 train-validation curve:
![5 female pa lung opacity 400, normal 400 train-validation curve](https://user-images.githubusercontent.com/52566550/117692167-92484d00-b1de-11eb-9a8c-5aa848785ac4.png)


6 Densenet121 on rsna ( male-female pa) class lung op  1076, normal 1076 train validation curve
![6 Densenet121 on rsna ( male-female pa) class lung op  1076, normal 1076 train validation curve](https://user-images.githubusercontent.com/52566550/117692170-92e0e380-b1de-11eb-868e-dd9e70086a67.png)



7 densenet121 female pa rsna normal and pneumonea 10 epochs train auc 90% test auc 55%:
![7 densenet121 female pa rsna normal and pneumonea 10 epochs train auc 90% test auc 55%](https://user-images.githubusercontent.com/52566550/117692222-9ecca580-b1de-11eb-841e-69857ccb9a14.png)


8 resnet101 male female rsna pa 224  25 10 epochs normal 1076 pneumonia 1076 split 0 2 train auc 90% test auc 55%
![8 resnet101 male female rsna pa 224  25 10 epochs normal 1076 pneumonia 1076 split 0 2 train auc 90% test auc 55%](https://user-images.githubusercontent.com/52566550/117692226-9ffdd280-b1de-11eb-8efb-faa060a14644.png)


9 densenet121 male female pa rsna normal and pneumonea 101 epochs train auc 92% test auc 70% 7_7 layer freeze:
![9 densenet121 male female pa rsna normal and pneumonea 101 epochs train auc 92% test auc 70% 7_7 layer freeze](https://user-images.githubusercontent.com/52566550/117692227-a0966900-b1de-11eb-8af1-c9bfe25dc5e2.png)



10 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 69% last to 7_7 layer unfreeze_new_augmentation:
![10 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 69% last to 7_7 layer unfreeze_new_augmentation](https://user-images.githubusercontent.com/52566550/117692228-a0966900-b1de-11eb-9522-c6298370a2c5.png)


11 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 68% last to 14_14 layer unfreeze:
![11 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 68% last to 14_14 layer unfreeze](https://user-images.githubusercontent.com/52566550/117692231-a12eff80-b1de-11eb-90c5-4e4918b8a1ce.png)



12 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 71% last to 28_28 layer unfreeze_new augmentation:
![12 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% test auc 71% last to 28_28 layer unfreeze_new augmentation](https://user-images.githubusercontent.com/52566550/117692235-a2602c80-b1de-11eb-9cb3-1c148a90c9f1.png)


[13 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% last to 14_14 layer unfreeze new aug +zoom +new dense layer:
![13 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 95% last to 14_14 layer unfreeze new aug +zoom +new dense layer](https://user-images.githubusercontent.com/52566550/117692238-a3915980-b1de-11eb-8464-0b87faa6d901.png)


14 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 96% test auc 71% last to 14_14 layer unfreeze_new augmentation:
![14 densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 96% test auc 71% last to 14_14 layer unfreeze_new augmentation](https://user-images.githubusercontent.com/52566550/117692239-a429f000-b1de-11eb-92e1-a89de659149b.png)



15 densenet121 male pa rsna normal 620  and pneumonea 620 ( 20 split) 10 epochs train auc 90% test auc 64%:
![15 densenet121 male pa rsna normal 620  and pneumonea 620 ( 20 split) 10 epochs train auc 90% test auc 64%](https://user-images.githubusercontent.com/52566550/117692217-9e340f00-b1de-11eb-803c-4622e252bc8b.png)



 

      

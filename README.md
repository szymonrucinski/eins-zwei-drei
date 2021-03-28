# Optical numbers recognition using MNIST dataset
The main purpose of this project is to provide beginners with a proper introduction to image recognition using CNN and PYtorch library for python. Project consists of 4 notebooks, each uses different CNN architecture: 2 custom architectures, alexanet and squeezent.

## *Custom architecture 1*
<div align="center">

| Layer        | Output (shape) |
|--------------|----------------|
| Linear-1     | [-1,1,256]     |
| ReLU-2       | [-1,1,256]     |
| Linear-3     | [-1,1,128]     |
| ReLu-4       | [-1,1,128]     |
| Linear-5     | [-1,1,64]      |
| Sigmoid-6    | [-1,1,64]      |
| Linear-7     | [-1,1,10]      |
| LogSoftmax-8 | [-1,1,10]      |
  
*Custom architecture 1*

</div>

## What does it do?
Well, it trains model to recognize images, generates report about architecture, accuracy, plots confusion matrix, graphs and save wrongly identified images to your hdd.
<div align="center">
   <img width="28" src="Images/wrong_idx0_pred7_actual2.png"> 
   <img width="28" src="Images/wrong_idx5_pred5_actual8.png"> 
   <img width="28" src="Images/wrong_idx9_pred3_actual5.png"> 
   <img width="28" src="Images/wrong_idx12_pred1_actual7.png"> 
   <img width="28" src="Images/wrong_idx15_pred9_actual4.png"> 
   <img width="28" src="Images/wrong_idx19_pred5_actual8.png"> 

   *Samples images to be classified*

   <img width="400" src="Images/matrix.png"> 
*confusion matrix*

   <img width="500" src="Images/graph.png"> 

*Epochs vs loss graph*

</div>

## Requirements
In order to run this notebooks you need to have conda installed. If it happens so that you already have it just run:

```bash
conda env create -f environment.yml
conda activate ein-zwei-drei
```

If you are on Windows just launch  *run.bat* script otherwise run

```bash
jupyter notebook .
```

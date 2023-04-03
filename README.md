American Sign Language MNIST
===================================
The American Sign Language MNIST dataset is a collection of images of hand gestures representing letters and numbers in American Sign Language (ASL). It consists of 27,455 training images and 7,172 test images, each of size 28x28 pixels. The dataset was created as a replacement for the original MNIST dataset.

The dataset was downloaded from Kaggle: [Sign Language MNIST](https://www.kaggle.com/datamunge/sign-language-mnist)

![ASL Image](https://miro.medium.com/v2/resize:fit:1180/format:webp/1*XrbqBLMR1W3N8mIQCPzPbw.png)


## 1. Clone the repository:
```bash
git clone https://github.com/Autodidact24/sign_language_mnist.git
```

## 2. Setup the environment:
```bash
python3 -m venv dvc-venv
echo "export PYTHONPATH=$PWD" >> dvc-venv/bin/activate
source dvc-venv/bin/activate
```

## 3. Install the required Python packages:


```bash
pip install -r requirements.txt
```

This DVC project comes with a preconfigured DVC
[remote storage](https://dvc.org/doc/commands-reference/remote) that holds raw
data (input) in AWS S3.

```console
$ dvc remote list
storage  s3:sign-language-mnist/archive
```

You will need to setup an AWS account, access keys, and an S3 bucket.


You can run [`dvc pull`](https://man.dvc.org/pull) to download the data:

```console
$ dvc pull
```

## Running in your environment

Run [`dvc exp run`](https://man.dvc.org/exp/run) to reproduce the
[pipeline](https://dvc.org/doc/user-guide/pipelines/defining-pipelinese):

```console
$ dvc exp run
Data and pipelines are up to date.
```

## ML pipeline

### [01-data-preprocessing](https://github.com/Autodidact24/sign_language_mnist/blob/main/notebooks/01-data-preprocessing.ipynb)

Contains a Jupyter notebook showing all the steps of data preprocessing.


### [02-classification-model](https://github.com/Autodidact24/sign_language_mnist/blob/main/notebooks/02-classification%20model.ipynb)

Contains a Jupyter notebook showing all the steps of model training and evaluation.

[DVCLive](https://dvc.org/doc/dvclive) is used for experiment tracking. 
See this [blog post](https://iterative.ai/blog/exp-tracking-dvc-python) for more
details.

## Project structure

The data files, DVC files, and results change as stages are created one by one.
After cloning and using [`dvc pull`](https://man.dvc.org/pull) to download
data, models, and plots tracked by DVC, the workspace should look like this:

```console
$ tree -L 2
├── LICENSE
├── README.md
├── data
│   ├── processed
│   ├── raw
│   ├── sign_mnist_test
│   └── sign_mnist_train
├── dvc.lock
├── dvc.yaml
├── models
├── notebooks
│   ├── 01-data-preprocessing.ipynb
│   └── 02-classification model.ipynb
├── params.yaml
├── references
├── reports
│   ├── figures
│   └── train
├── requirements.txt
└── src
    ├── stages
    └── utils

```
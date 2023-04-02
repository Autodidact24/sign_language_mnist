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
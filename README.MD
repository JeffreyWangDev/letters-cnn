# Greek Letter CNN
# INFO: I CANT HOST THIS BC IT NEEEDS A GPU FOR IT TO RUN AND #NEST IS WAY TO SLOW

This repository contains a Convolutional Neural Network (CNN) for recognizing Greek letters. The model is built using TensorFlow and Keras.


## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/JeffreyWangDev/letters-cnn.git
cd letters-cnn
pip install -r requirements.txt
```

## Data Preparation

All data that was used to train can be found in /training in the 4 folders

## Training the Model

To train the model, run all code in the train.ipynb:


## Usage

After training, you can use the model to make predictions on new images. Here's an example of how to use the trained model:

```python
import cv2
import tensorflow as tf

model = tf.keras.models.load_model('model.weights.best_1000.keras')

def predict(image):
    image = cv2.resize(image, (32, 32))
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image)
    return prediction[0]

img = cv2.imread('path_to_image.png')
print(predict(img))
```

## Web App

You can run the local Flask server for demonstration:

```bash
python web.py
```

Then visit http://localhost:5001 to test the CNN by uploading images.

### Docker Installation

1. **Build the Docker Image**:
    ```bash
    docker build -t greek-letter-cnn .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -it --rm -p 5001:5001 greek-letter-cnn
    ```

3. **Access the Web Application**:
    - Visit `http://localhost:5001` in your web browser to test the CNN by uploading images.

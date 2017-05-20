from models.convnet import ConvolutionalNeuralNetwork
from PIL import Image
import numpy as np

class Recognizer(object):

    def __init__(self, resize_length=400):
        self.resize_length = resize_length

    def recognize(self, image_path, flatten=True):
        img = Image.open(image_path)
        img = img.resize((self.resize_length, self.resize_length))
        X = np.array(img, dtype=np.float32)
        if flatten:
            X = X.flatten()
        cnn = ConvolutionalNeuralNetwork()
        y = cnn.predict(X)
        return y

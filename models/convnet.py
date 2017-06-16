# import tensorflow as tf
# import numpy as np


class ConvolutionalNeuralNetwork(object):

    def __init__(self):
        """ A 5 layer convnet to classify images. """
        # Hyperparameters
        pass

    def fit(self, X, y):
        """ Train a 5 layer convolutional neural network.
            Args:
                X: Training data. Flattened image pixels.
                y: Class or image label.
        """
        pass

    def predict(self, X):
        """ Predict label or class of an image.
            Args:
                X: Flattened image pixels.
            Return:
                y: one-hot encoded value of the correct class label.
        """
        pass

    def score(self, X, y):
        """ Evaluate the accuracy of the model.
            Args:
                X: Flattened image pixels for the testing or validation set.
                y: Class or image label for the testing or validation set.
            Return:
                accuracy: Accuracy of the model.
        """
        pass

import keras
import numpy as np
import matplotlib.pyplot as plt

class PredictionTester(keras.callbacks.Callback):
    features = []
    responses = []
    figure = None
    graph = None
    scaler = None

    def __init__(self, features, responses, scaler):
        super().__init__()
        self.features = features
        self.responses = responses
        self.scaler = scaler
        self.figure = plt.figure()
        self.graph = self.figure.add_subplot(111)
        return

    def on_train_begin(self, logs={}):
        return

    def on_train_end(self, logs={}):
        return

    def on_epoch_begin(self, epoch, logs={}):
        return

    def on_epoch_end(self, epoch, logs={}):
        min, scale = self.scaler.min_[-1], self.scaler.scale_[-1]
        predictions = np.flip(self.model.predict(self.features), 0)
        actual = np.flip(self.responses[:-1], 0)

        predictions = (predictions / scale) - min
        actual = (actual / scale) - min

        self.graph.clear()
        self.graph.plot(predictions, label='predicted')
        self.graph.plot(actual, label='actual')
        self.graph.set_xlabel('Time')
        self.graph.set_ylabel('Weighted price (USD)')
        self.graph.set_title('Epoch %d' % epoch)
        self.graph.legend()
        self.figure.show()
        plt.pause(0.001)
        return

    def on_batch_begin(self, batch, logs={}):
        return

    def on_batch_end(self, batch, logs={}):
        return
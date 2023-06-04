import numpy
import cv2
import tensorflow as tf
import keras
import tensorboard
import PIL
import tqdm

# Tensorflow (tensorflow-gpu==1.14.0, CPU version can be used too)
# Tensorboard (tensorboard==1.14.0)
# Keras (Keras==2.2.4)
# Opencv-python (opencv-python==4.1.0.25)
# Numpy (numpy==1.16.4)
# Pillow (Pillow==5.4.1)
# Tqdm (tqdm==4.31.1)

print("Tensorflow: " + tf.__version__)
print("Tensorboard: " + tensorboard.__version__)
print("Keras: " + keras.__version__)
print("Opencv-python/cv2: " + cv2.__version__)
print("Numpy: " + numpy.__version__)
print("Pillow: " + PIL.__version__)
print("Tqdm: " + tqdm.__version__)

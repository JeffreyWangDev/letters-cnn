import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image 
import cv2
from random import shuffle
import glob
import tables
import cv2  
from math import ceil
print("Num GPUs Available: ", len(tf.config.list_physical_devices("GPU")))

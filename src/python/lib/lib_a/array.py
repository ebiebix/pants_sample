import numpy as np
import tensorflow as tf
import tensorflow_io as tfio
import torch


def get_zero_array(shape):
    return np.zeros(shape)


def get_zero_tf_array(shape):
    return tf.zeros(shape)

def get_zero_torch_array(shape):
    return torch.zeros(shape)

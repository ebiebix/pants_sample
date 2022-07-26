import numpy as np
import tensorflow as tf
import tensorflow_io as tfio
import torch
from test_proto.test_pb2 import TEST


def get_zero_array(shape):
    return np.zeros(shape)


def get_zero_tf_array(shape):
    return tf.zeros(shape)

def get_zero_torch_array(shape):
    return torch.zeros(shape)

def get_test(test: str):
    return TEST(test=test)

import torch
import torch.nn as nn

class ODEFunc(nn.Module):
    def __init__(self, dim):
        super(ODEFunc, self).__init__()
        self.norm1 = norm(dim)
        self.relu = nn.RELU(inplace=True)

class ODEBlock(nn.Module):
    def __init__(self, odefunc):
        self.odefunc = odefunc

def conv(in_planes, out_planes, stride=1):
    '''3x3 convolution with padding'''
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)

def norm(dim):
    return nn.GroupNorm(min(32, dim), dim)


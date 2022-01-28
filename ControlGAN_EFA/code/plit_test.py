import os
from torch.autograd import Variable
import torch

data_dir = '../data/celeba'

with open(os.path.join(data_dir, 'CelebAMask-HQ-attribute-anno.txt'), 'r') as f:
    key = 29999
    index = 0
    label = []
    for line in f.readlines():
        index += 1
        if (index - 3) == int(key):
            line = line.strip('\n')
            line = line.split(" ")
            print(line[2:])
            line = line[2:]
            for l in line:
                label.append((int(l) + 1) / 2)
            break

    for l in label:
        print(l)
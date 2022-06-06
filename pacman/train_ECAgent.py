import pandas as pd
import numpy as np

data_north = pd.read_csv("../north.csv", header = None)
data_north = np.array(data_north)
data_east = pd.read_csv("../east.csv", header = None)
data_east = np.array(data_east)
data_south = pd.read_csv("../south.csv", header = None)
data_south = np.array(data_south)
data_west = pd.read_csv("../west.csv", header = None)
data_west = np.array(data_west)
constant = np.array([[1,1,1,1,1,1,1]])

train_n, label_n = np.c_[data_north[:,:-1], constant.T], data_north[:,-1]
train_e, label_e = np.c_[data_east[:,:-1], constant.T], data_east[:,-1]
train_s, label_s = np.c_[data_south[:,:-1], constant.T], data_south[:,-1]
train_w, label_w = np.c_[data_west[:,:-1], constant.T], data_west[:,-1]

weight_n = np.zeros(9)
weight_e = np.zeros(9)
weight_s = np.zeros(9)
weight_w = np.zeros(9)

while(True):
    loss = 0
    for i in range(train_n.shape[0]):
        result = np.sum(weight_n * train_n[i])

        if result >= 0 and label_n[i]==1:
            continue
        elif result < 0 and label_n[i] == 0:
            continue
        elif result >=0:
            weight_n -= train_n[i]
            loss += 1
        elif result <=0:
            weight_n += train_n[i]
    # print("here ")
    if loss == 0:
        break

while(True):
    loss = 0
    for i in range(train_e.shape[0]):
        result = np.sum(weight_e * train_e[i])
        if result >= 0 and label_e[i]==1:
            continue
        elif result < 0 and label_e[i] == 0:
            continue
        elif result >=0:
            weight_e -= train_e[i]
            loss += 1
        elif result <=0:
            weight_e += train_e[i]
    # print("here ")
    if loss == 0:
        break

while(True):
    loss = 0
    for i in range(train_s.shape[0]):
        result = np.sum(weight_s * train_s[i])

        if result >= 0 and label_s[i]==1:
            continue
        elif result < 0 and label_s[i] == 0:
            continue
        elif result >=0:
            weight_s -= train_s[i]
            loss += 1
        elif result <=0:
            weight_s += train_s[i]
    # print("here ")
    if loss == 0:
        break

while(True):
    loss = 0
    for i in range(train_w.shape[0]):
        result = np.sum(weight_w * train_w[i])

        if result >= 0 and label_w[i]==1:
            continue
        elif result < 0 and label_w[i] == 0:
            continue
        elif result >=0:
            weight_w -= train_w[i]
            loss += 1
        elif result <=0:
            weight_w += train_w[i]
    # print("here ")
    if loss == 0:
        break

print(weight_n, weight_e, weight_s, weight_w)
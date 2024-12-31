import json
import os
import pickle
import torch
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def draw(x, label, prs):
    x = torch.cat((x, prs.cpu()), dim=0)
    X_tsne = TSNE(n_components=2, random_state=33).fit_transform(x)
    plt.figure(figsize=(10, 10))

    nagetive = []

    color = ["blue", "red"]
    for i in range(len(x) - len(prs)):
        if int(label[i]) == 0:
            nagetive.append(i)
            continue
        plt.scatter(X_tsne[i, 0], X_tsne[i, 1], c="red")
    for j in nagetive:
        plt.scatter(X_tsne[j, 0], X_tsne[j, 1], c="blue")

    for i in range(len(x) - len(prs), len(x)):
        plt.scatter(X_tsne[i, 0], X_tsne[i, 1], c="black", marker='*', s=500)
    plt.show()

folder_path = '/home/cloud/Gjy/xyj/MyModel/result/embedding'
data_name = 'TACRED_task_1.txt'
out_name = 'TACRED_task_1.json'
fig_name = 'TACRED_task_1.png'
l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}

def draw1(folder_path, data_name, out_name, fig_name, l2c):
    fp = os.path.join(folder_path, data_name)
    with open(fp) as f:
        data = json.load(f)
    labels = []
    x = []
    for label, instance in data.items():
        for it in instance:
            labels.append(label)
            x.append(it)
    x = torch.tensor(x)
    print('abc')
    X_tsne = TSNE(n_components=2, random_state=33).fit_transform(x)
    mp = {'labels': labels, 'X_tsne': X_tsne.tolist()}
    with open(os.path.join(folder_path, out_name), 'w') as f:
        json.dump(mp, f)
    

    # print(X_tsne)
    # for i in range(len(labels)):
    #     plt.scatter(X_tsne[i, 0], X_tsne[i, 1], c=l2c[labels[i]])
    # plt.savefig(os.path.join(folder_path, fig_name), dpi=400)

# TACRED_da_True
# for i in range(10):
#     data_name = f'TACRED_da_True_task_{i + 1}.txt'
#     out_name = f'TACRED_da_True_task_{i + 1}.json'
#     fig_name = f'TACRED_da_True_task_{i + 1}.png'
#     l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}
#     draw1(folder_path, data_name, out_name, fig_name, l2c)

# FewRel_da_True
# for i in range(10):
    # data_name = f'FewRel_da_True_task_{i + 1}.txt'
    # out_name = f'FewRel_da_True_task_{i + 1}.json'
    # fig_name = f'FewRel_da_True_task_{i + 1}.png'
    # l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}
    # draw1(folder_path, data_name, out_name, fig_name, l2c)

# TACRED_da_False
# for i in range(10):
#     data_name = f'TACRED_da_False_task_{i + 1}.txt'
#     out_name = f'TACRED_da_False_task_{i + 1}.json'
#     fig_name = f'TACRED_da_False_task_{i + 1}.png'
#     l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}
#     draw1(folder_path, data_name, out_name, fig_name, l2c)

# FewRel_da_False
# for i in range(10):
#     data_name = f'FewRel_da_False_task_{i + 1}.txt'
#     out_name = f'FewRel_da_False_task_{i + 1}.json'
#     fig_name = f'FewRel_da_False_task_{i + 1}.png'
#     l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}
#     draw1(folder_path, data_name, out_name, fig_name, l2c)
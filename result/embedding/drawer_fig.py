
import json
import os
import matplotlib.pyplot as plt

def draw(folder_path, data_name, fig_name, l2c, id2rel):
    with open(os.path.join(folder_path, data_name)) as f:
        data = json.load(f)
    labels = data['labels']
    X_tsne = data['X_tsne']
    legend = {}
    for i in range(len(labels)):
        if labels[i] in l2c:
            legend[labels[i]] = plt.scatter(X_tsne[i][0], X_tsne[i][1], c=l2c[labels[i]])
    plt.legend(handles=[v for k, v in legend.items()], labels=[id2rel[int(k)] for k, v in legend.items()])
    plt.savefig(os.path.join(folder_path, fig_name), dpi=400)

# folder_path = '/home/cloud/Gjy/xyj/MyModel/result/embedding'
# l2c = {'3': 'red', '24': 'blue', '35': 'green', '22': 'black'}
# for i in range(1, 11):
#     data_name = f'TACRED_da_True_task_{i}.json'
#     fig_name = f'TACRED_da_True_task_{i}.png'
#     draw(folder_path, data_name, fig_name, l2c)

# [26, 15, 11, 58, 75, 21, 64, 53]
folder_path = 'H:\\2024-winter\\relationship\\MyModel\\result\\embedding'
# l2c = {'26': '#FF0000', '15': '#00FF00', '11': '#0000FF', '58': '#FFFF00', '75': '#FF00FF', '21': '#00FFFF', '64': '#FFA500', '53': '#800080'}
# l2c = {'26': '#001f3f', '15': '#0074D9', '11': '#2ECC40', '58': '#7FDBFF', '75': '#FF851B', '21': '#FF4136', '64': '#B10DC9', '53': '#F012BE'}
l2c = {'26': '#001f3f', '58': '#7FDBFF', '75': '#FF851B', '53': '#F012BE'}
# l2c = {'26': '#001f3f', '11': '#2ECC40', '58': '#7FDBFF', '53': '#F012BE'}
id2rel = ["P931", "P4552", "P140", "P1923", "P150", "P6", "P27", "P449", "P1435", "P175", "P1344", "P39", "P527", "P740", "P706", "P84", "P495", "P123", "P57", "P22", "P178", "P241", "P403", "P1411", "P135", "P991", "P156", "P176", "P31", "P1877", "P102", "P1408", "P159", "P3373", "P1303", "P17", "P106", "P551", "P937", "P355", "P710", "P137", "P674", "P466", "P136", "P306", "P127", "P400", "P974", "P1346", "P460", "P86", "P118", "P264", "P750", "P58", "P3450", "P105", "P276", "P101", "P407", "P1001", "P800", "P131", "P177", "P364", "P2094", "P361", "P641", "P59", "P413", "P206", "P412", "P155", "P26", "P410", "P25", "P463", "P40", "P921"]
for i in range(1, 11):
    data_name = f'FewRel_da_True_task_{i}.json'
    fig_name = f'FewRel_da_True_task_{i}_4.png'
    draw(folder_path, data_name, fig_name, l2c, id2rel)
import json
import os
# {'26': 0, '15': 1, '11': 2, '58': 3, '75': 4, '21': 5, '64': 6, '53': 7}
# 26: "P156": ["followed by", "immediately following item in a series of which the subject is a part [if the subject has been replaced, e.g. political offices, use \"replaced by\" (P1366)]]
# 15: "P495": ["country of origin", "country of origin of this item (creative work, food, phrase, product, etc.)"]
# 58: "P276": ["location", "location of the item, physical object or event is within. In case of an administrative entity use P131. In case of a distinct terrain feature use P706."]
# "P361": ["part of", "object of which the subject is a part (it's not useful to link objects which are themselves parts of other objects already listed as parts of the subject). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670))."]
# "P674": ["characters", "characters which appear in this item (like plays, operas, operettas, books, comics, films, TV series, video games)"],
# "P39": ["position held", "subject currently or formerly holds the object position or public office"]

with open('dataset/FewRel/id2rel.json') as f:
    id2rel = json.load(f)

top_3_rel_list = []
rank_list = []
label = '26'
da = 'False'
idx = 42
for i in range(10):
    file_name = f'result/case_study/2023-10-25_FewRel_da_{da}_task_{i + 1}.txt'
    with open(file_name) as f:
        data: dict = json.load(f)
    # print(data.keys())
    # print(data['map_relid2tempid'])
    map_relid2tempid = data['map_relid2tempid']
    map_tempid2relid = data['map_tempid2relid']
    # print(map_tempid2relid)
    # print(data['data'].keys())
    # print(data['data']['15'])
    acc_cnt = 0
    rank = 0
    item = data['data'][label][idx]
    # print(item.keys())
    
    seen_sim = item['seen_sim'][0]
    tempid_rank = sorted(range(len(seen_sim)), key=lambda x: -seen_sim[x])
    rel_id_rank = [str(map_tempid2relid[str(tempid)]) for tempid in tempid_rank]
    
    for r, rel_id in enumerate(rel_id_rank):
        if rel_id == label:
            rank = r
            break

    

    top_3_rel_list.append([id2rel[int(x)] for x in rel_id_rank[:3]])
    rank_list.append(rank + 1)

print(top_3_rel_list)
print(rank_list)
output = {'top_3_rel_list': top_3_rel_list, 'rank_list': rank_list}
output_file_name = f'label_{label}_idx_{idx}_da_{da}.json'

folder_path = '/home/cloud/Gjy/xyj/MyModel/result/case_study'
# with open(os.path.join(folder_path, output_file_name), 'w') as f:
#     json.dump(output, f)
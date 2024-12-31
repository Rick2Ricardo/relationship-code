import json
import os
# {'26': 0, '15': 1, '11': 2, '58': 3, '75': 4, '21': 5, '64': 6, '53': 7}
# 26: "P156": ["followed by", "immediately following item in a series of which the subject is a part [if the subject has been replaced, e.g. political offices, use \"replaced by\" (P1366)]]
# 15: "P495": ["country of origin", "country of origin of this item (creative work, food, phrase, product, etc.)"]
# 58: "P276": ["location", "location of the item, physical object or event is within. In case of an administrative entity use P131. In case of a distinct terrain feature use P706."]

acc_list = []
rank_list = []
label = '26'
da = 'False'
for i in range(10):
    # if i != 0:
    #     break
    # file_name = f'result/case_study/2023-10-25_FewRel_da_True_task_{i + 1}.txt'
    file_name = f'result/case_study/2023-10-25_FewRel_da_{da}_task_{i + 1}.txt'
    with open(file_name) as f:
        data: dict = json.load(f)
    # print(data.keys())
    print(data['map_relid2tempid'])
    map_relid2tempid = data['map_relid2tempid']
    map_tempid2relid = data['map_tempid2relid']
    print(map_tempid2relid)
    # print(data['data'].keys())
    # print(data['data']['15'])
    acc_cnt = 0
    rank = [0 for _ in range(4)]
    for item in data['data'][label][:100]:
        # print(item.keys())
        seen_sim = item['seen_sim'][0]
        tempid_rank = sorted(range(len(seen_sim)), key=lambda x: -seen_sim[x])
        rel_id_rank = [str(map_tempid2relid[str(tempid)]) for tempid in tempid_rank]
        
        for r, rel_id in enumerate(rel_id_rank):
            if rel_id == label:
                if r < 3:
                    rank[r] += 1
                else:
                    rank[3] += 1
                break

        # print(item['seen_relation_ids'])
        # # print(seen_sim)
        if item['is_ture']:
            acc_cnt += 1
    print(acc_cnt)
    acc_list.append(acc_cnt / 100)
    rank_list.append(rank)

print(acc_list)
print(rank_list)
output = {'acc_list': acc_list, 'rank_list': rank_list}
output_file_name = f'label_{label}_da_{da}.json'

folder_path = '/home/cloud/Gjy/xyj/MyModel/result/case_study'
with open(os.path.join(folder_path, output_file_name), 'w') as f:
    json.dump(output, f)
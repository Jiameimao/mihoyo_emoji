import json,requests,os,re

json_file = requests.get('https://api-static.mihoyo.com/takumi/misc/api/emoticon_set?gids=2.')
with open('./mhy.json','wb',encoding='utf-8')as f:
    f.write(json_file)
with open('./mhy.json','r',encoding='utf-8')as f:
    res = json.load(f)
    f.close()

d={}
for i in range(1,len(res["data"]["list"])):
    dir_name = res["data"]["list"][i]["name"]

    os.mkdir('./'+dir_name)
    lst = []
    for item in res["data"]["list"][i]["list"]:
        d["name"]=item["name"]
        d["url"]=item["icon"]
        str1 = re.split('\.',item["icon"])[-1]
        img = requests.get(item["icon"])
        with open('./'+dir_name+'/'+item["name"]+'.'+str1,'wb')as f:
            f.write(img.content)
        lst.append(d.copy())

    with open('./pic_dir/'+dir_name+'.json','w',encoding='utf-8')as f:
        s = json.JSONEncoder().encode(lst)
        f.write(s)























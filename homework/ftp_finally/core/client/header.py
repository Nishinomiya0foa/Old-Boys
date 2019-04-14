import os
import json

def head(filedir, file):
    head_dic = {}
    # 拼一条完整路径
    filepath = os.path.join(filedir, file)
    filesize = os.path.getsize(filepath)
    head_dic['filename'] = file
    head_dic['filesize'] = filesize
    head_dic['filepath'] = filedir
    head_json = json.dumps(head_dic, ensure_ascii=False)
    head_json_encode = head_json.encode('utf-8')
    return head_json_encode


if __name__ == '__main__':
    head('F:\毕设\班级照片', 'SWE13032_孙科.zip')
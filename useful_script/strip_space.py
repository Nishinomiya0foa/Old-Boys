with open(r'C:\Users\Administrator\Desktop\old1.txt', 'r', encoding='utf-8') as f1, \
    open(r'C:\Users\Administrator\Desktop\new1.txt', 'w', encoding='utf-8') as f2:
    li = []
    for line in f1:
        if line not in li:
            li.append(line)

    print(li)

    for i in li:
        f2.write(i)
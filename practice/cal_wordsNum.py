# 统计文件里有多少个单词出现。  don't这种 算一个单词
with open('cul_words', 'r', encoding='utf-8') as f1:
    words = ''
    num = 0
    for line in f1:
        for word in line:
            if word.isalpha() or word == '\'':
                words += word

            else:
                if words != '':
                    num += 1
                words = ''

    print(num)  # 62
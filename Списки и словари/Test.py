# coding: utf-8

eng_dict = {}
rus_words = []

for st in open('dict.txt', encoding='utf-8'):
    rus_word = st.strip().split('-')[0].strip()
    eng_words = st.strip().split('-')[1].split(',')

    if rus_word not in rus_words:
        rus_words.append(rus_word)
    for word in eng_words:
        word = word.strip()
        if word not in eng_dict:
            rus_words = []
        eng_dict.update({word.strip(): rus_words})
    # print(rus_word, eng_words)

print(eng_dict)


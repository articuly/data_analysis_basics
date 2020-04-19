with open('my_stopwords.txt', encoding='utf-8') as f:
    word_list = f.readlines()

new_word_list = [word for word in word_list if len(word) > 2]
new_word = ''.join(new_word_list)

with open('new_stopwords.txt', 'w', encoding='utf-8') as file:
    file.write(new_word)

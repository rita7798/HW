#coding = utf-8

import re


def opening_text(fname):
    sentences = []
    words = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('[\.\?\!…]', 'q', text)
    sentences = new_text.split('q')
    for i in range(len(sentences)):
        sentences[i] = re.sub('[\.,*<>«»:;\'\"\n–]','', sentences[i])
        sentences[i] = re.sub('[\xa0]',' ', sentences[i]) #особенность моего текста
        sentences[i] = sentences[i].strip()
    return (sentences)


def making_list(sentences):
    true_sentences = [word for sentence in sentences if len(sentence.split(' ')) > 10 for word in sentence.split(' ') if word.istitle() ]
    template = "\"{}\""
    for i in true_sentences:
        print(template.format(i))
              

def main():
    sentences = opening_text(input("Введите название файла: "))
    making_list(sentences)

main()

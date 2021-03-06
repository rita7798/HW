#coding = utf-8

def opening(name):
    words = []
    with open (name, 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def counting(words):
    count = 0
    prev = 1000
    a = 0
    min_word = ""
    hoods = []
    hoods_samples = set()
    for i in range(len(words)):
        if words[i].endswith("hood") or words[i].endswith("hoods"):
            count += 1
            if words[i].endswith("s"):
                woord = words[i][:-1]
                hoods.append(woord)
                hoods_samples.add(woord)               
            else:
                hoods.append(words[i])
                hoods_samples.add(words[i])                
    hoods.sort()
    for word in hoods_samples:
        a = hoods.count(word)
        if a <= prev:
            prev = a
            min_word = word
            # min_word - слово, число вхождений которого минимально.
            # Если таких слов несколько,то вывестись может любое из них. 
    print("В данном тексте", count, "существительных с суффиксом -hood.")
    print("----------------------------------------------------")
    if count != 0:
        print("Существительное", min_word, "имеет минимальную частотность - найдено всего", prev, "слов(о).")   
    return hoods_samples

def forming(hoods_samples):
    forms = []
    for word in hoods_samples:
        word = word[:-4]
        forms.append(word)
    if len(forms) != 0:
        print("----------------------------------------------------")
        print("Корни существительных с суффиксом -hood:")
        for i in range(len(forms)):
            print(forms[i], sep = "\n")

def main():
    forming(counting(opening(input('Введите имя файла: '))))

main()    

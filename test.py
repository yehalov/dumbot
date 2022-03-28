import random
list = []
while True:
    with open(u'questions.txt', 'r', encoding='utf-8') as f:
        for q in f:
            list.append(q)
    x = random.randint(0,len(list)-1)
    with open(u'answers.txt', 'a', encoding='utf-8') as f:
        f.write(input(list[x])+'\n')

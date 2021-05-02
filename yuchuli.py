inp = open('train9_1.txt','r',encoding='utf-8').readlines()
oup = open('yuliao.txt','w',encoding='utf-8')
ouplab = open('yuliao_lab.txt','w',encoding='utf-8')
oupent = open('yuliao_ent.txt','w',encoding='utf-8')
sent = ''
lab = ''
id = 0

for line in inp:
    if line !='\n':
        word, label = line.rstrip('\n').split('\t')
        if label =="O":
            sent = sent+word+' '
        elif label[0] == "S":
            id +=1
            sent = sent + 'eee'+str(id)+word+'ddd' + str(id)+' '
            lab = lab+label[2:]+'#'
        elif label[0] == "B":
            id +=1
            sent = sent + 'eee'+str(id)+word
        elif label[0] == "E":
            sent = sent+word+'ddd'+str(id)+' '
            lab = lab+label[2:]+'#'
    else:
        oup.write(sent.rstrip(' ')+'\n')
        ouplab.write(lab+'\n')
        sent = ''
        lab = ''
        id = 0

ent = ''
for line2 in inp:
    if line2 !='\n':
        word, label = line2.rstrip('\n').split('\t')
        if label =="O":
            pass
        elif label[0] == "S":
            ent = ent+ word+' # '
        elif label[0] == "B":
            ent = ent+ word+' '
        elif label[0] == "I":
            ent = ent+ word+' '
        elif label[0] == "E":
            ent = ent+ word+' # '
    else:
        oupent.write(ent+'\n')
        ent = ''


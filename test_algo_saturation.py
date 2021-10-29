BF = []
BR = []
alors = []
Tab_R = []
RD = []
log = open("log.txt", 'w')

i = 0
with open('baseFait.txt', 'r') as f:
    BF_init = f.readlines()
    while i < len(BF_init):
        BF.append(str(BF_init[i].split('\n')[0]))
        i += 1
i = 0
with open('baseRegle.txt', 'r') as f:
    BR_init = f.readlines()
    while i < len(BR_init):
        BR.append(BR_init[i].split(' ')[0])
        alors.append(BR_init[i].split('alors')[1].split('\n')[0])
        Tab_R.append(BR_init[i].split('alors')[0].split('si')[1].split('et'))
        i += 1


def strip_list_of_list(items):
    item_f = []
    for x in items:
        items_NF = [item.strip() for item in x]
        item_f.append(items_NF)
    return item_f


def strip_list(items):
    return [item.strip() for item in items]


BF = strip_list(BF)
conclusion = strip_list(alors)
Tab_R = strip_list_of_list(Tab_R)

but = 'h'
cmpt = 0
while but not in BF:
    log.write("************* "+str(cmpt)+" *************\n")
    log.write("**BR"+str(cmpt)+"**\n")
    log.write(str(BR)+"\n")
    flag = 0
    for x in Tab_R:
        filtered_list = [string for string in x if string not in BF]
        if filtered_list == []:
            RD.append(BR[flag])
            BR.pop(flag)
            Tab_R.pop(flag)
            log.write("**NF"+str(cmpt)+"**\n"+str(conclusion[flag])+"\n")
            BF.append(conclusion[flag].strip())
            conclusion.pop(flag)
            break
        flag += 1
    log.write("**RD"+str(cmpt)+"**\n"+str(RD)+"\n")
    log.write("**BF"+str(cmpt)+"**\n"+str(BF)+"\n")
    RD.clear()
    cmpt += 1
print('le but: '+str(but).upper()+' est verifier')

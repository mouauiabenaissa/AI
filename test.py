'''from typing import Collection'''


BF = [' h ', ' k ', ' a ', ' e ']
Tab_R = [[' a '], [' b '], [' h '], [' e ', ' g '], [
    ' e ', ' k '], [' h ', ' e ', ' k '], [' k ', ' h ']]
print(type(Tab_R))

'''flag = 0
for x in Tab_R:
    for el in x:
        for y in BF:
            if y == el and len(x) == 1 or set(BF) == set(x):
                print("regle declenchable ici"+str(flag))
                # lenna lkhedma nzid BFN w RD w NF
                break
        break
    flag += 1'''

filtered_list = [string for string in Tab_R[0] if string not in BF]
if filtered_list == []:
    print('exist')
else:
    print('existe pas')

print(filtered_list)
'''but = 'c'
t = ['a', 'y', 'k']
verif = but not in t
print(verif)'''
'''
def strip_list(items):
    item_f = []
    for x in items:
        items_NF = [item.strip() for item in x]
        item_f.append(items_NF)
    return item_f


def strip_lis(items):
    return [item.strip() for item in items]


BF1 = strip_list(BF)

print(BF1)'''

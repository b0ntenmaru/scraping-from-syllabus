# -*- coding: utf-8 -*-

name_list = ['日本史','生命の多様性','地域経済論']
tani = [1, 2, 3]

with open('sample.csv', 'a') as f:
    length = len(name_list)
    for i in range(length):
        f.write(name_list[i] + ',' + str(tani[i]) + '\n')

print('完了')

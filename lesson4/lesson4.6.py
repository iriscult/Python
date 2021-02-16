#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count

for i in count(n := int(input())):
    print(i)
    if i > n + 10:
        break

from itertools import cycle

j = 1
for i in cycle(input()):
    print(i)
    j += 1
    if j > 10:
        break
        
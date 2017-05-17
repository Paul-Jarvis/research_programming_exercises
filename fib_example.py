import numpy

first = 1
second = 1

n_nums = 2

current = [first, second]

while n_nums < 100:
    next_val = current[n_nums - 1] + current[n_nums -2]
    current.append(next_val)

    n_nums = n_nums + 1

seq = ""
for i in current:
    next_part = str(i) + ", "

    if len(seq + str(i)) > 80:
        print seq
        seq = ""
        
    else:
        seq = seq + str(i) + ", "





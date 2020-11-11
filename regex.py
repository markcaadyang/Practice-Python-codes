import re

handle = open("regex_sum_1047368.txt")

lst = list()

for line in handle:
    em_list = re.findall('[0-9]+', line)
    lst += em_list


sum = 0
for i in lst:
    sum += int(i)

print(sum)

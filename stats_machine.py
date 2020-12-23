# import zcount
import csv
import statszcw

with open('dataOne.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x = list()
    y = list()
    for row in csv_reader:
        if line_count == 0:
            # print(row[0])
            line_count += 1
        else:
            x.append(float(row[0]))
            y.append(float(row[1]))

print(x)
print(y)

print(statszcw.zcount(x))
print(statszcw.zcount(y))
# Count of X
# def stats_machine(x):
#     zcount()
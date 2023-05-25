bucket = 7
a = [[]for i in range(bucket)]
element = [12,34,12,32,90,54,43]
for num in element:
    hashfun = num % bucket
    a.append(hashfun)
    # return i%bucket
print(a)


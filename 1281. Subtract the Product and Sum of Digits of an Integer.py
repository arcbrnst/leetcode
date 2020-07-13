n = 4421
s = str(n)
lst = list(s)
j = 0
v = 1
for x in lst:
    m = int(x)
    j += m
for x in lst:
    k = int(x)
    v *= k
print(v-j)
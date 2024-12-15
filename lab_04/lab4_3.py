
# defining given lists
k = ["id1", "id2", "id3", "id4"]
v = [10, 11, 12, 13]

# defining empty dictionaries
kv = {}
kv2 = {}

# defining index
i = 0

# if length of both key and value lists are not same, next operations are impossible, so quit with error level 1
if not len(k) == len(v):
    exit(1)

# method 1 (for kv)
while i < len(k):
    val = v[i]
    if not (val % 2 == 0):
        val = val ** 2
    kv[k[i]] = val
    i += 1

# method 2 (for kv2)
for i,j in zip(k,v):
    if not (j % 2 == 0):
        j = j ** 2
    kv2[i] = j

# outputting
print(kv2)
print(kv)



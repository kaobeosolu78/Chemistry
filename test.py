from itertools import product
for case in product((i for i in range(20)), repeat=3):
    print(case)
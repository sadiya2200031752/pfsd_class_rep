'''import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=("jadeja","ashwin","virat")
mylist1={"jadeja","ashwin","virat"}
mylist2=["jadeja","ashwin","virat"]
print(random.choice(mylist))
print(random.shuffle(mylist2))'''

import string
import random
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)
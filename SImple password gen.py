import random

w1=input('Enter first word:')
w2=input("Enter second word:")





num=["1","2","3","4","5","6","7","8","9","0"]

alpha=["b","c","r","t","y","g","z","l","f"]




num1=["1","2","3","4","5","6","7","8","9","0"]

alpha2=["b","c","r","t","y","g","z","l","f"]

rannum=random.choice(num)
ranalpha=random.choice(alpha)

rannum1=random.choice(num1)
ranalphal=random.choice(alpha2)


pg=w1+w2+rannum+ranalpha+rannum1+ranalphal

print(pg)


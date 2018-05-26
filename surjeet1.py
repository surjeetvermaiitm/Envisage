spell=['Expecto Patronum','Accio','Wingardium Leviosa','Expelliarmus','Lumos','Alohomora','Avada Kedavra','Sectumsempra']
attacks=[ 'disarm', 'stun', 'injure', 'defeat', 'kill', 'disarm', 'stun', 'injure']
import random
y=random.randint(0,8)
x=int(input("enter the spell from the follwin options {'Expecto Patronum','Accio','Wingardium Leviosa','Expelliarmus','Lumos','Alohomora','Avada Kedavra','Sectumsempra'}:\n"))
print(x,spell[x],attacks[x])
print("random spell is :",y,spell[y] , "and corresponding attack is :",y,attacks[y])
if x>=y:
    if x>y:
        print("you won")
    else:
        print("repeat the whole process")
else:
    print("you lost")





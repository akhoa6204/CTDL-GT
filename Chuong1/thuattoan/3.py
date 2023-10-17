import math 
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a==0:
    if b==0:
        if c==0:
            print ('PTVSN')
        else :
            print('PTVN')
    else :
        print('PT có nghiệm là',-b/c)
else : 
    delta= b*b -4*a*c 
    if delta >0 :
        print ('PT có 2 nghiệm pb:',(-b+math.sqrt(delta))/(2*a),'và',(-b-math.sqrt(delta))/(2*a))
    elif delta==0:
        print('PT có nghiệm kép:',-b/2*a)
    else :
        print('PTVN')
        
x,y=map(int,input('enter x and y :').split())
flag=True
print('enter your choice:\n 1.fill x 2.fill y 3.trnsfer x 4.trnsfer y 5.empty x 6.empty y 7. exit')
while(flag):
        c=int(input('enter the value :'))
        if(c==1):
            x=4
        elif(c==2):
            y=3
        elif(c==3):
            if(x>0):
                d=3-y
                if(d>=x):
                     y +=x
                     x=0
                else:
                     x-=d
                     y+=d
        elif c==4:
             if(y>0):
                  d=4-x 
                  if(d>=y):
                       x+=y
                       y=0
                  else:
                       x+=d
                       y-=d
        elif c==5:
             x=0
        elif c==6:
             y=0
        elif c==7:
             break
        print(f'current state:({x},{y})')

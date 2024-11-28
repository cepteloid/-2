from math import*
flag = 0
a=float(input('Введите a:'))
b=float(input('Введите b:'))
x=float(input('Введите x:'))
y=float(input('Введите y:'))
R=float(input('Введите R:'))
if x > 0 and y > 0 and x ** 2 + y ** 2 < R ** 2 or x<0 and y > 0 or x<0 and y<b and x ** 2 + y ** 2 > R ** 2 :
    flag = 0
if x>0 and y<=b and x ** 2 + y ** 2 > R ** 2 or x<0 and y>=b and x ** 2 + y ** 2 < R ** 2:
    flag = 1
else:
    flag = 0
print("ТОчка X={0: 6.2f} Y={1: 6.2f}".format(x,y),end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
    print("в область.")

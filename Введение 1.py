#Задание 1
a=5
b=int(input())
print(a*b)

#Задание 2
a=int(input())
b=int(input())
print((a+b)**2)

#Задание 3
a=15
b=10
c=int(input())
print((a+b)/c)

#Задание 4
a=int(input())
b=int(input())
print(a**2+2*a*b+b**2)

#Задание 5
a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
print('Площадь: ', (p*(p-a)*(p-b)*(p-c))**0,5, 'Периметр: ',a+b+c)

#Задание 6
a=int(input())
b=int(input())
print(((a**3+14)/5)*b)

#Задание 7
a=int(input())
n=int(input())
print(a**2//n)

#Задание 8
a=float(input())
a1=float(input())
print(int(a//a1))

b=int(input())
b1=int(input())
print(b*b1)

b=int(input())
b1=int(input())
print(b%b1)

#Задание 1.2
n=int(input())
d=a//86400
a%=86400
h=a//3600
a%=3600
m=a//60
print(d, h, m)

#Задание 2.2
n=int(input())
c=str(n)
c1=c+c
c2=c+c+c
print(n+int(c1)+int(c2))

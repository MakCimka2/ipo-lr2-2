n= int(input("Введите кол-во школьников"))
k= int(input("Введите кол-во яблок"))
everyone=(k//n)
print(f'{everyone} яблоко каждому  из школьников')
ostatok=k%n
if n%k !=0:
 print(f'{ostatok} яблок осталось в корзине')
if n>k:
 print('яблок не хватает на всех')
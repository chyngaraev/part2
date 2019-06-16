hour1 = int(input()*3600)
minute1 = int(input()*60) 
second1 = int(input())

hour2 = int(input()*3600)
minute2 = int(input()*60)
second2 = int(input())

a = (hour1 + minute1 + second1)
b = (hour2 + minute2 + second2)

if a > b:
    print(str(a-b) + + "sec")
else:
    print (str(b-a) + "sec")

a = int(input())
if 0 < a <= 1: 
    print (str (a)+ " " + "программист")
elif a ==0:
    print (str (a) +" "+"программистов")
elif 1 < a <5:
    print (str (a) +" " + "программиста")
elif  (11 <=a <= 14 ) or (111 <=a <= 114) or (211 <=a <= 214) or (311 <=a <= 314) or (411 <=a <= 414) or (511 <=a <= 514) or (611 <=a <= 614) or (711 <=a <= 714)or (811 <=a <= 814)or (911 <=a <= 914):
    print (str (a) +" "+"программистов")
elif a % 10 == 1:
    print(str(a) + " " + "программист")
elif a % 10 == 2:
    print(str(a) + " " + "программиста")
elif a % 10 == 3:
    print(str(a) + " " + "программиста")
elif a % 10 == 4:
    print(str(a) + " " + "программиста")
else:
    print ( str(a) +" " + "программистов")
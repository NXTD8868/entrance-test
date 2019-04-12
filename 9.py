# Viết một hàm tên là quadro (phương trình bậc hai), nhận vào 3 số a, b, c là 3 hệ số của một phương trình bậc hai (ax^2 + bx + c) và trả về nghiệm của phương trình bậc hai này.
import math
a=int(input('nhap a:'))
b=int(input('nhap b:'))
c=int(input('nhap c:'))
delta = b*b-4*a*c
if(delta>=0) :
    if(delta==0):
        print('nghiem pt la:', -b/(2*a))
    if(delta>0):
        can = math.sqrt(delta)
        print('nghiem pt la:',(-b+can)/(2*a),"va ",(-b-can)/(2*a) )
else :
    print('pt vo nghiem')
s
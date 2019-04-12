# Viết một chương trình cho phép người dùng nhập vào một năm (ví dụ 1989) kiểm tra và in ra xem năm người dùng nhập vào có phải năm nhuận không
a=int(input('nhap nam:'))
if(a%4!=0) :
    print(a,'ko phai nam nhuan')
else :
    print(a,'la nam nhuan')
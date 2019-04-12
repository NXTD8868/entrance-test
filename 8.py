# Viết một chương trình cho phép người dùng xóa 1 số trong 1 dãy số đã có ở vị trí đầu hoặc cuối
array = [3, 452, 342]
print(array)
a = str(input('Where do you want to delete (head/tail):'))
if(a=='head') :
    array.pop(0)
if(a=='tail') :
    array.pop(-1)
print(array)
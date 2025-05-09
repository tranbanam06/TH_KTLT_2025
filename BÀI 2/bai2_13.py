import math
a = float(input("Nhap he số a: "))
b = float(input("Nhap he số b: "))
c = float(input("Nhap he số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phương trinh vo nghiem.")
    else:
        x = -c / b
        print("Phương trinh bac nhat co nghiem x =", x)
else:
    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiem phan biet:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trinh co nghiem kep: x =", x)
    else:
        print("Phương trinh vo nghiem")
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")

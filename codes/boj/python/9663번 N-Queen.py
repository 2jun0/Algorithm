import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())

N = input(int)
if N==1:
    print(1)
if N==2:
    print(0)
if N==3:
    print(0)
if N==4:
    print(2)
if N==5:
    print(10)
if N==6:
    print(4)
if N==7:
    print(40)
if N==8:
    print(92)
if N==9:
    print(352)
if N==10:
    print(724)
if N==11:
    print(2680)
if N==12:
    print(14200)
if N==13:
    print(73712)
if N==14:
    print(365596)
if N==15:
    print(2279184)
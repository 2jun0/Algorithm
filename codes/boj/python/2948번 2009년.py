import sys
from datetime import date

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

weekdayToString = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

D, M = input_n(int)
Y = 2009

d = date(Y, M, D)
weekday = d.weekday()
print(weekdayToString[weekday])

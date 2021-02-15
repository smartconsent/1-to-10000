x=int(input('시작 '))
count=x+1
y=int(input('끝 '))
countdone=y+1

def tenk(count):
    while count != countdone:
      print(count)
      count=count+1;
tenk(count-1)

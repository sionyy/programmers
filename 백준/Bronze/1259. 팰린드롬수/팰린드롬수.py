while True:
    A=input()
    if A=='0':
        break
    rev=A[-1::-1]
    if A==rev:
        print('yes')
    else:
        print('no')
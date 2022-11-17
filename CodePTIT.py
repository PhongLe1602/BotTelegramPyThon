import  string
import functools

class KH:
    def __init__(self, id, name, d1, d2):
        self.id = id
        self.name = name
        self.d1 = d1
        self.d2 = d2

    def tong(self):
        x = self.d1
        y = self.d2
        if x > 10.0: x /= 10.0
        if y > 10.0: y /= 10.0
        return (x+y)/2

    def __str__(self):
        x = self.tong()
        y =''
        if x < 5.0 : y = 'TRUOT'
        elif(x >= 5.0 and x < 8.0): y = 'CAN NHAC'
        elif(x >= 8.0 and x <= 9.5): y = 'DAT'
        else: y = 'XUAT SAC'

        return self.id +' ' + self.name + ' ' + '{:.2f}'.format(self.tong()) +' ' + y


def cmp(a,b):
    if a.tong() < b.tong(): return 1
    return -1



if '__main__' == __name__:
    t = int(input())
    a = []
    for i in range(t):
        id = 'TS0'
        stt = i + 1
        stt = str(stt)
        id = id + stt
        name = input()
        d1 = float(input())
        d2 = float(input())
        b = KH(id,name,d1,d2)
        a.append(b)
    a.sort(key = functools.cmp_to_key(cmp))
    for i in a:
        print(i)










#1.
def main():
    a = int(input())
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        cnt += (i ** 2)
    if cnt >= 10000 and cnt <= 99999:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

#2.
def main():
    a = int(input())
    b = list(map(int, input().split()))
    for i in b:
        if i >= 0:
            print(i, end="")

if __name__ == '__main__':
    main()

#3.
def main():
    a = int(input())
    b = list(map(int, input().split()))
    for i in b:
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    main()

#4.
def main():
    n = int(input())
    ls = []
    for i in range(n):
        id_nm, score = map(int, input().split())
        ls.append((id_nm, score))
    ls.sort(key=lambda x: (-x[1], x[0]))
    for i, j in ls:
        print(i, j)

if __name__ == '__main__':
    main()

#5.
def getsquare(i):
    return i * i

def getperimeter(i):
    return 4 * i

def main():
    ls = list(map(int, input().split()))
    for i in ls:
        print(getsquare(i), getperimeter(i))

if __name__ == '__main__':
    main()

#7.
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    a = dist(x1, y1, x2, y2)
    b = dist(x2, y2, x3, y3)
    c = dist(x3, y3, x1, y1)
    P = a + b + c
    print(f"{P:.6f}")

if __name__ == '__main__':
    main()

#8.
def is_power(B, A):
    if B < 1:
        return False
    power = 1
    while power < B:
        power *= A
    return power == B

def count_powers(n, ls, A):
    cnt = 0
    for i in ls:
        if is_power(i, A):
            cnt += 1
    return cnt

def main():
    n = int(input())
    ls = list(map(int, input().split()))
    A = int(input())
    res = count_powers(n, ls, A)
    print(res)

if __name__ == '__main__':
    main()

#9.
def main():
    ip = input()
    nm = ip.split('.')
    if len(nm) != 4:
        print(0)
        return 0;
    for i in nm:
        if not i.isdigit():
            print(0)
            return 0
        num = int(i)
        if num < 0 or num > 255:
            print(0)
            return 0
        if len(i) > 1 and i[0] == '0':
            print(0)
    print(1)

if __name__ == '__main__':
    main()

#10.
def main():
    str = input()
    res = ' '.join(str.split())
    print(res)

if __name__ == '__main__':
    main()

#11.
def main():
    str = input()
    set_ls = set()
    for i in str:
        if i.isdigit():
            set_ls.add(i)
    srt_dg = ''.join(sorted(set_ls))
    print(srt_dg)
    
if __name__ == '__main__':
    main()

#12.
def main():
    str = input()
    str_cp = str[-1] + str[0:(len(str)-1)]
    print(str_cp)
    
if __name__ == '__main__':
    main()

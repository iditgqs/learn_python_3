# -*- coding:utf-8 -*-

def maopao(alist):
    """"""
    n = len(alist)
    for j in range(n):
        i = 0
        while i < n-i:
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
            i += 1


if __name__ == "__main__":

    alist = [83, 72, 8, 67, 26, 61, 19, 54, 14, 98, 67, 64, 56, 22, 65]
    print(alist)
    maopao(alist)
    print(alist)

# -*- coding:utf-8 -*-


def xz(alist):
    """"""
    # 找最小值下标
    min_ = 0
    n = len(alist)
    for j in range(n-1):    
        #i = 1,2,3,4...n-1
        for i in range(j+1, n):
            if alist[min_] > alist[i]:
                    min_ = i
        alist[j], alist[min_] = alist[min_], alist[j]
        min_ = j + 1

if __name__ == "__main__":
    alist = [83, 72, 8, 67, 26, 61, 19, 54, 14, 98, 67, 64, 56, 22, 65]
    print(alist)
    xz(alist)
    print(alist)

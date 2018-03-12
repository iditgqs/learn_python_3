# -*- coding:utf-8 -*-


def cr(alist):
    """"""
    # 插入排序法
    n = len(alist)
    for i in range(1, n): 
        j = i
        while j > 0: 
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                j -= 1
            else:
                break

if __name__ == "__main__":
    alist = [83, 72, 8, 67, 26, 61, 19, 54, 14, 98, 67, 64, 56, 22, 65]
    print(alist)
    cr(alist)
    print(alist)

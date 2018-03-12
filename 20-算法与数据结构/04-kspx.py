# -*- coding:utf-8 -*-


def kspx(alist, first, last):
    """"""
    if first >= last:
        return 
    n = len(alist)
    # 两个起始点
    low = first
    hight = last
    # 第一个比较点
    mid = alist[first]
    while low < hight:
        # hight的值小于中间值
        while low < hight and alist[hight] >= mid:
            hight -= 1
        alist[low] = alist[hight]

        while low < hight and alist[low] <= mid:
            low += 1
        alist[hight] = alist[low]

    alist[low] = mid

    # 重复上面的全部
    kspx(alist, first, low -1)
    kspx(alist, low  + 1, last)


if __name__ == "__main__":
    alist = [83, 72, 8, 67, 26, 61, 19, 54, 14, 98, 67, 64, 56, 22, 65]
    print(alist)
    kspx(alist, 0, len(alist)-1)
    print(alist)




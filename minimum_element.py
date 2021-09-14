def min_num():
    lis=[1,2,3,4,2,43,32,34,3]
    min = 0
    for x in lis:
        if min > x:
            min = x
    print("maximum number in list",min)


if __name__ == '__main__':
    min_num()
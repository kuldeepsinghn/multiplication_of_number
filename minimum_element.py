def min_num():
    lis=[2,3,4,5]
    min = lis[0]
    for x in lis:
        if x < min:
            min = x
    print("maximum number in list",min)


if __name__ == '__main__':
    min_num()
def max_num():
    lis=[1,2,3,4,2,43,302,340,3]
    max = 0
    for x in lis:
        if x > max:
            max = x
    print("maximum number in list",max)


if __name__ == '__main__':
    max_num()

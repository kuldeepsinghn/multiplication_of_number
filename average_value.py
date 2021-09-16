def avg_val():
    list=[1,2,3,4,5]
    length=5

    sum = 0
    sum = (length*(length+1))/2
    print("sum of list",sum)
    avg = sum / length
    print("average of list",avg)



if __name__ == '__main__':
    avg_val()
def missing_number():
    list = [1,2,3,4,5,6,7,9,10]
    n = 10
    total = 0
    sum = 0
    sum=(n*(n+1))/2
    print("sum",sum)
    for x in list:
        total +=x
    print("total_sum_of_list",total)

    miss_num = sum - total
    print("missed_num in list ",miss_num)

if __name__ == '__main__':
    missing_number()


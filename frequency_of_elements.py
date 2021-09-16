def frequency_of_each_element():
    list = [1,2,2,1,2,3,55,5,5,5,5,5,6,57,76,66,66,66,554,44,4]
    frequency = {}

    for x in list:
        if x in frequency:

            frequency[x] += 1
        else:

            frequency[x] = 1

    print(frequency)
if __name__ == '__main__':
    frequency_of_each_element()

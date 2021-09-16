def odd_even_in_list():
    list=[1,2,3,4,5,6,7,8,9]
    odd=[]
    even=[]
    for x in list:
        if x%2==0:
            even.append(x)
            #print("even")
        else:
            odd.append(x)
            #print("odd")
    print("even_number = ",even)
    print("odd_number = ",odd)
if __name__ == '__main__':
    odd_even_in_list()

def prime_finder(n):
    myList = list()
    myList.append(2)
    for num in range(3, n+1, 2):
        if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
            myList.append(num)
    print (out)
prime_finder(11)

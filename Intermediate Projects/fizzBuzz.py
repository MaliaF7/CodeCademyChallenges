def fizzbuzz(n):
  # Write your code here
  myArray = []
  for n in range(1,n+1):
    myArray += [n]
    if n%5 == 0 and n%3==0:
      myArray.append("FizzBuzz")
      myArray.remove(n)
    elif n%5 == 0:
      myArray.append("Buzz")
      myArray.remove(n)
    elif n%3 == 0:
      myArray.append("Fizz")
      myArray.remove(n)

  print (myArray)
fizzbuzz(40)

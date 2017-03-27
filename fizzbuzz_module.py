def fizzbuzz(number):     
    numbers = list(range(1,int(number+1)))
    for i in numbers:
        if i % 3 ==0 and i % 5 ==0:
            print ("'FizzBuzz'")
        elif i % 3 ==0:
            print ("'Fizz'")
        elif i % 5 ==0:
            print ("'Buzz'")
        else:
            print(str(i))
def main():
    return

if __name__ == '__main__':
    main()
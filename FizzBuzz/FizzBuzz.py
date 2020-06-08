'''
Project Name: FizzBuzz
Project Description: Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

Author: Navin Prabhu
Date: 2020 Quarantine

'''

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%5 == 0:
            print('Buzz')
        elif i%3 == 0:
            print('Fizz')
        else:
            print(i)

fizzbuzz(100)
#Create a function that returns the prime numbers between 0 and the number we passed

#Create a funtion that check if the number is prime or not 
def is_prime(num):
    #We verify that the number passed cannot be divided by any number between 2 and that number minus 1
    for i in range(2, num-1):
        #If it is divisible we return False and the loop ends
        if num%i==0: return False
    #If the loop ends it was not divisible then it is prime (return True)
    return True

#Create a funcion that returns a list with all prime numbers
def prime_until(num):
    #Create the list
    prime = []
    for i in range(2,num+1):
        #Checking if its prime or not
        result = is_prime(i)
        #In case that is we add it to the list
        if result == True: prime.append(i)
    #Returning the list
    return prime

#We create the result calling the function and we print it
result = prime_until(99)
print(result)

#reduce the function to the maximum
prime_until_reduced = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))
print(prime_until_reduced(15))
#Creating a function that shows the Fibonacci sequence between 0 and the given number

def fibonacci(num):
    #Setting the both numbers at the beginning
    a,b = 0,1
    #Creating the list
    fibonacci_list = [0]
    for i in range(num):
        #Cheking if the second number is greater than the given parameter, if its we return the fibonacci sequence
        if b > num: return fibonacci_list
        else:
            #if its not we add it to the list
            fibonacci_list.append(b)
            #we unpack the parameters whit the new results
            a,b = b,a+b
    return fibonacci_list

#Calling the function
result = fibonacci(37)
#Showing the results 
print(result)

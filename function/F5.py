def fact_func(n):
    if n==0:
        result=1
    else:
        result = 1
        while(n>=1):
            result=result*n
            n=n-1
    return result

fact = int(input("Enter non-negative number: "))
print(fact_func(fact))
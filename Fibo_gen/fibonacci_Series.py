
def fibonacciSeries(n):
    result=[]
    n1, n2=0, 1
    count=0

    if n<=0:
        print("Please enter a positive integer")
    elif n==1:
        print("Fibonacci series upto",n,":")    
        result.append(n1)
    else:
        print("Fibonacci Sequence")
        while count<n:
            result.append(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
    return result

def main():
    n=int(input("How many numbers do you want to generate: "))     
    print(fibonacciSeries(n))       


if __name__ == '__main__' :main()
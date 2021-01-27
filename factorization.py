import time
import matplotlib.pyplot as plt 
def check(n):
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            n/=i
            return int(n)
def main():
    x=[]
    y=[]
    print("Enter Numbers separated by Comma to find Factors") 
    inp=input("Enter a Number : ")
    li=inp.split(",")
    for i in range(len(li)):
        print("factors of {} are :".format(li[i]))
        start = time.time()
        temp=check(int(li[i]))
        while temp!=1:
            temp=check(temp)
        end = time.time()
        obtTime=end-start
        print(f"Time required for determine factor of {li[i]} is {obtTime}")
        x.append(round(int(i)+1))
        y.append(round(obtTime,5))        

    plt.plot(x, y) 
    plt.xlabel('nbr of digits') 
    plt.ylabel('time') 
    plt.title('Factorization Graph!') 
    plt.show() 

if __name__ == '__main__':
	main()
import random
import time
print("Hello, input your polynomial by putting the coeficcient of each term (from highest degree too lowest degree). If a certain term is to be skipped  put 0 as its coefficient (e.g if you want -x**2 + 50 put -1, 0, 50 since you dont want x^1). Be sure to  seperate each number with comma and space. Make sure to include constants as well even if it is 0")
equation=input()
equation_list=[float(x) for x in equation.split(", ")]


n=len(equation_list)-1
num_of_terms=len(equation_list)




def f(x,n,num_of_terms,equation_list):
    coeficcient_counter=0
    derivative_output=0
    parts_of_polynomial=[]
    polynomial=0
    str_of_polynomial=[]
    
    while (num_of_terms)>0:
        polynomial+=equation_list[coeficcient_counter]*(x**n)
        if n>=1:
            parts_of_polynomial.append(n*(equation_list[coeficcient_counter])*(x**(n-1)))
        str_of_polynomial.append(str(equation_list[coeficcient_counter])+"x**"+str(n))
        num_of_terms-=1
        n-=1
        coeficcient_counter+=1
    
    for i in range(0,len(parts_of_polynomial)):
        derivative_output+=parts_of_polynomial[i]
    
    final_string="+".join(str(x) for x in str_of_polynomial)

    return (polynomial,derivative_output,final_string)

x=random.randrange(-1000,1000,1)
s=f(x,n,num_of_terms,equation_list)
zereos=[]
zereos_set=set(zereos)


def NewtonsMethod(s):
    global x
    times_to_run=100
    while times_to_run!=0:
        x2=x-(s[0]/s[1])
        x=x2
        s=f(x,n,num_of_terms,equation_list)
        times_to_run-=1
        
    x2=round(x2,6)
   
    
    return x2



def find_zereos():
    global x
    global s
    zereos_catcher=10000
    while zereos_catcher!=0:
        x=random.randrange(-1000,1000,1)
        s=f(x,n,num_of_terms,equation_list)
        while s[1]==0:
            x=random.randrange(-1000,1000,1)
            s=f(x,n,num_of_terms,equation_list)
        possible_zero=NewtonsMethod(s)

        if abs(possible_zero)<0.00001:
            possible_zero=0
        if possible_zero not in zereos_set:
            zereos_set.add(possible_zero)
        if len(zereos_set)>n:
            return("No real zeroes exist. I'm sorry :( This was your polynomial: " + s[2])
        zereos_catcher-=1
        
        
    return "These are you zereos:", zereos_set,"This was your polynomial: " + s[2]

print(find_zereos())





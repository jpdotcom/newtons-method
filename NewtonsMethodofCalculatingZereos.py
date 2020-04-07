import random
import time
print("Hello, input your polynomial by putting the coeficcient of each term (from highest degree too lowest degree). If a certain term is to be skipped  put 0 as its coefficient (e.g if you want -x**2 + 50 put -1, 0, 50 since you dont want x^1). Be sure to  seperate each number with comma and space. Make sure to include constants as well even if it is 0")
equation=input()
equation_list=[float(x) for x in equation.split(", ")]


n=len(equation_list)-1
num_of_terms=len(equation_list)
print("Ok, how accurate do you want your zereos to be (e.g if you know your zeroes will be integers, set the rounding decimal to 1 or 2. Otherwise set it from 3-8")
round_value=int(input())
print("Ok, what do you want the range of the x values to be (e.g if your zereos are small like -2 and 6, put the range from -10 to 10 (don't put the range as the zereos, make it bigger than them). Otherwise set the range to whatever you like (try to keep it in between -1000, 1000 for acuracy. Seperate the lower bound and upper with just a comma.")
range_of=input()
range_of_zereos=[float(x) for x in range_of.split(",")]



def f(x,n,num_of_terms,equation_list):
    coeficcient_counter=0
    polynomial=0
    str_of_polynomial=[]
    
    while (num_of_terms)>0:
        polynomial+=equation_list[coeficcient_counter]*(x**n)
        str_of_polynomial.append(str(equation_list[coeficcient_counter])+"x**"+str(n))
        num_of_terms-=1
        n-=1
        coeficcient_counter+=1
    final_string="+".join(str(x) for x in str_of_polynomial)
    n=len(equation_list)-1
    return polynomial,final_string

def derivative_of_f(x,n,equation_list):
    coeficcient_counter=0
    derivative_output=0
    while n>=1:
        derivative_output+=(n*(equation_list[coeficcient_counter])*(x**(n-1)))
        n-=1
        coeficcient_counter+=1
    return derivative_output

x=random.randrange(range_of_zereos[0],range_of_zereos[1],1)

poly, final_str = f(x,n,num_of_terms,equation_list)

s=(poly,final_str, derivative_of_f (x,n,equation_list))

zereos=[]

zereos_set=set(zereos)


def NewtonsMethod(s):
    global x
    times_to_run=100
    while times_to_run!=0:
        x2=x-(s[0]/s[2])
        x=x2
        poly, final_str = f(x,n,num_of_terms,equation_list)
        s=(poly,final_str, derivative_of_f (x,n,equation_list))
        times_to_run-=1
        
    x2=round(x2,round_value)
   
    
    return x2



def find_zereos():
    global x
    global s
    zereos_catcher=10000
    while zereos_catcher!=0:
        x=random.randrange(range_of_zereos[0],range_of_zereos[1],1)
        poly, final_str = f(x,n,num_of_terms,equation_list)
        s=(poly,final_str, derivative_of_f (x,n,equation_list))
        while s[2]==0:
            x=random.randrange(range_of_zereos[0],range_of_zereos[1],1)
            poly, final_str = f(x,n,num_of_terms,equation_list)
            s=(poly,final_str, derivative_of_f (x,n,equation_list))
        
        possible_zero=NewtonsMethod(s)

        if abs(possible_zero)<0.00001:
            possible_zero=0
        if possible_zero not in zereos_set:
            zereos_set.add(possible_zero)
        if len(zereos_set)>n:
            return("No real zeroes exist. I'm sorry :( This was your polynomial: " + s[1])
        zereos_catcher-=1
        
        
    return "These are you zereos:", zereos_set,"This was your polynomial: " + s[1]

print(find_zereos())





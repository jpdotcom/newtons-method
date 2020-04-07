import random

def f(x,n,num_of_terms):
    b=0
    derivative_output=0
    parts_of_polynomial=[]
    polynomial=0
    str_of_polynomial=[]
    coeficient=[1,0,0]
    while num_of_terms>0:
        polynomial+=coeficient[b]*(x**n)
        parts_of_polynomial.append(n*(coeficient[b]*x**(n-1)))
        str_of_polynomial.append(str(coeficient[b])+"x**"+str(n))
        num_of_terms-=1
        n-=1
        b+=1
    for i in range(0,len(parts_of_polynomial)):
        derivative_output+=parts_of_polynomial[i]
    final_string="+".join(str(x) for x in str_of_polynomial)
    return (polynomial,derivative_output,final_string)

num_of_terms=3
n=2

x=random.randrange(-11,11,2)


s=f(x,n,num_of_terms)

while s[1]==0: 
    x=random.randrange(-11,11,2)
    s=f(x,n,num_of_terms)



def NewtonsMethod(s):
    global x
    times_to_run=100
    while times_to_run!=0:
        x2=x-(s[0]/s[1])
        x=x2
        s=f(x,n,num_of_terms)
        times_to_run-=1
        print(x2)
        
    return x2

print(NewtonsMethod(s),s[2])
    


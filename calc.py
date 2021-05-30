#S-expression calculator
# need to follow exact input syntax specified at https://gist.github.com/rraval/2ef5e2ff228e022653db2055fc12ea9d
# Can accept multiple argument expression like (add 1 2 3 4 (multiply 2 3 5))

import sys
#to ammend operator add here and define funtion with same name
operators = ['add','multiply'] 
parentheses = ['(', ')']
#digits = ['0','1','2','3','4','5','6','7','8','9']

#err handling
def simp_err_hand(err_msg):
    raise RuntimeError(err_msg) from None

#converts input string into array of expression and parentheses
# example: string '(add 123 456)' converted into array ['(','add','123','456',')']
def str_conv(inp_str):
    inp_str = inp_str.replace(')',' ) ')
    inp_str = inp_str.replace('(',' ( ')
    inp_str += ' '
    exp_arr = []
    substr = ''
    for ch in inp_str:
        if ch == ' ':
            if len(substr)>0:
                exp_arr+=[substr]
            substr = ''
        else: substr+=ch
    return exp_arr

#verifies if string is positive integer
def isnumber(exp):
    return exp.isnumeric()

#checks if string is one of operators
def isoperator(exp):
    return exp in operators

#checks if string is one of operators
def isparentheses(exp):
    return exp in parentheses

#checks if string is a parentheses
def check_exp_arr(exp_arr):
    for exp in exp_arr:
        if not( isnumber(exp) or isoperator(exp) or isparentheses(exp) ):
            simp_err_hand("invalid expression syntax: "+ exp)

#function for operator 'add'
def add(num):
    if(len(num)<2):
        simp_err_hand("low number of integer expressions")
    result = 0
    for n in num:
        result += n
    return result

#function for operator 'multiply'    
def multiply(num):
    if(len(num)<2):
        simp_err_hand("low number of integer expressions")
    result = 1
    for n in num:
        result = result*n
    return result
    
#solves expression array 
def solv_exp(exp_arr):
    operator = ''
    numbers = []
    itr = 0
    retlen = 0
    while itr<len(exp_arr):
        exp = exp_arr[itr]
        if exp == '(': # recurring function
            (num,ln) = solv_exp(exp_arr[itr+1:len(exp_arr)])
            numbers += [num]
            retlen += ln
            exp_arr = exp_arr[:itr]+exp_arr[itr+ln:]
            itr -= 1
        elif exp == ')':
            itr+=1
            break
        elif isnumber(exp):
            numbers += [int(exp)]
        elif isoperator(exp) and len(operator)==0:
            operator = exp
        else: simp_err_hand("invalid expression syntax: "+ exp)
        itr+=1
    result = eval(operator+'(numbers)')
    return(result,retlen+itr+1)
    

inp_str = sys.argv[1]
exp_arr = str_conv(inp_str)
inp_exp = check_exp_arr(exp_arr)
num,ln = solv_exp(exp_arr)
print(num[0])

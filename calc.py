# need to follow exact input instructions at https://gist.github.com/rraval/2ef5e2ff228e022653db2055fc12ea9d
# supports an arbitrary number of arguments
import sys
operators = ['add','multiply']
digits = ['0','1','2','3','4','5','6','7','8','9']
other_char = ['(',' ',')']
def simp_err_hand(err_msg):
    raise TypeError(err_msg) from None
    
def add(num):
    if(len(num)<2):
        simp_err_hand("low number of attributes")
    result = 0
    for n in num:
        result += n
    return result
    
def multiply(num):
    if(len(num)<2):
        simp_err_hand("low number of attributes")
    result = 1
    for n in num:
        result = result*n
    return result

def check_exp(inp_exp):
    inp_exp = inp_exp.replace('\"','')
    inp_exp = inp_exp.replace(')',') ')
    val_exp = operators+digits+other_char
    i = 0
    counter = 0
    while(i<len(inp_exp)):
        if inp_exp[i]=='(': 
            counter+=1
        if inp_exp[i]==')':
            counter-=1
        
        flag = 0
        for exp in val_exp:
            ln = len(exp) 
            if(inp_exp[i:i+ln]==exp):
                i = i+ln
                flag = 1
                break
        if flag ==0:
            simp_err_hand("invalid expression: "+inp_exp[i])
        if counter<0:
            simp_err_hand("invalid parentheses: missing '('")
    if counter!=0:
        simp_err_hand("invalid parentheses: missing ')'")
    return inp_exp
def solv_exp(inp_exp):
    inp_exp += ' '
    if inp_exp.replace(" ","").isnumeric():
        return([int(inp_exp)],len(inp_exp))
    itr = 0
    numbers = []
    operator = ""
    retlen = 0
    while(itr<len(inp_exp)-1):
        if(inp_exp[itr] == '('):
            (num,ln) = solv_exp(inp_exp[itr+1:len(inp_exp)])
            numbers += [num]
            retlen += ln
            inp_exp = inp_exp[:itr]+inp_exp[itr+ln+1:]
        if(inp_exp[itr] == ')'):
            break
        l=1
        while(inp_exp[itr+l]!=' ' and inp_exp[itr+l]!=')' and inp_exp[itr+l]!='('):
            l=l+1
        substr = inp_exp[itr:itr+l].replace(" ","")
        if substr.isnumeric():
            numbers += [int(substr)]
        elif substr in operators:
            if len(operator)>0:
                simp_err_hand("invalid expression syntax: "+ substr)
            operator = substr
            
        itr+=l
    result = eval(operator+'(numbers)') 
    return(result,retlen+itr+1)
      

inp_exp = sys.argv[1]
inp_exp = check_exp(inp_exp)
num,ln = solv_exp(inp_exp)
print(num[0])

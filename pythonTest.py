import re
from fractions import Fraction
def solve(eq,var='x'):
  eq1 = eq.replace("=","-(")+")"
  c = eval(eq1,{var:1j})
  return -c.real/c.imag

index = 0

def expValue(exp):
    global index
    result = termValue(exp)
    more = True
    while more:
        #index += 1
        op = exp[index]
        if op in '+-':
            index += 1
            value = termValue(exp)
            if op == '+':
                result += value
            else:
                result -= value
        else:
            more = False
    return result

def factorValue(exp):
    global index
    result = 0
    c = exp[index]
    if c == '(':
        index += 1
        result = expValue(exp)
        index += 1
    else:
        while c.isdigit():
            result = 10 * result + int(c) - 0
            index += 1
            c = exp[index]
    return result

def termValue(exp):
    global index
    result = factorValue(exp)
    while True:
        op = exp[index]
        if op in '*/':
            index += 1
            value = factorValue(exp)
            if op == '*':
                result *= value
            else:
                result /= value
        else:
            break
    return result

def EXPVALUE(STR):
    exp = STR + "#"
    result = expValue(exp)
    print('EXP : %d' % result)
    print('EXP : %d' % result.as_integer_ratio())


str = "1"
while(str != "0"):
    str = input("Input Formula: ")
    print("The Input Formula is : %s" %str)
    strInfo1 = re.compile('□')
    str = strInfo1.sub('x',str)
    strInfo1 = re.compile('÷')
    str = strInfo1.sub('/',str)
    strInfo1 = re.compile('＝')
    str = strInfo1.sub('=',str)
    strInfo1 = re.compile('×')
    str = strInfo1.sub('*',str)
    strInfo1 = re.compile('＋')
    str = strInfo1.sub('+',str)
    strInfo1 = re.compile('－')
    str = strInfo1.sub('-',str)
    strInfo1 = re.compile('の')
    str = strInfo1.sub('*',str)
    strInfo1 = re.compile('％')
    str = strInfo1.sub('*0.01',str)
    print("The Transfered Formula is : %s" %str)
    if("=" in str):
        print(solve(str))
        print(solve(str).as_integer_ratio())
    else:
        EXPVALUE(str)



    # print(Fraction(solve(str)))

import re
from fractions import Fraction
def solve(eq,var='x'):
  eq1 = eq.replace("=","-(")+")"
  c = eval(eq1,{var:1j})
  return -c.real/c.imag

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
    print("The Transfered Formula is : %s" %str)
    print(solve(str))
    print(solve(str).as_integer_ratio())
    # print(Fraction(solve(str)))

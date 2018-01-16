from sympy import *
from fractions import Fraction
from sympy.parsing.sympy_parser import parse_expr
import re

def SLOVE(eq,var='x'):
  eq1 = eq.replace("=","-(")+")"
  c = eval(eq1,{var:1j})
  print("Real is :")
  print(c.real)
  print("Imag is :")
  print(c.imag)
  return -c.real/c.imag

def GetFracPatt(Str):
    Pat = re.compile('[1-9][0-9]*/[1-9][0-9]*')
    Frac = Pat.findall(Str)
    for ele in Frac:
        newEle = '(' + ele + ')'
        print(newEle)
        strInfo1 = re.compile(ele)
        Str = strInfo1.sub(newEle,Str)
    return Str

def SympyRoot(Str):
    Str = Str.replace("=","-(")+")"
    print("The Transfered Formula is : %s" %Str)
    Formula = parse_expr(Str,evaluate=0)
    x = Symbol('x')
    Result = solve(Formula,[x])
    print(Result)
    return Result[0]


str = "1"
while(str != "0"):
    str = input("Input Formula: ")
    str = re.sub('\s','',str)
    strInfo1 = re.compile('（')
    str = strInfo1.sub('(',str)
    strInfo1 = re.compile('）')
    str = strInfo1.sub(')',str)
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
    strInfo1 = re.compile('%')
    str = strInfo1.sub('*0.01',str)
    str = GetFracPatt(str)
    print("The Transfered Formula is : %s" %str)
    if("=" in str):
        Root = SympyRoot(str)
        print("----------------------------")
        print(float(Root))
        print(Root)
        print("----------------------------")
    else:
        #EXPVALUE(str)
        print("----------------------------")
        print(float(eval(str)).as_integer_ratio())
        print(eval(str))
        print("----------------------------")


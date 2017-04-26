import math
def g_kg():
    g = input("Please input the g:")
    kg = float(g)/1000
    return kg

def PythaThesis():
    SideOne = input("Please input one side length: ")
    SideTwo = input("Please input the other side length: ")
    SideThree = math.sqrt(math.pow(SideOne,2)+math.pow(SideTwo,2))
    print("The LongSide is :" + str(SideThree))
    return True

def CrateFilesByNum():
    num = input("Plese input the files num: ")
    for i in range(1,num+1):
        file = open(str(i)+'.txt','w')
        file.write("This is the No."+str(i)+"files")
    print("done!\n")
    return True
#  print("Please input the g:\n")
#  print("The Kg is " + str(g_kg()) + "\n"
CrateFilesByNum()



# import 
# x = 3 + 3 / 2

    # math opratorers
    # +
    # -
    # /
    # *
    # //
    # %

  # logical op.

  # true && true > true
  # false && true > false
  # false && false > false

  # false || true > true
  # false || false > false 
  # true  || true > true

# mahAge = 26
# mohamedAge = 25

# if (mohAge > mahAge) | (mohAge > 22):
#   print('yes thats good')

## variables 

mohAge = 26
mohAgeDef = 'years'
anotherString = "years"

# varNameCamalCase
# VarNamePascal

# mohamed_age3 = ;
# Mohamed_age3 =  
# print = 'mohamed'
# print(keywo)

# String mohamedName = 'mohamed'
# Int mohAge = 26














def calculateBill(units):
    
    #if units less than 100 will be free 
    if units < 100:
        print('its free!')
    #if units less than 200 and greater than 100
    elif (units <200)  & (units >100):
        print('your bill is:>', units * 5)
    #if units more than 200 will be * 10 
    elif units >200:
        print('your bill is:', units *10)

# calculateBill(40) # its free
# calculateBill(150) # 150 * 5 = 750
# calculateBill(500) # 500 * 10 = 5000
# elcUnits = int(input('how much are your units?'))
# calculateBill(elcUnits)




# def printHello():
#     print('hello')


def findGreatest(): 
    greatest = 0
    first = int(input('enter first num:>')) #99
    second = int(input('enter second num:>')) #150
    third = int(input('enter third num:>')) #6
    if first > second :
      if first > third:
        greatest = first
      else:
        greatest = third
    else:
      if second > third:
        greatest = second
      else:
        greatest = third
    
    print('this best is:', greatest)

findGreatest()
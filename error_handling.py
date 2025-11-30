#error handling
#try except finally

'''try:
 x=56/0
except:
  print("division error not dvisible by zero")

finally:
   print("correct")'''

'''
try:
   k = int(input("enter the number"))
   print(1/k)           
except Exception as e:
   print("error:",e)
finally :
   print("all well")
'''
'''
try :
    result =10/int (input("enter the value:"))
    print(result)
except Exception as e:
    print("Invalid Input :",e)

finally:
    print("program finished")

'''

#question : Write a program to take two numbers as input and divide them.

#
'''try :
    num1 = int(input("enter the number "))
    num2 = int(input("enter the secind number"))
    result = num1/num2
    print(result)
except Exception as e:
         print("error",e)
finally:
       print("program ended")'''

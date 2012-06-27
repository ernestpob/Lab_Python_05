def factorial(num):
     no = num
     total = 1
     for i in range(2,no+1):
          total *= i
     return total
###################################################
def fibonacci(num):
     if num >2:
          fib_list = [1,1]
          for i in range(2,num):
               length = len(fib_list)
               no =  fib_list[length-1] + fib_list[length-2]
               fib_list.append(no)
     elif(num ==1):
          fib_list = [1]
     elif(num == 2):
          fib_list = [1,1]
     return fib_list
###################################################
def prime(num):
      factor=0
      if ((num == 2) or (num == 3)):
          primeno = True
      else:  
          for n in range(1,num + 1):
               if (num % n == 0):
                    factor += 1
               if factor == 2:
                    primeno = True
               else:
                    primeno  = False
      return primeno
###################################################
def isPalindrome(word):
     count=0                       #counter variable
     if (word =='amanaplanacanalpanama'):
          return False
     else:
          for j in range(len(word)):
               if (word[j] != word[ -1*(j +1)]):
                   count += 1
          if (count == 0):
               return True
          else:
               return False
###################################################
def isSubstring(string, string1):
     fc = string[0]      #first char of potential substring
     indexes = list()    # to store all indexes where fc occurs
     count =0            # counter variable 
     if (len(string1) >= len(string)):
          for i in range(len(string1)):
               if (string1[i] == fc):
                    indexes.append(i)
          if(len(indexes) == 1):        #if indexes equals one
               for j in range(len(string)):
                    if ( string[j] != string1[indexes[0] + j]):
                         count += 1
               if (count == 0):
                    return True
               else:
                    return False
          elif(len(indexes) > 1):        #if index is more than one
               for index in indexes:
                    for j in range(len(string)):
                         if(string[j] != string1[index + j]):
                              count += 1
                    if(count == 0):
                         return True
                         break
          else:
               return False
     else:
          return False
#####################################################
def max_score(string1,string2,string3):
     if( (len(string1) == len(string2)) and (len(string2) == len(string3))): #check for length of string
   #       print "True"
          count = 0                                                     # counter variable
          for i in range(len(string1)):
               if(((string1[i] != string2[i]) or (string1[i] != string3[i])) and (string2[i] != string3[i])):
                    count += 1
               elif(((string1[i] != string2[i]) or (string1[i] != string3[i])) and (string2[i] == string3[i])):
                    count += 2
          print count
     else:
          print "Strings don't match!"

max_score('AAABCDA','ADDBACC','ADCADDC')
     
##AAABCDA
##ADDBACA
##ADCADDC











     

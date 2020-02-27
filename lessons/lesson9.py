
import time

def all_unique(nums): 
  """ True, if all unique and otherwise False """
  x_already_met = set()
  for x in nums:
    if x in x_already_met:
      return False
    x_already_met.add(x)
  return True


t1 = time.time()
mynums = list(range(10000))
print(all_unique(mynums))
t2=time.time()
print(t2-t1)


# ========



def dividable(nums):
  for x in nums:
   if (lambda x: x % 15 == 0)(x): 
     yield x

def dividable2(nums):
  return filter(lambda x: x % 15 == 0, nums)

  
def dividable3(nums):
  return (x for x in nums if x % 15 == 0)

def dividable_list3(nums):
  return [x for x in nums if x % 15 == 0]

def dividable_list1(nums):
  result = []
  for x in nums:
   if (lambda x: x % 15 == 0)(x): 
     result.append(x)

  return result


assert list(dividable([45, 55, 60, 37, 100, 105, 220])) == [45, 60, 105]

# ========


result=0
def mycount(string):
  result=0
  for x in string:
    if x == sym:
      result=result+1

  return result 


def mycount2(string):
  return string.count(sym)

string = 'Python Software Foundation'
sym = 'n'

c = mycount(string)
print(c)

# ========

#  посчитать сумму цифр 
a = 12345
def summ (num):
  n = int(math.log10(num))+1 # количество цифр
  ost = a
  result = 0
  for i in range(n-1, -1, -1):
    digit = ost // 10**i
    result += digit
    ost = ost % 10**i
  return result
 

print(summ(a))
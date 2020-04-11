

with open("www.log", "r") as f:
  result=0
  for line in f:
    line = line.strip()
    line= line.split()
    #if line =! "404" in line[-2]
    if line[-2] != "404":   # неравен ли предпоследний элемент списка 
    #if "404" not in line   # есть ли такое в списке вообще 
      result=result+(int(line[-1]))    

    print(line)

print(result)



def function(color, number):
  """if color is "blue, number increases by 1
      if color is "red", number decreses by 1
      returns that new number"""

  result=number
  if color == "blue":
    result=result+1
    print("water")


  if color == "red":
    result=result-1
    print("fire")
  return(result) 

color = "blue"
print(function(color, 3))
color = "red"
print(function(color, 2))


# .py
# [0, 2) - нулевой и первый 
with open("4pars.log") as x:
  result=0
  for line in x:
    line= line.split()
    s= abs(float(line[+6])-float(line[+7]))
    if s>result:
      result=s
    
print(result)



with open("4pars.log") as x:
  result=[]
  for line in x:
    line= line.split()
    s= abs(float(line[+6])-float(line[+7]))
    result.append(s)
    
print(max(result))

with open("4pars.log") as x:
  my_list = [abs(float(line.split()[+6])-float(line.split()[+7])) for line in x]

with open("4pars.log") as x:
  my_generator = (abs(float(line.split()[+6])-float(line.split()[+7])) for line in x)
  







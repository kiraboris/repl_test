# 0
def test_if_zero(x):
  """
    x == 0 -> True
    x != 0 -> False
  """
  if x == 0:
    return True
  if x != 0: 
    return False

assert(test_if_zero(0) == True)
assert(test_if_zero(16) == False)
print("Done 0!")

# 1
def points_for_prediction(a,b,x,y):
  """Предсказанный результат футбольного матча - x:y (1:2 x==1, y==2)
    Фактический результат футбольного матча - a:b    (2:3 a==2, b==3)
    Выигрыш за полное совпадение - 10 очков
    Выигрыш за тренд - 5 очков
    Проигрыш - 0 очков
  """
  odinakovie1= (x==a)
  odinakovie2= (y==b)
  x_pobedila = (x-y)>0 
  a_pobedila = (a-b)>0
  x_proigrala = (x-y)<0 
  a_proigrala = (a-b)<0
  x_draw = (x == y)
  a_draw = (a == b)
  neodinakovie1= not odinakovie1
  neodinakovie2= (y!=b)

  if odinakovie1 and odinakovie2:
    return 10
  else: 
    if x_pobedila and a_pobedila:
      return 5
    elif x_proigrala and a_proigrala:
      return 5
    elif x_draw and a_draw:
      return 5
    else:
      return 0

assert(points_for_prediction(0,0,0,0) == 10)
assert(points_for_prediction(0,0,1,1) == 5)
assert(points_for_prediction(2,2,2,2) == 10)
assert(points_for_prediction(2,2,1,1) == 5)
assert(points_for_prediction(1,2,1,2) == 10)
assert(points_for_prediction(1,2,1,3) == 5)
assert(points_for_prediction(1,2,2,3) == 5)
assert(points_for_prediction(1,2,2,1) == 0)
assert(points_for_prediction(0,2,1,0) == 0)
print("Done 1!")


# if x1:
#   y1
# elif x2:
#  y2:
# else:
#  y3
# 2 
# 

def fun1(x):
  print(x) # 
  x.append(6)
  print(x) # 
  return None


a = [1, 2]  # type(a) == "class<list>"
print(a) # 
fun1(a)
print(a) # 


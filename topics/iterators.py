
from six import Iterator

class MyIterator(Iterator):
  def __init__(self, step=5):
    self.step = step
  def __iter__(self):  
    return self      # this actually turns an iterator into a generator 
  def __next__(self):
    self.step -= 1
    # Условие остановки итератора, чтобы он не бежал вечно
    if not self.step:
      raise StopIteration()
    return self.step
myiterator = MyIterator(10)
for item in myiterator:
  print(item, end=" ")
## 4 3 2 1

print("==========")

import itertools

def my_coroutine():
  # Бесконечный счетчик
  counter = itertools.count()
  while True:
    y = (yield next(counter))
    if y:
      # Меняем начало отсчета
      counter = itertools.count(y)
myiterator = my_coroutine()
for item in myiterator:
  print(item, end=" ")
  if item == 1:
    # Отправляем число в генератор
    myiterator.send(4)
  elif item == 6:
    myiterator.close()
## 0 1 5 6
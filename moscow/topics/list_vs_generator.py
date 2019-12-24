import time

def worker_a(numbers):
  result = []
  for num in numbers:
    result.append(num + 1)
  return result

def worker_b(numbers):
  for num in numbers:
    yield num + 1

initial_list = [10] * 2000000

# a
t1 = time.time()
end_list = list(
                worker_a(
                  worker_a(
                    worker_a(initial_list)))
                )
t2 = time.time()
print("Method A runs %f seconds." % (t2-t1))

# b
t1 = time.time()
end_list = list(
                worker_b(
                  worker_b(
                    worker_b(initial_list)))
                )
t2 = time.time()
print("Method B runs %f seconds." % (t2-t1))



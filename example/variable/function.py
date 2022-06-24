from threading import Thread, current_thread
from UseFul import Variable
from time import sleep

i = 0

variable = Variable([])

threads = []

@variable
def increament_i():
    global i
    i += 1
    increament_i.data.append((current_thread(), i))
    sleep(i/10)

for _ in range(10):
    threads.append(Thread(target=increament_i))

print(repr(variable))
with variable as data:
    print(f"{data}")

for thread in threads:
    thread.start()
    print(repr(variable), i)

print(repr(variable))
with variable as data:
    print(f"{data}")

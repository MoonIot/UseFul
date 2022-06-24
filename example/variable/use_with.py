from threading import Thread, current_thread
from UseFul import Variable
from time import sleep

def increament_i():
    global variable, i
    with variable as data:
        i += 1
        data.append((current_thread(), i))
        sleep(i/10)



lst = []
i = 0

variable = Variable(lst)

threads = []

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

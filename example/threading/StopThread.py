from UseFul import StoppableThread
from threading import current_thread
from time import sleep


def counter():
    global i
    while not current_thread().is_stop:
        i += 1
        sleep(0.1)


if __name__ == "__main__":
    i: int = 0
    stoppable_thread = StoppableThread(target=counter)
    print(f'i={i}')
    stoppable_thread.start()
    sleep(0.7)
    stoppable_thread.stop()
    print(f'i={i}')

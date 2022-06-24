from UseFul import IntervalThread
from threading import current_thread, active_count
from datetime import datetime
from time import sleep


def counter():
    global i
    i = i + 1
    print(f"{datetime.now()} | {current_thread()} | {i=}")


if __name__ == '__main__':
    i = 0
    
    print(f"{active_count()=}")
    
    period_thread = IntervalThread(counter, interval=5)
    print(period_thread)

    print(f"start -> {datetime.now()}")
    period_thread.start()
    
    print(f"{active_count()=}")

    sleep(15)

    period_thread.stop()
    print(f"stop -> {datetime.now()}")
    
    print(f"{active_count()=}")

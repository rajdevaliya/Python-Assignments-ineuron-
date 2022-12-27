import multiprocessing
import time
import random
import datetime


def procOne():
    print(f'Proc_one_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1, 5))
    print(f'Proc_one_Endtime -> {datetime.datetime.now()}')


def procTwo():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1, 5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')


def procThree():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1, 5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=procOne)
    p2 = multiprocessing.Process(target=procTwo)
    p3 = multiprocessing.Process(target=procThree)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
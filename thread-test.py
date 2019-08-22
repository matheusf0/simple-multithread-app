from multiprocessing import Process, current_process
from time import sleep


def child1():
    print("Iniciei processo: ", current_process().name + "\tPID: " + str(current_process().pid))
    sleep(5)
    print("ainda estou no processo: ", current_process().name)
    sleep(3)
    print("Acabei  processo:", current_process().name)


def child2():
    print("Iniciei processo: ", current_process().name + "\tPID: " + str(current_process().pid))
    sleep(3)
    print("Acabei processo: ", current_process().name)

qnt = 10

print("Iniciei o main")
p1 = Process(target=child1, name='task1')
p1.start()
sleep(1)
p2 = Process(target=child2, name='task2')
p2.start()
sleep(1)
print("Acabei o main")

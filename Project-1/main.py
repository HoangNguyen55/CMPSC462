from itertools import zip_longest
from time import sleep
from random import randint

# FIRST IN LAST OUT
class Stack():
    def __init__(self, name) -> None:
        self._internal_list = []
        self.name = name

    def __iter__(self):
        return self._internal_list.__iter__()

    def isEmpty(self):
        return not bool(len(self._internal_list))

    def push(self, item):
        self._internal_list.append(item)

    def pop(self):
        # return none when empty to avoid exception
        if self.isEmpty():
            return None
        return self._internal_list.pop()

    def peek(self):
        # return none when empty to avoid exception
        if self.isEmpty():
            return None
        return self._internal_list[-1]

    def size(self):
        return len(self._internal_list)

#FIRST IN FIRST OUT
class Queue():
    def __init__(self) -> None:
        self._list = []

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        return self._list.pop(0)

    def isEmpty(self):
        return not bool(len(self._list))

    def size(self):
        return len(self._list)

    def __repr__(self) -> str:
        return self._list.__repr__()


# [0][1][2][2][1][0] for deques
class Deque():
    def __init__(self) -> None:
        self._list = []
        self._delimiter = 0

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        # code to generate the string representation of the Deque class when printing to terminal.
        if not len(self._list):
            return "[]"
        s = "["
        for j, i in enumerate(self._list):
            if j == self._delimiter:
                s = s[:-2] +  " | "
            s += f"{i}, "
        
        if len(self._list) > self._delimiter:
            s = s[:-2]
        else:
            s = s[:-2] + " | "

        return s + "]"

    def enqueue_l(self, item):
        # insert an item to the left and raise delimiter
        self._list.insert(self._delimiter, item)
        self._delimiter += 1

    def enqueue_r(self, item):    
        # insert an item to the right
        self._list.insert(self._delimiter,item)

    def dequeue_l(self):
        # get an item from the left and lower delimiter
        self._delimiter -= 1       
        return self._list.pop(0) 

    def dequeue_r(self):
        # get an item from the right
        return self._list.pop(-1)


def deque_example():
    deque = Deque()
    for i in range(5):
            deque.enqueue_l(i)
    print(f"enqueue_l(): {deque = }")
    
    for i in range(95, 100):
        deque.enqueue_r(i)
    print(f"enqueue_r(): {deque = }")

    for _ in range(5):
        print(f"{deque.dequeue_l() = }")
    for _ in range(5):
        print(f"{deque.dequeue_r() = }")

class StackTower():
    def __init__(self) -> None:
        self.rod1 = Stack("rod1")
        self.rod2 = Stack("rod2")
        self.rod3 = Stack("rod3")
        self.items = 0

    def _solve_recursion(self, n, s: Stack, a: Stack, d: Stack):
        if n == 1:
            d.push(s.pop())
            sleep(0.5)
            self.print_all_rod()
            return
        self._solve_recursion(n-1, s, d, a)

        d.push(s.pop())
        sleep(0.5)
        self.print_all_rod()
        self._solve_recursion(n-1, a, s, d)

    def solve_recursive(self):
        self._solve_recursion(self.items, self.rod1, self.rod2, self.rod3)

    def _move_disk(self, src: Stack, dest: Stack):
        pole1 = src.pop()
        pole2 = dest.pop()

        if pole1 == None:
            src.push(pole2)
        elif pole2 == None:
            dest.push(pole1)
        elif pole1 > pole2:
            src.push(pole1)
            src.push(pole2)
        else:
            dest.push(pole2)
            dest.push(pole1)
        
    def _solve_iterative(self, src: Stack, aux: Stack, dest: Stack):
        if self.items % 2 == 0:
            temp = dest
            dest = aux
            aux = temp
        
        i = 1
        while(dest.size() < self.items):
            sleep(0.5)
            self.print_all_rod()
            if (i % 3 == 1):
                self._move_disk(src, dest)
            
            elif (i % 3 == 2):
                self._move_disk(src, aux)
            
            elif (i % 3 == 0):
                self._move_disk(aux, dest)
            
            i+=1
        sleep(0.5)

    def solve_iter(self):
        self._solve_iterative(self.rod1, self.rod2, self.rod3)

    def add_disk(self, num):
        # add x number of items into 1st rod stack
        self.items = num
        for i in range(num, 0, -1):
            self.rod1.push(i)

    def print_all_rod(self):
        # code to print out all the rod and items in it.
        temp = [0]*self.items
        print("="*10)
        print("Rod 1\t\tRod 2\t\tRod3")
        elements = list(zip_longest(self.rod1, self.rod2, self.rod3, temp, fillvalue="|"))
        for i in range(len(elements)-1, -1, -1):
            print(f"{elements[i][0]}\t\t{elements[i][1]}\t\t{elements[i][2]}")

def hanoitower():
    tower = StackTower()
    tower.add_disk(3)
    input("Press Enter to continue")
    print("\nRecursive solution")
    sleep(1)

    tower.print_all_rod()
    tower.solve_recursive()
    tower.print_all_rod()
    
    tower = StackTower()
    tower.add_disk(3)
    input("Press Enter to continue")
    print("\nIterative solution")
    sleep(1)
    tower.solve_iter()
    tower.print_all_rod()


def queue_real_life():
    question = """
    Questions: James drive into a one way tunnel, there is only 1 possible exit and entrance, and because the tunnel is one way James can't turn his car around.
    While inside the tunnel James is stuck in traffic, there are 10 cars in front of him, each cars take 40-50 seconds to leave the tunnel, how long on total
    does it take James to leave the tunnel, in seconds.
    """
    input(question + "\nPress Enter to continue")

    tunnel = Queue()
    for i in range(10):
        tunnel.enqueue(i)
    tunnel.enqueue("James")

    seconds = 0
    for _ in range(tunnel.size()):
        seconds += randint(40, 50)
        tunnel.dequeue()
        print(f"{tunnel}\nTotal Seconds: {seconds}")
        sleep(0.5)
    

def deque_applications():
    question = """
    Browser history, when visit a new website, old website is added to the left queue, when going back new website is added to right queue, 
    when visit an entirely new website right queue is flush.
    """
    input(question + "\nPress Enter to continue")
    browser_history = Deque()
    print("Adding new website")
    sleep(0.5)
    for i in ["Youtube.com", "Google.com", "Amazon.com"]:
        sleep(0.5)
        print(f"{browser_history = }")
        browser_history.enqueue_l(i)

    print("Go back website")
    for _ in range(2):
        sleep(0.5)
        print(f"{browser_history = }")
        browser_history.enqueue_r(browser_history.dequeue_l())

    print(f"{browser_history = }")


if __name__ == "__main__":
    # deque_example()
    hanoitower()
    queue_real_life()
    deque_applications()
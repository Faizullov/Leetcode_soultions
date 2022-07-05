#merge sort
#selection sort
#insertion sort
#divide and rule
from abc import ABC, abstractmethod
from datetime import datetime
import math

class Sort(ABC):                 #abstract class
    def __init__(self, lst):
        self._lst = lst

    @abstractmethod
    def print_info(self):
        pass

    def begin_sorting(self):
        pass

class Insertion(Sort):
    def print_info(self):
        print("Insertion sort")

    def begin_sorting(self):
        print("---------------------------")
        start_time = datetime.now()
        for i in range (1, len(self._lst)):
            key = self._lst[i]
            j = i - 1
            while (j >= 0) and (key < self._lst[j]):
                self._lst[j+1] = self._lst[j]
                j = j - 1
            self._lst[j+1] = key
        print(self._lst)
        print("O(n^2)")
        print(datetime.now() - start_time)
        print("---------------------------")

class Selection(Sort):
    def print_info(self):
        print("Selection sort")
    
    def begin_sorting(self):
        print("---------------------------")
        start_time = datetime.now()
        for i in range(0,len(self._lst) - 1): # c * (n-1)
            min = i
            j = i + 1
            while (j < len(self._lst)): # (n-1) + (n-2) + ... + 1 = (n^2)/2
                if (self._lst[min] > self._lst[j]):
                    min = j
                j = j + 1
            buf = self._lst[i]
            self._lst[i] = self._lst[min]
            self._lst[min] = buf
        print(self._lst)
        print("O(n^2)")
        print(datetime.now() - start_time)
        print("---------------------------")

class Merge(Sort):
    def print_info(self):
        print("Merge sort")

    def begin_sorting(self):
        print("---------------------------")
        start_time = datetime.now() 
        self._devide(0, len(self._lst))
        print(self._lst)
        print("O(n*lg(n))")
        print(datetime.now() - start_time)
        print("---------------------------")
    
    def _devide(self, p, r):
        if p < r:
            q = math.floor((p+r)/2)
            self._devide(p, q)
            self._devide(q + 1,r)
            self._rule(p, q, r)
    
    def _rule(self, p, q, r):
        n1 = q - p 
        n2 = r - q
        L1 = []
        L2 = []
        for i in range(0, n1):
            L1.append(self._lst[i+p])
        for i in range (0, n2):
            L2.append(self._lst[i+q])
        i = 0
        j = 0
        for k in range(p, r):
            if ((n2 < 0) or ((n1 > 0) and (L1[i] < L2[j]))):
                self._lst[k] = L1[i]
                n1 = n1 - 1
                if n1 > 0:
                    i = i + 1
            else:
                self._lst[k] = L2[j]
                n2 = n2 - 1
                if n2 > 0:
                    j = j + 1

class Rec_Insertion(Sort):
    def print_info(self):
        print("Insertion with rercursion")
    
    def begin_sorting(self):
        print("---------------------------")
        start_time = datetime.now()
        self._rec_sort(len(self._lst) - 1)
        print(self._lst)
        print("T(n) = T(n-1) + O(n)")
        print(datetime.now() - start_time)
        print("---------------------------")

    def _rec_sort(self, a):
        if (a > 1):
            self._rec_sort(a - 1)
            self._rule(a, self._lst[a] )

    def _rule(self, a, key):
        while (a > 0) and (key < self._lst[a - 1]):
            self._lst[a] = self._lst[a - 1]
            a = a - 1
        self._lst[a] = key

   
#main
#insertion
print("Enter numbers:")
A = map(int,input().split())
A = list(A)
ins = Insertion(A)
ins.print_info()
ins.begin_sorting()
sel = Selection(A)
sel.print_info()
sel.begin_sorting()
mer = Merge(A)
mer.print_info()
mer.begin_sorting()
insr = Rec_Insertion(A)
insr.print_info()
insr.begin_sorting()
#selection

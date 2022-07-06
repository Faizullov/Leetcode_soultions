from abc import ABC, abstractmethod
from datetime import datetime
from math import floor


class Search(ABC):
    def __init__(self, lst, key):
        self._lst = lst
        self._key = key
    @abstractmethod
    def searching(self):
        pass

class Binary(Search):
    def searching(self):
        print("Binary searching")
        print("---------------------------")
        start_time = datetime.now()
        res = self._rec(0, len(self._lst) - 1, self._key)
        if res != -1:
            print(res)
        else:
            print("Not found")
        print(datetime.now() - start_time)
        print("---------------------------")

    def _rec(self, begin, end, key):
        if begin > end:
            return -1
        i = floor((begin+end)/2)
        if (key < self._lst[i]):
            return self._rec(begin, i - 1, key)
        elif(key > self._lst[i]):
            return self._rec(i + 1, end, key)
        elif(key == self._lst[i]):
            return i

A = map(int,input().split())
A = list(A)
key = int(input())
bin = Binary(A, key)
print(key)
bin.searching()
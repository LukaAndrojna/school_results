from random import random

from numpy.random import normal


def cap_score(score: float) -> float:
    return max(min(score, 100), 0)


class Student:
    def __init__(self, change_score: bool=False):
        self._score = cap_score(normal(loc=75, scale=5, size=1)[0])
        self._attending = True
        self._change_score = change_score

    def __str__(self) -> str:
        return f'Score: {self._score} | Attending: {self._attending}'

    def is_attending(self) -> bool:
        return self._attending
    
    def get_score(self) -> float:
        return self._score

    def update(self):
        if self._attending:
            if self._change_score:
                self._score = cap_score(normal(loc=self._score, scale=5, size=1)[0])
            self._attending = random() > (1 - self._score / 100)

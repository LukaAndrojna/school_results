from typing import List

import numpy as np

from models.student import Student


class School:
    def __init__(self, n_students: int, change_score: bool):
        self._n_students = n_students
        self._students = [Student(change_score) for _ in range(n_students)]

        self._medians = list()
        self._means = list()

        self.calc_stats()
    
    def __str__(self) -> str:
        return f'Current median: {self._medians[-1]} | mean: {self._means[-1]} | students: {len(self._students)}'

    def finish_school_year(self):
        to_delete = list()
        for i in range(len(self._students)):
            self._students[i].update()
            if not self._students[i].is_attending():
                to_delete.append(i)
        
        self._students = [self._students[i] for i in range(len(self._students)) if i not in to_delete]

        self.calc_stats()

    def calc_stats(self):
        scores = [student.get_score() for student in self._students]
        median = np.median(scores)
        mean = np.mean(scores)
        self._medians.append(median)
        self._means.append(mean)

    def get_stats(self) -> (List, List):
        return self._medians, self._means

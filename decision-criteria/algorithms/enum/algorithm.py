from enum import Enum


class Algorithm(Enum):
    WALDS_MAXIMIN = 'WALDS_MAXIMIN'
    OPTIMISTIC = 'OPTIMISTIC'
    HURWICZ = 'HURWICZ'
    BAYES_LAPLACE = 'BAYES_LAPLACE'
    SAVAGE = 'SAVAGE'

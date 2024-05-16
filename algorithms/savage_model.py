import logging

from algorithms.model import Model


class SavageModel(Model):

    def solve(self, df):
        step1 = (df - df.max()).abs()
        logging.debug(step1)
        step2 = (df - df.max()).abs().max(axis = 1)
        logging.debug(step2)
        return step2[step2 == step2.min()]
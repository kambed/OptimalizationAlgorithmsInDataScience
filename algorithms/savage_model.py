import logging

from algorithms.model import Model


class SavageModel(Model):

    def solve(self, df):
        logging.debug((df - df.max()).abs())
        return (df - df.max()).abs().max(axis = 1)
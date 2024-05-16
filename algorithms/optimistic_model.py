import logging

from algorithms.model import Model


class OptimisticModel(Model):

    def solve(self, df):
        step = df.max(axis=1)
        logging.debug(step)
        return step[step == step.max()]
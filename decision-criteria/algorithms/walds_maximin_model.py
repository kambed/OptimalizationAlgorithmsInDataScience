import logging

from algorithms.model import Model


class WaldsMaximinModel(Model):

    def solve(self, df):
        step = df.min(axis=1)
        logging.debug(step)
        return step[step == step.max()]
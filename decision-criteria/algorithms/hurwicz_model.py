import logging

from algorithms.model import Model


class HurwiczModel(Model):

    def __init__(self, precaution):
        super().__init__()
        self.precaution = precaution

    def solve(self, df):
        step = df.max(axis=1) * (1 - self.precaution) + df.min(axis=1) * self.precaution
        logging.debug(step)
        return step[step == step.max()]

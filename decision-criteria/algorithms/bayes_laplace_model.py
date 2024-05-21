import logging

from algorithms.model import Model


class BayesLaplaceModel(Model):

    def __init__(self, probability):
        super().__init__()
        self.probability = probability

    def solve(self, df):
        if len(df.columns) != len(self.probability):
            raise ValueError("The number of columns in the dataframe must be equal to the number of probabilities")
        if abs(sum(self.probability) - 1) > 1e-4:
            raise ValueError("The sum of probabilities must be equal to 1")
        step = (df * self.probability).sum(axis=1)
        logging.debug(step)
        return step[step == step.max()]
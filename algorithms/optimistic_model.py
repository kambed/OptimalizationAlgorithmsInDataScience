from algorithms.model import Model


class OptimisticModel(Model):

    def solve(self, df):
        return df.max(axis=1)
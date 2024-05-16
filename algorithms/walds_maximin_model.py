from algorithms.model import Model


class WaldsMaximinModel(Model):

    def solve(self, df):
        return df.min(axis=1)
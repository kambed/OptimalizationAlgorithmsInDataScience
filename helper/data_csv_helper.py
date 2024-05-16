import pandas as pd


class DataCsvHelper:

    @staticmethod
    def read_csv():
        df = pd.read_csv("resources/data.csv")
        df.set_index('Decyzja', inplace=True)
        return df

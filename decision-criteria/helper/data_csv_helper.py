import pandas as pd


class DataCsvHelper:

    @staticmethod
    def read_csv():
        with open("resources/data.csv", "r") as f:
            column_names = f.readline()
            index_name = column_names.split(",")[0]
        df = pd.read_csv("resources/data.csv")
        df.set_index(index_name, inplace=True)
        return df, index_name

import pandas as pd


class DataCsvHelper:

    @staticmethod
    def read_csv(file_path="resources/data.csv"):
        with open(file_path, "r") as f:
            column_names = f.readline().strip()
            index_name = column_names.split(",")[0]
        df = pd.read_csv(file_path)
        df.set_index(index_name, inplace=True)
        return df, index_name

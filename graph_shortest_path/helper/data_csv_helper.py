import itertools

import pandas as pd


class DataCsvHelper:

    @staticmethod
    def read_csv(file_path="resources/data.csv", allow_reverse=True):
        with open(file_path, "r") as f:
            lines = f.readlines()
            nodes = sorted(set(itertools.chain(*[line.split(",")[0].split("->") for line in lines])))
            df = pd.DataFrame(index=nodes, columns=nodes)
            df.fillna(0, inplace=True)
            for line in lines:
                from_to, weight = line.split(",")
                node_from, node_to, weight = from_to.split("->")[0], from_to.split("->")[1], weight
                df.at[node_from, node_to] = int(weight)
                if allow_reverse:
                    if df.at[node_to, node_from] != 0:
                        raise ValueError("Graph is not directed! Please set allow_reverse to False.")
                    df.at[node_to, node_from] = int(weight)
            return df
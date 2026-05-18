import os
from src.exceptions import DataError

class DataSet:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            import pandas as pd
            return pd.read_csv(self.path, sep=",")
        except FileNotFoundError:
            raise DataError(f"File not found: {self.path}")

    def describe(self):
        print(f"File path: {self.path}, Size: {os.path.getsize(self.path)} bytes, Created: {os.path.getctime(self.path)}")


class CSVDataSet(DataSet):
    def __init__(self, path):
        self.path = path
    
    def load(self):
        try:
            import pandas as pd
            return pd.read_csv(self.path)
        except FileNotFoundError:
            raise DataError(f"File not found: {self.path}")
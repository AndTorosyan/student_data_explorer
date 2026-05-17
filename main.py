print("hello world")
from src.models import CSVDataSet

if __name__ == "__main__":
    dataset = CSVDataSet("data/sample_scores.csv")
    data = dataset.load()
    print(data.head())
    dataset.describe()
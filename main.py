print("hello world")
from src.models import CSVDataSet
from src.analysis import summarize

if __name__ == "__main__":
    dataset = CSVDataSet("data/sample_scores.csv") 
    data = dataset.load()
    print(data.head())
    dataset.describe()

    with open("outputs/summary.txt", "w") as f:
        summary = summarize(data["score"])
        for i, j in summary.items():
            f.write(f"{i}: {j}\n")
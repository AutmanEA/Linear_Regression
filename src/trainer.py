import pandas as pd


def load_csv(path: str) -> pd.DataFrame | None:
    """CSV file loader to pandas DataFrame, returns None on error"""
    if not isinstance(path, str):
        return None
    try:
        dataset = pd.read_csv(path)
    except Exception:
        return None
    return dataset


class Trainer:
    """docstring"""
    def __init__(self, path: str):
        """docstring"""
        dataset = load_csv(path)
        if dataset is None:
            raise Exception("Failed to load csv file")
        self.km = dataset['km']
        self.price = dataset['price']



data = Trainer("./res/data.csv")
print(data.price)

bug = Trainer(12)
print(bug)

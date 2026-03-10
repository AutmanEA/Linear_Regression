import pandas as pd


def load_csv(path: str) -> pd.DataFrame | None:
    """CSV file loader to pandas DataFrame, returns None on error"""
    if not isinstance(path, str):
        raise Exception("Error: data file path problem.")
    try:
        dataset = pd.read_csv(path)
    except Exception:
        raise Exception("Error: data file path problem.")
    return dataset

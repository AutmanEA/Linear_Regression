from load_csv import load_csv
from thetas import save_thetas
from pandas import Series
import numpy as np


class DataSet:
    def __init__(self, dataset: Series):
        """creates a new data with useful values for training program"""
        if not isinstance(dataset, Series):
            raise Exception("Error: invalid dataset")
        self.dataset = dataset.to_list()
        self.mean = np.mean(dataset)
        self.std = np.std(dataset)
        self.normalized = [(x - self.mean) / self.std for x in self.dataset]


def main():
    try:
        ite = 10000
        learning_rate = 0.01
        tmp0 = 0
        tmp1 = 0
        dataset = load_csv("./res/data.csv")
        km = DataSet(dataset['km'])
        price = DataSet(dataset['price'])
        for _ in range(ite):
            e0 = [(tmp0 + tmp1 * km_i) - price_i
                  for km_i, price_i in zip(km.normalized, price.normalized)]
            e1 = [((tmp0 + tmp1 * km_i) - price_i) * km_i
                  for km_i, price_i in zip(km.normalized, price.normalized)]
            tmp0 = tmp0 - (learning_rate * np.mean(e0))
            tmp1 = tmp1 - (learning_rate * np.mean(e1))
        t1 = tmp1 * (price.std / km.std)
        t0 = (tmp0 * price.std) + price.mean - (t1 * km.mean)
        save_thetas(t0, t1)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("program stopped manualy")


if __name__ == "__main__":
    main()

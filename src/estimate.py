import json
import os


class Estimator:
    """docs"""
    def __init__(self, mileage, thetas_json):
        """docs"""
        self.mileage = mileage
        self.t0 = thetas_json.get('theta0', 0)
        self.t1 = thetas_json.get('theta1', 0)

    def estimate(self):
        """docs"""
        return self.t0 + (self.t1 * self.mileage)


def init_thetas():
    """docstring"""
    with open('./res/thetas.json', 'w') as file:
        thetas = {
            "theta0": 0,
            "theta1": 0
        }
        json.dump(thetas, file, indent=4)


def main():
    """docstring"""
    if not os.path.exists("./res/thetas.json"):
        init_thetas()
    with open('./res/thetas.json', 'r') as file:
        try:
            thetas_json = json.load(file)
        except Exception as e:
            print("Error:", e)
            return
        except KeyboardInterrupt:
            print("program stopped manualy")
            return
    try:
        km = int(input("Enter a mileage: "))
        price = Estimator(km, thetas_json).estimate()
        print("The estimated price is:", price)
    except EOFError:
        print("invalid EOF on input")
    except Exception as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("program stopped manualy")


if __name__ == "__main__":
    main()

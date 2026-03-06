import json
import os


def init_thetas():
    """creates thetas.json file with default value"""
    with open('./res/thetas.json', 'w') as file:
        thetas = {
            "theta0": 0,
            "theta1": 0
        }
        json.dump(thetas, file, indent=4)


def main():
    """this program takes trained or default parameters from file thetas.json
    and estimate price of a car based on its mileage"""
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
        t0 = thetas_json.get('theta0', 0)
        t1 = thetas_json.get('theta1', 0)
        estimatePrice = t0 + (t1 * km)
        print("The estimated price is:", estimatePrice)
    except EOFError:
        print("invalid EOF on input")
    except Exception as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("program stopped manualy")


if __name__ == "__main__":
    main()

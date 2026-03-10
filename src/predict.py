import os
from thetas import init_thetas, load_thetas


def main():
    """this program takes trained or default parameters from file thetas.json
    and estimate price of a car based on its mileage"""
    if not os.path.exists("./res/thetas.json"):
        init_thetas()
    try:
        thetas_json = load_thetas()
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

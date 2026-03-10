import json


def init_thetas():
    """creates thetas.json file with default value"""
    with open('./res/thetas.json', 'w') as file:
        thetas = {
            "theta0": 0,
            "theta1": 0
        }
        json.dump(thetas, file, indent=4)


def load_thetas():
    """loads thetas.json file"""
    with open('./res/thetas.json', 'r') as file:
        try:
            thetas_json = json.load(file)
            return thetas_json
        except Exception as e:
            raise Exception(e)
        except KeyboardInterrupt:
            raise KeyboardInterrupt


def save_thetas(t0, t1):
    """saves t0 and t1 in thetas.json file"""
    with open('./res/thetas.json', 'w') as file:
        thetas = {
            "theta0": t0,
            "theta1": t1
        }
        json.dump(thetas, file, indent=4)

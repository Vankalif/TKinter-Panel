import random
from flask import Flask
import yaml
app = Flask(__name__)


def random_tuple():
    return [round(random.uniform(1.0, 90.0), 2) for x in range(6)]


def generate_vals():
    skv = boreholes["ess_boreholes"] + boreholes["kis_boreholes"] + boreholes["pyat_boreholes"] + boreholes["jel_boreholes"]
    vals = dict.fromkeys(skv)
    for key in vals:
        vals[key] = random_tuple()
    return vals


@app.route('/sensor-values')
def sensor_values():
    vals = generate_vals()
    return vals


@app.route('/config-gui')
def get_config():
    return boreholes


if __name__ == '__main__':
    with open(".\\conf\\conf.yaml", encoding="utf-8") as stream:
        boreholes = yaml.load(stream, Loader=yaml.FullLoader)
    app.run()

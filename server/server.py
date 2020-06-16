from flask import Flask
import yaml
app = Flask(__name__)


@app.route('/sensor-values')
def hello():
    return "Hello World!"


@app.route('/config-gui')
def get_config():
    try:
        with open(".\\conf\\conf.yaml", encoding="utf-8") as stream:
            return yaml.load(stream, Loader=yaml.FullLoader)
    except FileNotFoundError:
        return "Файл конфигурации в папке conf не найден."


if __name__ == '__main__':
    app.run()

import yaml
import requests
import os


class ConfReader:
    def __init__(self):
        # чтение конфигурации для инициализации интерфейса
        response = requests.get("http://127.0.0.1:5000/config-gui")
        self.boreholes = yaml.load(response.content, Loader=yaml.FullLoader)

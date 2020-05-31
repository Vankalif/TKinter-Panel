import yaml
import os


class ConfReader:
    def __init__(self):
        # переменная для отображения ошибки в интерфейсе программы
        self.error_text = None
        # проверка платформы
        if os.name == "nt":
            # чтение конфигурации для инициализации интерфейса
            try:
                with open(".\\conf\\conf.yaml", encoding="utf-8") as stream:
                    self.boreholes = yaml.load(stream, Loader=yaml.FullLoader)
            except FileNotFoundError:
                self.error_text = "Файл конфигурации в папке conf не найден."
                raise
        else:
            try:
                # путь для unix платформ
                with open("./conf/conf.yaml", encoding="utf-8") as stream:
                    self.boreholes = yaml.load(stream, Loader=yaml.FullLoader)
            except FileNotFoundError:
                self.error_text = "Файл конфигурации в папке conf не найден."
                raise


if __name__ == '__main__':
    r = ConfReader()
    print(r.boreholes)

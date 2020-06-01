import tkinter as tk


# класс используется для создания набора датчиков скважин на вкладках участков.
class SensorFrame(tk.LabelFrame):
    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        # строка давление
        self.pressure = tk.Label(self, text="Давление")
        self.pressure_value = tk.Label(self, text="0.0")
        self.pressure_abbreviation = tk.Label(self, text="КПа")
        self.pressure.grid(row=0, column=0, sticky="W")
        self.pressure_value.grid(row=0, column=1)
        self.pressure_abbreviation.grid(row=0, column=2)
        # строка счетчик Д-80
        self.water_sensor_80 = tk.Label(self, text="Счетчик воды Д-80")
        self.water_sensor_80_value = tk.Label(self, text="0.0")
        self.water_sensor_80_abbreviation = tk.Label(self, text="м3/час")
        self.water_sensor_80.grid(row=1, column=0, sticky="W")
        self.water_sensor_80_value.grid(row=1, column=1)
        self.water_sensor_80_abbreviation.grid(row=1, column=2)
        # строка счетчик Д-50
        self.water_sensor_50 = tk.Label(self, text="Счетчик воды Д-50")
        self.water_sensor_50_value = tk.Label(self, text="0.0")
        self.water_sensor_50_abbreviation = tk.Label(self, text="м3/час")
        self.water_sensor_50.grid(row=2, column=0, sticky="W")
        self.water_sensor_50_value.grid(row=2, column=1)
        self.water_sensor_50_abbreviation.grid(row=2, column=2)
        # строка счетчик Д-20
        self.water_sensor_20 = tk.Label(self, text="Счетчик воды Д-20")
        self.water_sensor_20_value = tk.Label(self, text="0.0")
        self.water_sensor_20_abbreviation = tk.Label(self, text="м3/час")
        self.water_sensor_20.grid(row=3, column=0, sticky="W")
        self.water_sensor_20_value.grid(row=3, column=1)
        self.water_sensor_20_abbreviation.grid(row=3, column=2)
        # строка счетчик Д-15
        self.water_sensor_15 = tk.Label(self, text="Счетчик воды Д-15")
        self.water_sensor_15_value = tk.Label(self, text="0.0")
        self.water_sensor_15_abbreviation = tk.Label(self, text="м3/час")
        self.water_sensor_15.grid(row=4, column=0, sticky="W")
        self.water_sensor_15_value.grid(row=4, column=1)
        self.water_sensor_15_abbreviation.grid(row=4, column=2)
        # строка термометр сопротивления КТСП
        self.thermometer = tk.Label(self, text="Термометр сопротивления КТСП")
        self.thermometer_value = tk.Label(self, text="0.0")
        self.thermometer_abbreviation = tk.Label(self, text="C")
        self.thermometer.grid(row=5, column=0, sticky="W")
        self.thermometer_value.grid(row=5, column=1)
        self.thermometer_abbreviation.grid(row=5, column=2)

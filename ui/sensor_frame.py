import tkinter as tk


global_font = ('', 10, "")


# класс используется для создания набора датчиков скважин на вкладках участков.
class SensorFrame(tk.LabelFrame):
    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        self.hidden_name = kw['text']

        # строка давление
        # ячейка давление
        self.pressure_cell = tk.Label(self, text="Давление", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка значения давления
        self.pressure_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self.pressure_abbr_cell = tk.Label(self, text="КПа", bg="#282C34", fg="#989DAC", font=global_font)
        self.pressure_cell.grid(row=0, column=0, sticky="W")
        self.pressure_val_cell.grid(row=0, column=1)
        self.pressure_abbr_cell.grid(row=0, column=2)

        # строка счетчик Д-80
        # ячейка названия счетчика
        self.sensor_80_cell = tk.Label(self, text="Счетчик воды Д-80", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка показателя счетчика
        self.sensor_80_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self.sensor_80_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=global_font)
        self.sensor_80_cell.grid(row=1, column=0, sticky="W")
        self.sensor_80_val_cell.grid(row=1, column=1)
        self.sensor_80_abbr_cell.grid(row=1, column=2)

        # строка счетчик Д-50
        # ячейка названия счетчика
        self.sensor_50_cell = tk.Label(self, text="Счетчик воды Д-50", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка показателя счетчика
        self.sensor_50_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self.sensor_50_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=global_font)
        self.sensor_50_cell.grid(row=2, column=0, sticky="W")
        self.sensor_50_val_cell.grid(row=2, column=1)
        self.sensor_50_abbr_cell.grid(row=2, column=2)

        # строка счетчик Д-20
        # ячейка названия счетчика
        self.sensor_20_cell = tk.Label(self, text="Счетчик воды Д-20", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка показателя счетчика
        self.sensor_20_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self._sensor_20_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=global_font)
        self.sensor_20_cell.grid(row=3, column=0, sticky="W")
        self.sensor_20_val_cell.grid(row=3, column=1)
        self._sensor_20_abbr_cell.grid(row=3, column=2)

        # строка счетчик Д-15
        # ячейка названия счетчика
        self.sensor_15_cell = tk.Label(self, text="Счетчик воды Д-15", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка показателя счетчика
        self.sensor_15_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self.sensor_15_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=global_font)
        self.sensor_15_cell.grid(row=4, column=0, sticky="W")
        self.sensor_15_val_cell.grid(row=4, column=1)
        self.sensor_15_abbr_cell.grid(row=4, column=2)

        # строка термометр сопротивления КТСП
        # ячейка названия счетчика
        self.therm_cell = tk.Label(self, text="Термометр сопротивления КТСП", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка показателя счетчика
        self.therm_val_cell = tk.Label(self, text="0.0", bg="#282C34", fg="#989DAC", font=global_font)
        # ячейка аббревитуры единицы изменерния
        self.therm_abbr_cell = tk.Label(self, text="C", bg="#282C34", fg="#989DAC", font=global_font)
        self.therm_cell.grid(row=5, column=0, sticky="W")
        self.therm_val_cell.grid(row=5, column=1)
        self.therm_abbr_cell.grid(row=5, column=2)

    def update_values(self, val):
        pass

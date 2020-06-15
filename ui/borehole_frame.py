import tkinter as tk


GLOBAL_FONT = ('', 10, "")


# класс используется для создания набора датчиков скважин на вкладках участков.
class BoreholeFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw, bg="#282C34", fg="#E4BF7B", font=("", 12, "bold"))
        self.borehole_name = kw["text"]
        self.pressure_val = tk.DoubleVar()
        self.pressure_val.set(0.0)
        self.sensor_80_val = tk.DoubleVar()
        self.sensor_80_val.set(0.0)
        self.sensor_50_val = tk.DoubleVar()
        self.sensor_50_val.set(0.0)
        self.sensor_20_val = tk.DoubleVar()
        self.sensor_20_val.set(0.0)
        self.sensor_15_val = tk.DoubleVar()
        self.sensor_15_val.set(0.0)
        self.therm_val = tk.DoubleVar()
        self.therm_val.set(0.0)

        # строка давление
        # ячейка давление
        self.pressure_cell = tk.Label(self, text="Давление", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка значения давления
        self.pressure_val_cell = tk.Label(self, textvariable=self.pressure_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self.pressure_abbr_cell = tk.Label(self, text="КПа", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.pressure_cell.grid(row=0, column=0, sticky="W")
        self.pressure_val_cell.grid(row=0, column=1)
        self.pressure_abbr_cell.grid(row=0, column=2)

        # строка счетчик Д-80
        # ячейка названия счетчика
        self.sensor_80_cell = tk.Label(self, text="Счетчик воды Д-80", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка показателя счетчика
        self.sensor_80_val_cell = tk.Label(self, textvariable=self.sensor_80_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self.sensor_80_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.sensor_80_cell.grid(row=1, column=0, sticky="W")
        self.sensor_80_val_cell.grid(row=1, column=1)
        self.sensor_80_abbr_cell.grid(row=1, column=2)

        # строка счетчик Д-50
        # ячейка названия счетчика
        self.sensor_50_cell = tk.Label(self, text="Счетчик воды Д-50", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка показателя счетчика
        self.sensor_50_val_cell = tk.Label(self, textvariable=self.sensor_50_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self.sensor_50_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.sensor_50_cell.grid(row=2, column=0, sticky="W")
        self.sensor_50_val_cell.grid(row=2, column=1)
        self.sensor_50_abbr_cell.grid(row=2, column=2)

        # строка счетчик Д-20
        # ячейка названия счетчика
        self.sensor_20_cell = tk.Label(self, text="Счетчик воды Д-20", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка показателя счетчика
        self.sensor_20_val_cell = tk.Label(self, textvariable=self.sensor_20_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self._sensor_20_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.sensor_20_cell.grid(row=3, column=0, sticky="W")
        self.sensor_20_val_cell.grid(row=3, column=1)
        self._sensor_20_abbr_cell.grid(row=3, column=2)

        # строка счетчик Д-15
        # ячейка названия счетчика
        self.sensor_15_cell = tk.Label(self, text="Счетчик воды Д-15", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка показателя счетчика
        self.sensor_15_val_cell = tk.Label(self, textvariable=self.sensor_15_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self.sensor_15_abbr_cell = tk.Label(self, text="м3/час", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.sensor_15_cell.grid(row=4, column=0, sticky="W")
        self.sensor_15_val_cell.grid(row=4, column=1)
        self.sensor_15_abbr_cell.grid(row=4, column=2)

        # строка термометр сопротивления КТСП
        # ячейка названия счетчика
        self.therm_cell = tk.Label(self, text="Термометр сопротивления КТСП", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка показателя счетчика
        self.therm_val_cell = tk.Label(self, textvariable=self.therm_val, bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        # ячейка аббревитуры единицы изменерния
        self.therm_abbr_cell = tk.Label(self, text="C", bg="#282C34", fg="#989DAC", font=GLOBAL_FONT)
        self.therm_cell.grid(row=5, column=0, sticky="W")
        self.therm_val_cell.grid(row=5, column=1)
        self.therm_abbr_cell.grid(row=5, column=2)

    def set_values(self, values):
        if values[0] > 30:
            self.pressure_val_cell.config(fg="red")
        else:
            self.pressure_val_cell.config(fg="green")

        if values[1] > 40:
            self.sensor_80_val_cell.config(fg="red")
        else:
            self.sensor_80_val_cell.config(fg="green")

        self.sensor_50_val_cell.config(fg="red") if values[2] > 25 else self.sensor_50_val_cell.config(fg="green")
        self.pressure_val.set(values[0])
        self.sensor_80_val.set(values[1])
        self.sensor_50_val.set(values[2])
        self.sensor_20_val.set(values[3])
        self.sensor_15_val.set(values[4])
        self.therm_val.set(values[5])

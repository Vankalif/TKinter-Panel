import tkinter as tk
from tkinter import ttk
from ui.sensor_frame import SensorFrame
from utils.conf_reader import ConfReader


class MainWindow(tk.Frame):
    def __init__(self, root, boreholes):
        super().__init__(root)
        self.boreholes = boreholes
        self.init_main()

    def init_main(self):
        tab_control = ttk.Notebook()
        ess_tab = ttk.Frame(tab_control)
        kis_tab = ttk.Frame(tab_control)
        pyat_tab = ttk.Frame(tab_control)
        jel_tab = ttk.Frame(tab_control)
        archive_tab = ttk.Frame(tab_control)
        tab_control.add(ess_tab, text="ЕЭУ")
        tab_control.add(kis_tab, text="КЭУ")
        tab_control.add(pyat_tab, text="ПЭУ")
        tab_control.add(jel_tab, text="ЖЭУ")
        tab_control.add(archive_tab, text="Архивы")
        tab_control.pack(expand=1, fill="both")
        skv_sensor = SensorFrame(ess_tab, text="5/0")
        skv_sensor.grid(row=0, column=0, padx=10)
        skv_sensor2 = SensorFrame(ess_tab, text="5/0 БИС")
        skv_sensor2.grid(row=0, column=1, padx=10)
        skv_sensor3 = SensorFrame(ess_tab, text="5/0 БИС")
        skv_sensor3.grid(row=0, column=2, padx=10)
        skv_sensor4 = SensorFrame(ess_tab, text="5/0 БИС")
        skv_sensor4.grid(row=0, column=3, padx=10)
        skv_sensor5 = SensorFrame(ess_tab, text="5/0 БИС")
        skv_sensor5.grid(row=0, column=4, padx=10)


if __name__ == '__main__':
    try:
        boreholes_list = ConfReader().boreholes
    except FileNotFoundError:
        pass

    root = tk.Tk()
    app = MainWindow(root, boreholes=boreholes_list)
    root.title("Мониторинг")
    root.geometry("1400x600")
    root.resizable(False, False)
    root.mainloop()


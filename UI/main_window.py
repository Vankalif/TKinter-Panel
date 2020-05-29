import tkinter as tk
from tkinter import ttk
from UI.sensor_frame import SensorFrame


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
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
        skv_sensor.grid(row=0, column=0)
        skv_sensor2 = SensorFrame(ess_tab, text="5/0 БИС")
        skv_sensor2.grid(row=0, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.title("Мониторинг")
    root.geometry("1400x600")
    root.resizable(False, False)
    root.mainloop()

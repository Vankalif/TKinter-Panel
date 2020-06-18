import requests
import json
import tkinter as tk
from tkinter import ttk
from utils.conf_reader import ConfReader
from ui.remote_site_tab import RemoteSiteTab


class MainWindow(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.s = ttk.Style()
        self.s.configure("new.TFrame", background="#282C34")
        self.title("Мониторинг")
        self.geometry("1505x700")
        self.resizable(False, False)
        self.boreholes = ConfReader().boreholes
        self.tab_control = ttk.Notebook()
        self.ess_tab = RemoteSiteTab(self.tab_control, boreholes=self.boreholes, site="ess_boreholes", style="new.TFrame")
        self.kis_tab = RemoteSiteTab(self.tab_control, boreholes=self.boreholes, site="kis_boreholes", style="new.TFrame")
        self.pyat_tab = RemoteSiteTab(self.tab_control, boreholes=self.boreholes, site="pyat_boreholes", style="new.TFrame")
        self.jel_tab = RemoteSiteTab(self.tab_control, boreholes=self.boreholes, site="jel_boreholes", style="new.TFrame")
        self.archive_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.ess_tab, text="ЕЭУ")
        self.tab_control.add(self.kis_tab, text="КЭУ")
        self.tab_control.add(self.pyat_tab, text="ПЭУ")
        self.tab_control.add(self.jel_tab, text="ЖЭУ")
        self.tab_control.add(self.archive_tab, text="Архивы")
        self.tab_control.pack(expand=1, fill="both")
        self.vals = self.get_vals()

    def get_vals(self):
        response = requests.get("http://127.0.0.1:5000/sensor-values")
        json_data = json.loads(str(response.content, encoding='utf-8'))
        return json_data

    def update_tabs(self):
        self.ess_tab.update_boreholes_frames(self.vals)
        self.kis_tab.update_boreholes_frames(self.vals)
        self.pyat_tab.update_boreholes_frames(self.vals)
        self.jel_tab.update_boreholes_frames(self.vals)
        self.vals = self.get_vals()
        self.after(3000, self.update_tabs)


if __name__ == '__main__':
    app = MainWindow()
    app.after(3000, app.update_tabs)
    app.mainloop()


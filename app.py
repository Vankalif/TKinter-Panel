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
        self.geometry("1435x700")
        self.resizable(False, False)
        self.boreholes = ConfReader().boreholes
        self.init_main()

    def init_main(self):
        tab_control = ttk.Notebook()
        ess_tab = RemoteSiteTab(tab_control, boreholes=self.boreholes, site="ess_boreholes", style="new.TFrame")
        kis_tab = RemoteSiteTab(tab_control, boreholes=self.boreholes, site="kis_boreholes", style="new.TFrame")
        pyat_tab = RemoteSiteTab(tab_control, boreholes=self.boreholes, site="pyat_boreholes", style="new.TFrame")
        jel_tab = RemoteSiteTab(tab_control, boreholes=self.boreholes, site="jel_boreholes", style="new.TFrame")
        archive_tab = ttk.Frame(tab_control)
        tab_control.add(ess_tab, text="ЕЭУ")
        tab_control.add(kis_tab, text="КЭУ")
        tab_control.add(pyat_tab, text="ПЭУ")
        tab_control.add(jel_tab, text="ЖЭУ")
        tab_control.add(archive_tab, text="Архивы")
        tab_control.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()


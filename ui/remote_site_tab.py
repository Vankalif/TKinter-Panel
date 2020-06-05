from tkinter import ttk
from ui.sensor_frame import SensorFrame


class RemoteSiteTab(ttk.Frame):
    def __init__(self, root, boreholes, site, **kw):
        super().__init__(root, **kw)
        self.boreholes = boreholes
        self.site = site
        self.frames = [SensorFrame(self, text=borehole_name) for borehole_name in self.boreholes[site]]
        self.tab_columns = 0
        self.tab_row = 0
        for sensor_frame in self.frames:
            if self.tab_columns != 5:
                sensor_frame.grid(row=self.tab_row, column=self.tab_columns, padx=10, pady=5)
                self.tab_columns += 1
            else:
                self.tab_columns = 0
                self.tab_row += 1
                sensor_frame.grid(row=self.tab_row, column=self.tab_columns, padx=10, pady=5)
                self.tab_columns += 1

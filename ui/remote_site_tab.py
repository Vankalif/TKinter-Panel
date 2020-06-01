from tkinter import ttk
from ui.sensor_frame import SensorFrame


class RemoteSiteTab(ttk.Frame):
    def __init__(self, root, boreholes, site, **kw):
        super().__init__(root, **kw)
        self.boreholes = boreholes
        self.site = site
        self.frames = []
        self.tab_columns = 0
        self.tab_row = 0
        for borehole_name in self.boreholes[site]:
            if self.tab_columns != 5:
                self.frames.append(SensorFrame(self, text=borehole_name).grid(row=self.tab_row,
                                                                              column=self.tab_columns,
                                                                              padx=10,
                                                                              pady=5))
                self.tab_columns += 1
            else:
                self.tab_columns = 0
                self.tab_row += 1
                self.frames.append(SensorFrame(self, text=borehole_name).grid(row=self.tab_row,
                                                                              column=self.tab_columns,
                                                                              padx=10,
                                                                              pady=5))

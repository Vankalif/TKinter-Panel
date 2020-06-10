from tkinter import ttk
from ui.sensor_frame import SensorFrame


class RemoteSiteTab(ttk.Frame):
    def __init__(self, root, boreholes, site, **kw):
        super().__init__(root, **kw)
        self.boreholes = boreholes
        self.site = site
        self.frames = [SensorFrame(self, text=borehole_name, bg="#282C34",
                                   fg="#E4BF7B", font=('', 12, "bold")) for borehole_name in self.boreholes[site]]
        # https://ru.stackoverflow.com/questions/1136725
        self.column_count = 5
        for i, sensor_frame in enumerate(self.frames):
            tab_row, tab_columns = divmod(i, self.column_count)
            sensor_frame.grid(row=tab_row, column=tab_columns, padx=10, pady=5)

from tkinter import ttk
from ui.borehole_frame import BoreholeFrame


# Класс для создания вкладки с названием участка
class RemoteSiteTab(ttk.Frame):
    def __init__(self, parent, boreholes, site, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.boreholes = boreholes
        self.site = site
        self.frames = [BoreholeFrame(self, text=borehole_name) for borehole_name in self.boreholes[site]]
        # https://ru.stackoverflow.com/questions/1136725
        # отрисовка фреймов датчиков на вкладках
        self.column_count = 5
        for i, sensor_frame in enumerate(self.frames):
            tab_row, tab_columns = divmod(i, self.column_count)
            sensor_frame.grid(row=tab_row, column=tab_columns, padx=5, pady=5)

    def update_boreholes_frames(self):
        for frame in self.frames:
            print(frame.borehole_name)

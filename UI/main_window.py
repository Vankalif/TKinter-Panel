from tkinter import *
from tkinter import ttk


class MainWindowTabs:
    def __init__(self, root):
        # навигатор вкладок
        tab_control = ttk.Notebook(main_window)
        # ессентукская вкладка
        ess_tab = ttk.Frame(tab_control)
        # добавить вкладку на окно
        tab_control.add(ess_tab, text="ЕЭУ")
        # расположить на главном окне
        tab_control.pack(expand=1, fill="both")

        skv_frame = LabelFrame(ess_tab, text="5/0", width="50", height="50", bg="gray")
        skv_frame.grid(row=0, column=0)


# конфигурвция главного окна
main_window = Tk()
main_window.title("Мониторинг")
main_window.geometry("1400x600")
main_window.resizable(0, 0)
tabs = MainWindowTabs(main_window)
main_window.mainloop()

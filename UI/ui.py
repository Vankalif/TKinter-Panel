from tkinter import *
from tkinter import ttk

# конфигурвция главного окна
main_window = Tk()
main_window.title("Мониторинг")
main_window.geometry("1400x600")
main_window.resizable(0, 0)

# навигатор вкладок
tab_control = ttk.Notebook(main_window)
# ессентукская вкладка
ess_tab = ttk.Frame(tab_control)
# кисловодская вкладка
kis_tab = ttk.Frame(tab_control)
# пятигорская вкладка
pyat_tab = ttk.Frame(tab_control)
# железноводская вкладка
jelez_tab = ttk.Frame(tab_control)
# вкладка архивы
archive_tab = ttk.Frame(tab_control)

# добавить вкладку на окно
tab_control.add(ess_tab, text="ЕЭУ")
tab_control.add(kis_tab, text="КЭУ")
tab_control.add(pyat_tab, text="ПЭУ")
tab_control.add(jelez_tab, text="ЖЭУ")
tab_control.add(archive_tab, text="Архивы")

tab_control.pack(expand=1, fill="both")

main_window.mainloop()

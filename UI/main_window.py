import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        tab_control = ttk.Notebook()
        ess_tab = ttk.Frame(tab_control)
        tab_control.add(ess_tab, text="ЕЭУ")
        tab_control.pack(expand=1, fill="both")


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.title("Мониторинг")
    root.geometry("1400x600")
    root.resizable(False, False)
    root.mainloop()

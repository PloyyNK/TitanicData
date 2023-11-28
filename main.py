from titanic_class import Titanic
from titanicUI import TitanicUI
import tkinter as tk


if __name__ == '__main__':
    """Launch the application."""
    root = tk.Tk()
    root.title("Titanic Ticket Rate")
    root.geometry("680x800")
    app = TitanicUI(root)
    root.mainloop()

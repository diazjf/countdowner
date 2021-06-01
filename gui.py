import tkinter as tk

class GUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Rachel's Vest Date Countdown")
        self.master.option_add('*Font', '50')
        self.master.geometry("350x150")
        self.label = tk.Label(self.master)
        self.label.pack()

    def changeLabel(self, text):
        message = "%s days to go!!" % text
        self.label.config(text = message, font = "Times 20")
        self.label.pack(padx = 10, pady = 50)
import tkinter as tk


class ViewText(tk.Text):

    main_view = None
    controller = None

    def __init__(self, main_view, controller):
        tk.Text.__init__(self, main_view)
        self.main_view = main_view
        self.controller = controller
        self.configure(state="disabled")

    def do_pack(self):
        self.pack(side="left", expand=True)

    def set_text(self, text_model):
        self.configure(state='normal')
        self.delete('1.0', tk.END)
        self.insert("end", text_model.text)
        self.configure(state='disabled')




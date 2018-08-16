import tkinter as tk


class ViewMenuBar(tk.Frame):

    main_view = None
    controller = None

    def __init__(self, main_view, controller):
        self.main_view = main_view
        self.controller = controller
        tk.Frame.__init__(self, main_view)

        self.prev_btn = tk.Button(self, text="Previous", command=self.switch_previous)
        self.next_btn = tk.Button(self, text="Next", command=self.switch_next)

    def do_pack(self):
        self.pack(side="bottom")
        self.prev_btn.pack(side="left")
        self.next_btn.pack(side="left")

    def switch_previous(self):
        self.controller.previous()

    def switch_next(self):
        self.controller.next()
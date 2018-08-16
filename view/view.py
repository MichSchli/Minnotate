import tkinter as tk
from tkinter.font import Font


class View(tk.Frame):

    controller = None

    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        tk.Frame.__init__(self, self.root)

        #self.toolbar = tk.Frame(self, bg="#eee")
        #self.toolbar.pack(side="top", fill="x")

        #self.bold_btn = tk.Button(self.toolbar, text="Bold", command=self.make_bold)
        #self.bold_btn.pack(side="left")

        #self.clear_btn = tk.Button(self.toolbar, text="Clear", command=self.clear)
        #self.clear_btn.pack(side="left")

        # Creates a bold font
        #self.bold_font = Font(family="Helvetica", size=14, weight="bold")

        #self.text = tk.Text(self)
        #self.text.insert("end", "Select part of text and then click 'Bold'...")
        #self.text.focus()
        #self.text.pack(fill="both", expand=True)

        # configuring a tag called BOLD
        #self.text.tag_configure("BOLD", background="green")

    def make_bold(self):
        # tk.TclError exception is raised if not text is selected
        try:
            self.text.tag_add("BOLD", "sel.first", "sel.last")
            #REVERSE IS tag_remove
        except tk.TclError:
            pass

    def clear(self):
        self.text.tag_remove("BOLD", "1.0", 'end')

    def display(self):
        self.pack(expand=1, fill="both")
        self.root.mainloop()

    def show(self, model):
        self.winfo_toplevel().title("Minnotate: " + model.filename)
        self.view_text.set_text(model)
        self.view_annotation_list.set_annotations(model.annotations)

    def show_annotation(self, annotation):
        self.view_selected_annotation.set_annotation(annotation)

    def clear_annotation(self):
        self.view_selected_annotation.clear()
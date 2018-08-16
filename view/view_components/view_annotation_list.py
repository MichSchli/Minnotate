import tkinter as tk


class ViewAnnotationList(tk.Listbox):

    main_view = None
    controller = None
    annotations = None

    def __init__(self, main_view, controller):
        self.main_view = main_view
        self.controller = controller
        tk.Listbox.__init__(self, main_view)
        self.bind("<<ListboxSelect>>", self.selection_changed)

    def do_pack(self):
        self.pack(side="right")

    def set_annotations(self, annotations):
        self.annotations = annotations[:]
        self.delete(0, "end")
        for annotation in self.annotations:
            self.add_annotation(annotation)

    def add_annotation(self, annotation):
        self.insert("end", annotation.get_title())

    def selection_changed(self, event):
        selected_item = self.annotations[self.curselection()[0]]
        self.controller.select_annotation(selected_item)
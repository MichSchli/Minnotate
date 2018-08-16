import tkinter as tk

class ViewSelectedAnnotation(tk.Text):

    main_view = None
    controller = None
    annotation = None

    def __init__(self, main_view, controller):
        tk.Text.__init__(self, main_view)
        self.main_view = main_view
        self.controller = controller
        self._resetting_modified_flag = False
        self.bind("<<Modified>>", self._beenModified)

    def do_pack(self):
        self.pack(side="right")

    def clear(self):
        self.annotation = None
        self.delete('1.0', tk.END)

    def set_annotation(self, annotation):
        self.clear()

        self.annotation = annotation
        self.insert("end", annotation.note)

    def _beenModified(self, event=None):
        if self._resetting_modified_flag:
            return

        self.beenModified(event)
        self.clearModifiedFlag()

    def beenModified(self, event=None):
        new_text = self.get("1.0", "end")

        if self.annotation is not None:
            self.annotation.note = new_text.strip()
            self.annotation.mark_changed()

    def clearModifiedFlag(self):
        self._resetting_modified_flag = True
        try:
            self.tk.call(self._w, 'edit', 'modified', 0)
        finally:
            self._resetting_modified_flag = False
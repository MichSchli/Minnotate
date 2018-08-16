class AnnotationModel:

    filename = None
    start_index = None
    end_index = None
    title = None
    note = None

    changed = False

    def __init__(self, filename):
        self.filename = filename

    def get_title(self):
        if self.title is not None:
            return self.title

        return str(self.start_index) + "-" + str(self.end_index)

    def mark_changed(self):
        self.changed = True

    def to_json(self):
        return {"start_index": self.start_index,
                "end_index": self.end_index,
                "note": self.note}
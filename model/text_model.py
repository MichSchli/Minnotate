class TextModel:

    identifier = None
    filename = None
    text = None
    annotations = None

    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.annotations = []

    def clear_annotations(self):
        self.annotations = []

    def add_annotation(self, annotation):
        self.annotations.append(annotation)

    def get_filename(self):
        return self.filename

    def get_text(self):
        return self.text

    def get_annotations(self):
        return self.annotations
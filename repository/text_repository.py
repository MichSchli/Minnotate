import os

from model.text_model import TextModel


class TextRepository:

    texts = None
    annotation_repository = None

    def __init__(self, annotation_repository):
        self.texts = []
        self.annotation_repository = annotation_repository

    def get(self, identifier):
        if identifier >= len(self.texts) or identifier < 0:
            return None
        else:
            return self.texts[identifier]

    def load_from_folder(self, folder_name):
        for filename in sorted(os.listdir(folder_name)):
            if not filename.endswith(".annotations.json"):
                file_location = folder_name + "/" + filename
                with open(file_location, 'r') as source_file:
                    source_text = source_file.read()
                    model = TextModel(filename, source_text)
                    self.create(model)
                    self.annotation_repository.load_annotations(file_location)
                    self.populate(model)

    def create(self, model):
        identifier = len(self.texts)
        model.identifier = identifier
        self.texts.append(model)

    def populate(self, model):
        model.clear_annotations()
        for annotation in self.annotation_repository.get(model.filename):
            model.add_annotation(annotation)

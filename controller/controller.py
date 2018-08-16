from repository.annotation_repository import AnnotationRepository
from repository.text_repository import TextRepository


class Controller:

    current_text_id = None
    view_model = None

    def __init__(self):
        self.current_text_id = 0
        self.annotation_repository = AnnotationRepository()
        self.text_repository = TextRepository(self.annotation_repository)

    def load_data(self, data_dir):
        self.text_repository.load_from_folder(data_dir)

    def current(self):
        return self.text_repository.get(self.current_text_id)

    def save_annotations(self):
        annotations = self.view_model.current_model.annotations

        for annotation in annotations:
            if annotation.changed:
                annotation.changed = False
                self.annotation_repository.save_annotations(annotation.filename)
                break

    def next(self):
        self.save_annotations()
        current_id = self.view_model.get_current_id()
        new_model = self.text_repository.get(current_id + 1)

        if new_model is not None:
            self.view_model.switch(new_model)

    def previous(self):
        self.save_annotations()
        current_id = self.view_model.get_current_id()
        new_model = self.text_repository.get(current_id - 1)

        if new_model is not None:
            self.view_model.switch(new_model)

    def set_view_model(self, view_model):
        self.view_model = view_model

    def initialize(self):
        first_model = self.text_repository.get(0)
        self.view_model.switch(first_model)

    def select_annotation(self, annotation):
        self.view_model.show_annotation(annotation)
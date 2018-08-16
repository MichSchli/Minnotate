import json

from model.annotation_model import AnnotationModel


class AnnotationRepository:
    annotations = None

    def __init__(self):
        self.annotations = {}

    def get(self, identifier):
        if identifier not in self.annotations:
            return []
        else:
            return self.annotations[identifier]

    def save_annotations(self, identifier):
        annotation_location = "sample_data/" + identifier + ".annotations.json"
        annotations = self.get(identifier)
        if len(annotations) > 0:
            annotation_dict = {"filename": identifier,
                               "annotations": []}

            for annotation in annotations:
                annotation_dict["annotations"].append(annotation.to_json())

            with open(annotation_location, 'w') as fp:
                json.dump(annotation_dict, fp)

    def load_annotations(self, filename):
        try:
            annotation_location = filename + ".annotations.json"
            with open(annotation_location, 'r') as source_file:
                json_data = json.load(source_file)
                for annotation_line in json_data["annotations"]:
                    model = AnnotationModel(json_data["filename"])
                    model.start_index = self.variable_read(annotation_line, "start_index")
                    model.end_index = self.variable_read(annotation_line, "end_index")
                    model.note = self.variable_read(annotation_line, "note")
                    self.create(model)
        except FileNotFoundError:
            pass

    def variable_read(self, annotation_line, variable_name):
        return annotation_line[variable_name] if variable_name in annotation_line else None

    def create(self, model):
        identifier = model.filename
        if identifier is not None:
            if identifier not in self.annotations:
                self.annotations[identifier] = []
            self.annotations[identifier].append(model)
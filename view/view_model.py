class ViewModel:

    current_model = None

    def __init__(self, view):
        self.view = view

    def switch(self, model):
        self.clear_annotation()
        self.current_model = model
        self.view.show(model)

    def get_current_id(self):
        return self.current_model.identifier

    def clear_annotation(self):
        self.view.clear_annotation()

    def show_annotation(self, annotation):
        self.view.show_annotation(annotation)
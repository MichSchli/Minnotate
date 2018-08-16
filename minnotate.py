from controller.controller import Controller
from helpers.configuration_loader import ConfigurationLoader
from view.view import View
from view.view_factory import ViewFactory
from view.view_model import ViewModel

configuration_filename = "minnotate.cfg"
configuration_loader = ConfigurationLoader()
configuration = configuration_loader.load(configuration_filename)

controller = Controller()
controller.load_data(configuration["data_dir"])

view_factory = ViewFactory()
view = view_factory.make_view(controller)

view_model = ViewModel(view)
controller.set_view_model(view_model)

controller.initialize()
view.display()
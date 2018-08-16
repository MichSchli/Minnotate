import tkinter as tk

from view.view import View
from view.view_components.view_annotation_list import ViewAnnotationList
from view.view_components.view_menu_bar import ViewMenuBar
from view.view_components.view_selected_annotation import ViewSelectedAnnotation
from view.view_components.view_text import ViewText


class ViewFactory:

    def make_view(self, controller):
        root = tk.Tk()
        view = View(root, controller)

        view.view_text = ViewText(view, controller)
        view.view_text.do_pack()

        view.view_menu_bar = ViewMenuBar(view, controller)
        view.view_menu_bar.do_pack()

        view.view_annotation_list = ViewAnnotationList(view, controller)
        view.view_annotation_list.do_pack()

        view.view_selected_annotation = ViewSelectedAnnotation(view, controller)
        view.view_selected_annotation.do_pack()

        return view
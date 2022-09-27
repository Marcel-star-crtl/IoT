from cgitb import text
from turtle import width
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

name_handler = """
MDTextField:
    hint_text: "Enter device name: "
    helper_text: "Enter name of device"
    helper_text_mode: "on_focus"
    icon_right: "plus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint : {'center_x': 0.5,'center_y': 0.5}
    size_hint_x : None
    width: 200
"""

class MyApp(MDApp):
    def build(self):
        scr = Screen()
        self.theme_cls.primary_palette = "Green"
        # name = MDTextField(
        #     text = "Enter User Name",
        #     pos_hint = {'center_x': 0.5,'center_y': 0.5},
        #     size_hint = {0.3, 1}
        # )

        name = Builder.load_string(name_handler)
        scr.add_widget(name)
        return scr

MyApp().run()
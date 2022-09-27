from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helper import name_handler

class MyApp(MDApp):
    def build(self):
        scr = Screen()
        self.theme_cls.primary_palette = "Green"
        # name = MDTextField(
        #     text = "Enter User Name",
        #     pos_hint = {'center_x': 0.5,'center_y': 0.5},
        #     size_hint = {0.3, 1}
        # )

        btn = MDFloatingActionButton(
            icon = "plus",
            pos_hint = {'center_x': 0.5,'center_y': 0.37},
            on_release = self.show_data
        )
        name = Builder.load_string(name_handler)
        self.fname = name
        scr.add_widget(self.fname)
        scr.add_widget(btn)
        return scr

    def show_data(self, obj):
        print(self.fname.text)

MyApp().run()
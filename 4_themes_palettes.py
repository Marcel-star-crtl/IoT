from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Green'      # primary theme
        self.theme_cls.primary_hue = "A700"         # primary theme hue
        self.theme_cls.theme_style = 'Dark'         # background color         
        myscreen = Screen()
        btn = MDRectangleFlatButton(
            text = "Click here",
            pos_hint = {'center_x':0.5, 'center_y':0.5},
        )
        myscreen.add_widget(btn)
        return myscreen

MyApp().run()
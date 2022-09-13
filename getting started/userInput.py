from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from  kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from helpers import username_helper



class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"
        # username = MDTextField(text='Enter username',
        #                         pos_hint={'center_x':0.5, 'center_y':0.5},
        #                         size_hint_x=None, width=300)

        button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                        on_release=self.show_data)

        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):
        dailog = MDDialog(title='Username',text=self.username.text,
                            size_hint=(0.55, 1))
        dailog.open()

DemoApp().run()
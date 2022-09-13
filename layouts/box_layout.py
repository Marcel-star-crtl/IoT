from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 600)

class App(MDApp):
    def build(self):
        self.screen = Builder.load_file('box_layout.kv')
        return self.screen

App().run()
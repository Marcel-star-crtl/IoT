from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
BoxLayout:
    orientation: 'vertical'
    ColorPicker:
        id: cp
    Label:
        size_hint_y: None
        height: 30
        text: f'Color with hex value: {cp.hex_color} selected'
"""


class CPApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


CPApp().run()
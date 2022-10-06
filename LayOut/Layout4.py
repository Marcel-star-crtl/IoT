from kivy.app import App
from kivy.lang import Builder
from kivy.uix.spinner import Spinner

kv = """
AnchorLayout:
    LimitSpinner:
        size_hint: None, None
        size: 200, 48
        text: 'Value 0'
        values: [f'Values {x}' for x in range(50)]      
"""


class LimitSpinner(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown_cls.max_height = 4 * 48


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()
from kivymd.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import NumericProperty

kv = """
<HeightButton>:
    size_hint_y: None
    height: app.root.ids.slider.value
    text: f'Button {self.number} height: {self.height:.1f}'

BoxLayout:
    orientation: 'vertical'
    ScrollView:
        BoxLayout:
            id: scroll_box
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
    Label:
        size_hint_y: None
        height: 30
        background_color: 0, 0, 0
        text: 'Slide to change widget size'
    Slider:
        id: slider
        value: 50
        size_hint_y: None
        height: 60
        min: 20
        max: 100
"""


class HeightButton(Button):
    number = NumericProperty()


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        for i in range(50):
            self.root.ids.scroll_box.add_widget(HeightButton(number=i))


MyApp().run()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

kv = """
<Ball>:
    size_hint: None, None

    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Ellipse:
            size: self.size
            pos: self.pos


<ButtonBubble>:

    orientation: 'horizontal'
    spacing: self.width * .1
    padding: self.width * .1

    Button:
        id: left_button
        background_color: 0, 1, 0, .5
        on_press: 

    Button:
        id: right_button
        text: "Click Me"
        background_color: 0, 1, 0, .5
        on_press: app.root.current = 'ScreenTwo'

<BScreen>:
    ButtonBubble:
        id: btns
    Ball:
        size: self.set_size(btns.ids.left_button.width, btns.ids.left_button.height)
        pos: self.set_pos(btns.ids.left_button.size, btns.ids.left_button.pos)

ScreenManager:
    BScreen:
        name: 'ScreenOne'
    BScreen:
        name: 'ScreenTwo'
"""


class Ball(Widget):
    def set_size(self, w, h):
        return min(w, h), min(w, h)

    def set_pos(self, b_size, b_pos): # button size and pos
        x = (b_size[0] - self.height) / 2 + b_pos[0]
        y = (b_size[1] - self.height) / 2 + b_pos[1]
        return x, y


class ButtonBubble(BoxLayout):
    pass


class BScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    MyApp().run()
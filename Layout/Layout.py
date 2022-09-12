import kivymd
from kivy.app import App
import random
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

Window.clearcolor = (0, 0, 0, 1)

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        colors = [red, green, blue, purple]

        self.add_widget(Image(source="celebrate.jpg"))

        self.sub = GridLayout()
        self.sub.cols = 2

        self.sub.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.sub.add_widget(self.name)

        self.sub.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.sub.add_widget(self.lastName)

        self.sub.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.sub.add_widget(self.email)

        self.add_widget(self.sub)

        self.send = Button(text="Send", font_size=30, background_color=random.choice(colors))
        self.add_widget(self.send)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
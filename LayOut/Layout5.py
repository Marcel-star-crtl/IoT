from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

kv = """
<MyTextInput>:
    cols: 2
    rows: 2

    Label:
        id: counter_label
        text: "IOT"
        font_size: "80dp"
        color: .2, .2, 1, 1

    TextInput:
        id: t_input
        hint_text: 'Enter text'

    Label:  
        text: 'Column 0, row 1'
    Label:
        text: 'Column 1, row 1'

MyTextInput:

"""


class MyTextInput(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()
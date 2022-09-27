from cgitb import text
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class App(MDApp):
    def build(self):
        MyScreen = Screen()
        # flat button
        # Button = MDFlatButton(
        #     text = 'First Button',
        #     pos_hint={'center_x':0.5, 'center_y':0.5}
        # )

        # formatted button
        # Button = MDRectangleFlatButton(
        #     text = 'First Button',
        #     pos_hint={'center_x':0.5, 'center_y':0.5}
        # )

        # icon button
        # Button = MDIconButton(
        #     icon = 'plus',
        #     pos_hint={'center_x':0.5, 'center_y':0.5}
        # )

        # floating action button
        Button = MDFloatingActionButton(
            icon = 'plus',
            pos_hint={'center_x':0.5, 'center_y':0.5}
        )

        MyScreen.add_widget(Button)
        return MyScreen

App().run()
from cgitb import text
from tkinter import dialog
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helper import name_handler

class MyApp(MDApp):
    def build(self):
        scr = Screen()
        self.theme_cls.primary_palette = "Green"
        # name = MDTextField(
        #     text = "Enter User Name",
        #     pos_hint = {'center_x': 0.5,'center_y': 0.5},
        #     size_hint = {0.3, 1}
        # )]

        btn = MDFloatingActionButton(
            icon = "plus",
            pos_hint = {'center_x': 0.5,'center_y': 0.37},
            on_press = self.show_box
        )
        name = Builder.load_string(name_handler)
        self.fname = name
        scr.add_widget(self.fname)
        scr.add_widget(btn)
        return scr

    def show_box(self, obj):
        if self.fname.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.fname.text + ' Successfully added'
        close_btn =  MDFlatButton(text = 'Close', on_press = self.close_box)
        self.box = MDDialog(
            text = check_string,
            title = "Adding Device",
            size_hint = (0.5, 1),
            buttons = [close_btn])
        self.box.open() 
    
    def close_box(self, obj):
        self.box.dismiss()

MyApp().run()
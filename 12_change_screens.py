import imp
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (300, 600)

builder = '''
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'

<ProfileScreen>
    name: 'profile'
    MDLabel:
        text: 'Welcome Lesky'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
'''

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

scr_manage = ScreenManager()
scr_manage.add_widget(MenuScreen(name = 'menu'))
scr_manage.add_widget(MenuScreen(name = 'profile'))

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(builder)

MyApp().run()
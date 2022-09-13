from kivymd.uix.label import MDIcon, MDLabel
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout


kv = """
MDScreen:
    MDFloatLayout:
        ScreenManager:
            HomeScreen:
                id: home
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar: 
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: 'Navigation Drawer'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget: 
            MenuScreen:
                id: menu 
                
<HomeScreen>:
    name: 'home_screen'
    MyMDLabel:
        id: label
        text: "account on"
        pos_hint: {"center_x": .5, "center_y": .8}
        halign: "center"
        font_size: dp(20)
        theme_text_color: "Primary"
    MyMDIcon:
        id: icon
        icon: "account"
        pos_hint: {"center_x": .5, "center_y": .6}
        halign: "center"
        font_size: dp(100)
        theme_text_color: "Primary"
    MDRaisedButton:
        text: "Press"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_release:
            label.text= "account on" if label.text=="account off" else "account off"
            icon.icon= "account" if icon.icon=="account-off" else "account-off"
    MDRaisedButton:
        text: 'Next'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu_screen'

<MenuScreen>:
    name: 'menu_screen'
    MyMDLabel:
        id: label
        text: "account off"
        pos_hint: {"center_x": .5, "center_y": .8}
        halign: "center"
        font_size: dp(20)
        theme_text_color: "Primary"
    MyMDIcon:
        id: icon
        icon: "account-off"
        pos_hint: {"center_x": .5, "center_y": .6}
        halign: "center"
        font_size: dp(100)
        theme_text_color: "Primary"
    MDRaisedButton:
        text: "Press"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_release:
            label.text= "account on" if label.text=="account off" else "account off"
            icon.icon= "account" if icon.icon=="account-off" else "account-off"
            
    MDRaisedButton:
        text: 'Pre'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'home_screen'
"""

class MyMDIcon(MDIcon):
    pass


class MyMDLabel(MDLabel):
    pass


class HomeScreen(Screen):
    pass


class MenuScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home_screen'))
sm.add_widget(MenuScreen(name='menu_screen'))

class Hey(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(kv)



if __name__ == '__main__':
    Hey().run()
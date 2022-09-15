from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineIconListItem, OneLineIconListItem, MDList, IconLeftWidget
from kivy.core.window import Window
from kivy.lang import Builder
from data import icons, names, types, modes
from random import randint

Window.size = (300, 600)

loader = """
MDScreen: 
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'DEVICES'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        right_action_items: [['card-search', lambda x: app.search_btn()]]
                        elevation: 20
                        opposite_colors: True

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Add New Device'
                                IconLeftWidget:
                                    icon: 'plus'

                    MDBottomAppBar:
                        MDTopAppBar:
                            left_action_items: [['devices', lambda x: app.all_devices()],['wifi', lambda x: app.wifi_devices()], ['bluetooth', lambda x: app.bt_devices()], ['web', lambda x: app.web_devices()], ['cable-data', lambda x: app.wired_devices()], ['remote', lambda x: app.ir_devices()]]
                            opposite_colors: True
                            mode: 'free-end'
                            type: 'bottom'
                            icon: 'plus'
                            on_action_button: app.add_device()
                                
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: 'vertical'

                Image:
                    source: 'assets/images/remote.jpg'
                    size_hint: (0.25, 0.25)

                MDLabel:
                    text: 'Remote Devices'
                    halign: 'left'
                    size_hint_y: None
                    font_style: 'H6'
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Home'
                            IconLeftWidget:
                                icon: 'home'
                        
                        OneLineIconListItem:
                            text: 'Controller'
                            IconLeftWidget:
                                icon: 'controller'

                        OneLineIconListItem:
                            text: 'Devices'
                            IconLeftWidget:
                                icon: 'devices'

                MDBoxLayout:
                    orientation: 'horizontal'

                    MDIcon:
                        icon: 'account-circle'

                    MDIcon:
                        icon: 'brightness-7'
"""

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(loader)
        return screen

    def nav_draw(self):
        print("Navigation Drawer")

    def search_btn(self):
        print("Search Button")

    def add_device(self):
        print("Add New Device")

    def web_devices(self):
        print('Internet Connected Devices')
        
    def all_devices(self):
        print('All Devices')
        
    def wifi_devices(self):
        print('Wifi Devices')
        
    def bt_devices(self):
        print('Bluetooth Devices')

    def wired_devices(self):
        print('Wired Devices')
    
    def ir_devices(self):
        print("Infra-Red Devices")
        
if __name__=="__main__":
    MyApp().run()
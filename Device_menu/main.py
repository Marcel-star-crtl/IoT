from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineIconListItem, OneLineIconListItem, MDList, IconLeftWidget
from kivy.core.window import Window
from kivy.lang import Builder
from data import icons, names, types, modes
from random import randint

Window.size = (300, 600)

loader = """
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'DEVICES'
            left_action_items: [['menu', lambda x: app.nav_draw()]]
            right_action_items: [['card-search', lambda x: app.search_btn()]]
            elevation: 20
            opposite_colors: True

        ScrollView:
            MDList:
                id: container

        MDBottomAppBar:
            MDTopAppBar:
                left_action_items: [['devices', lambda x: app.all_devices()],['wifi', lambda x: app.wifi_devices()], ['bluetooth', lambda x: app.bt_devices()], ['web', lambda x: app.web_devices()], ['cable-data', lambda x: app.wired_devices()], ['remote', lambda x: app.ir_devices()]]
                opposite_colors: True
                mode: 'free-end'
                type: 'bottom'
                icon: 'plus'
                on_action_button: app.add_device()
"""

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(loader)
        return screen

    def on_start(self):
        item = OneLineIconListItem(text = 'Add New Device')
        item.add_widget(IconLeftWidget(icon = 'plus'))
        self.root.ids.container.add_widget(item)
        for x in range(18):
            i = randint(0, 17)
            icon = IconLeftWidget(icon = icons[i])
            item = ThreeLineIconListItem(
                text = names[i],
                secondary_text = types[i],
                tertiary_text = modes[randint(0, 4)]
            )
            item.add_widget(icon)
            self.root.ids.container.add_widget(item)

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
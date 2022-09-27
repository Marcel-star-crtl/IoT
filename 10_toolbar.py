from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (300, 500)

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

        MDLabel:
            text: 'Hello There'
            halign: 'center'

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
        return Builder.load_string(loader)

    def nav_draw(self):
        print("Coming Up")

    def search_btn(self):
        print("Coming Up")

    def add_device(self):
        print("Coming Up")

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
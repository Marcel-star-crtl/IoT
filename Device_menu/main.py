from kivy.lang import Builder
from kivymd.app import MDApp

class DeviceApp(MDApp):
    def build(self):
        return Builder.load_file('screens.kv')

class Device():
    def __init__(self, device_name, device_id, device_type, device_connect_mode, date_added):
        self.name = device_name
        self.id = device_id
        self.type = device_type
        self.mode = device_connect_mode
        self.date = date_added

    def addDevice(self):
        pass


DeviceApp().run()
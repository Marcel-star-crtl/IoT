from kivymd.app import  MDApp                 
from kivy.lang.builder import Builder

loader = """
MDBoxLayout:
    orientation: 'vertical'
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDTextField:
        hint_text: "Enter device name: "
        helper_text: "Enter name of device"
        helper_text_mode: "on_focus"
        pos_hint : {'center_x': 0.5,'center_y': 1.0}
        size_hint_x : None
        width: 200

    MDTextField:
        hint_text: "Enter device type: "
        helper_text: "Enter type of device"
        helper_text_mode: "on_focus"
        pos_hint : {'center_x': 0.5,'center_y': 1.0}
        size_hint_x : None
        width: 200

    MDTextField:
        hint_text: "Enter device mode: "
        helper_text: "Enter mode of device"
        helper_text_mode: "on_focus"
        pos_hint : {'center_x': 0.5,'center_y': 1.0}
        size_hint_x : None
        width: 200

    MDFloatingActionButton:
        icon: 'plus'
        on_press: Device.addDevice
        on_release: Device.showSuccessful
        pos_hint : {'center_x': 0.5,'center_y': 1.0}

    Widget:
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(loader)

class Device():
    def __init__(self, name, type, mode):
        self.name = name
        self.type = type
        self.mode = mode

    def addDevice(self, obj):
        pass

    def showSuccess(self, obj):
        close_btn =  MDFlatButton(text = 'Close', on_press = self.close_box)
        self.box = MDDialog(
            text = self.name + ' successfully added',
            title = "Adding Device",
            size_hint = (0.5, 1),
            buttons = [close_btn])
        self.box.open() 
    
    def close_box(self, obj):
        self.box.dismiss()

MainApp().run()
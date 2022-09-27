from kivymd.app import MDApp
from kivy.lang.builder import Builder

loader = """
MDBoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: "Home Devices"
        md_bg_color: app.theme_cls.primary_color

    MDBottomNavigation: # this is a fancy manager
        MDBottomNavigationItem: # This is a fancy Screen
            text: "All"
            name: "all" 
            icon: "devices"
            ScrollView:
                MDList:
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'
                    ThreeLineListItem:
                        text: 'Device Name'
                        secondary_text: 'Device Type'
                        tertiary_text: 'Mode'

        MDBottomNavigationItem: # This is a fancy Screen
            text: "WIFI"
            name: 'wifi'
            icon: "wifi"
            ScrollView:
                MDGridLayout:
                    cols: 2
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"
                    MDFlatButton:
                        text: "Device name"

        MDBottomNavigationItem: # This is a fancy Screen
            text: "BLUETOOTH"
            name: "bluetooth" 
            icon: "wifi"
            ScrollView:
                MDGridLayout:
                    cols: 2
                    
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
                    MDRectangleFlatButton:
                        text: "Device #"
"""

class MyApp(MDApp):
    def build(self):

        return Builder.load_string(loader)
if __name__=="__main__":
    MyApp().run()
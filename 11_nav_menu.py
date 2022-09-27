from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, MDList
from kivy.core.window import Window
from kivy.lang.builder import Builder

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
                        # replaced '.nav_drawer()' with '.set_state('toggle')
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 20
                        opposite_colors: True
                    
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: 'vertical'

                Image:
                    source: 'remote2.jpg'
                    size_hint: (0.3, 0.3)

                MDLabel:
                    text: 'Remote Devices'
                    halign: 'left'
                    size_hint_y: None
                    font_style: 'H6'
                    height: self.texture_size[1]

                ScrollView:
                    id: scrv

                
                MDBoxLayout:
                    orientation: 'horizontal'

                    MDIcon:
                        icon: 'account-circle'

                    MDIcon:
                        icon: 'brightness-7'
"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(loader)

    def on_start(self):
        list = MDList()
        for i in range(4):
            list.add_widget(OneLineListItem(text = 'Menu ' + str(1+i)))
        return self.root.ids.scrv.add_widget(list)

if __name__=="__main__":
    MyApp().run()
from email.mime import image
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem, ImageLeftWidget
from kivy.core.window import Window


Window.size = (300, 500)

list_helper ="""
Screen:
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: 'My House'
                left_action_items: [["menu", lambda x: app.navigation_draw()]]
                right_action_items:[["logout",lambda x: app.navigation_draw()]]
            MDList:
                id: container

"""


class DemoListApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):

        for i in range(6):
            image = ImageLeftWidget(source='./images/boy.png')
            items = TwoLineAvatarIconListItem(text='Lespa ', 
                                                secondary_text='Hello Fellow Users')
            
            items.add_widget(image)
            self.root.ids.container.add_widget(items)

        return 

    def navigation_draw(selt):
        print("Navigation")

DemoListApp().run()
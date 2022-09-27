from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem,  MDList
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.size = (300, 600)

class MyApp(MDApp):
    def build(self):
        
        # uncomment one of the two screen
        screen = Builder.load_file('list.kv')
        screen = MDScreen()
        list = MDList()
        scroll = ScrollView()

        #   Uncomment this block and comment/remove the for loop
        """
        item1 = OneLineListItem(text = "Item 1")
        item2 = OneLineListItem(text = "Item 2")
        item3 = OneLineListItem(text = "Item 3")
        item4 = OneLineListItem(text = "Item 4")
        item5 = OneLineListItem(text = "Item 5")
        item6 = OneLineListItem(text = "Item 6")

        
        list.add_widget(item1)
        list.add_widget(item2)
        list.add_widget(item3)
        list.add_widget(item4)
        list.add_widget(item5)
        list.add_widget(item6) 
        """

        for x in range(1,21):
            item = ThreeLineListItem(
                text = 'Item ' + str(x), 
                secondary_text = "This is Item #" + str(x)
                )
            list.add_widget(item)

        scroll.add_widget(list)
        screen.add_widget(scroll)
        return screen

MyApp().run()
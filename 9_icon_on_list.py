from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem, OneLineIconListItem, MDList, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.lang import Builder
from Device_menu.data import icons, names, type

Window.size = (300, 600)

class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        list = MDList()
        scroll = ScrollView()
        scroll.add_widget(list)

        for x in range(18):
            icon = IconLeftWidget(icon = icons[x])
            item = TwoLineIconListItem(
                text = names[x],
                secondary_text = type[x]
            )
            item.add_widget(icon)
            list.add_widget(item)

        addItem = OneLineIconListItem(text = "Add New Device")
        addItem.add_widget(IconLeftWidget(icon = 'plus'))
        list.add_widget(addItem)

        screen.add_widget(scroll)
        return screen

if __name__=="__main__":
    MyApp().run()
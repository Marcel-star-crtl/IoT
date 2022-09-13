from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view=MDList()
        scroll.add_widget(list_view)

        for i in range(5):
            items = TwoLineListItem(text='item ' + str(i),
                                        secondary_text='list items')
            list_view.add_widget(items)

        screen.add_widget(scroll)

        return screen

DemoApp().run()
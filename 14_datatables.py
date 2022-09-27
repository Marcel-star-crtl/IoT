import imp
from tabnanny import check
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        table = MDDataTable(
            size_hint = (0.9, 0.6),
            pos_hint = {'center_x':0.5, 'center_y':0.5},
            elevation = 50,
            rows_num = 5,
            check = True,
            column_data = [
                ('Software', dp(35)),
                ('Languages', dp(40)),
                ('Frameworks', dp(40)),
                ('IDEs', dp(40))
            ],
            row_data = [
                ('Front End', 'HTML, CSS, JavaScript', 'Bootstrap, Vue.Js', 'Dreamweaver, Webstorm'),
                ('Back End', 'PHP, SQL', '', ''),
                ('Crossplatform', 'Python, Arduino', '', 'Arduino, VScode'),
                ('Android App', 'Java, Kotlin', '', 'Android studio, IntelliJ Idea'),
                ('Front End', 'HTML, CSS, JavaScript', 'Bootstrap, Vue.Js', 'Dreamweaver, Webstorm'),
                ('Back End', 'PHP, SQL', '', ''),
                ('Crossplatform', 'Python, Arduino', '', 'Arduino, VScode'),
                ('Android App', 'Java, Kotlin', '', 'Android studio, IntelliJ Idea'),
                ('Front End', 'HTML, CSS, JavaScript', 'Bootstrap, Vue.Js', 'Dreamweaver, Webstorm'),
                ('Back End', 'PHP, SQL', '', ''),
                ('Crossplatform', 'Python, Arduino', '', 'Arduino, VScode'),
                ('Android App', 'Java, Kotlin', '', 'Android studio, IntelliJ Idea'),4
            ]
        )
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)

        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print('Current', instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print('Instance', instance_table, instance_row)

MyApp().run()
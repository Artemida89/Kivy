from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout


KV = '''

<MyGridLayout>:
    rows: 2
    id: main_win
    Dropdown:
        id: dropdown
        Button:
            id: btn1
            text: 'option 1'
        Button:
            id: btn2
            text: 'option 2'
    BoxLayout:

    BoxLayout:
        
        
        
'''

class MyGridLayout(GridLayout):
    def build(self):
        return Builder.load_string(KV)

class LayoutsApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    LayoutsApp().run()
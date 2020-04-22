from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp


root_kv = """

"""


class MyApp(MDApp):
    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MyApp().run()

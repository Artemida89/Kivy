from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Размер ОКНА
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 480)
Config.set("graphics", "height", 640)


class CalcApp(App):

    # Функция - Обновить (Обнулить результат при вводе нового)
    def update_lable(self):
        # Текст в кнопки - это часть формулы
        self.bll.text = self.formula

    # Функция для цифр
    def add_namber(self, instance):
        if (self.formula == " "):
            self.formula = ""
        # Добавить новую цифру
        self.formula += str(instance.text)

        # Если опирация совершилась. Обновить (Обнулить результат при вводе нового)
        self.update_lable()

    # Функция для опираторов
    def add_operation(self, instance):
        if( str(instance.text).lower() == "x"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)

        # Если опирация совершилась. Обновить (Обнулить результат при вводе нового)
        self.update_lable()

    # Функцыя для результата
    def calc_result(self, instance):
        self.bll.text = str(eval(self.bll.text))
        self.formula = ""

    # ОСНОВА
    def build(self):

        self.formula = ""

        # BoxLayout Бокс расположение вертикальное граница 20 везде. Внутри Результат опирации и Сама клавиатура.
        bl = BoxLayout(orientation="vertical", padding=20)
        # GridLayout - клавиатура в 4 колонки и 3 растояние между кнопак
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        # Вывод результата Калькулятора Размер и прочее
        self.bll = Label(text="0", font_size=50, halign="right", valign="center", size_hint=(1, .4),
                         text_size=(480 - 40, 640 * .4 - 40))
        bl.add_widget(self.bll)

        # 1 ряд кнопок
        gl.add_widget(Button(text="7", on_press=self.add_namber))
        gl.add_widget(Button(text="8", on_press=self.add_namber))
        gl.add_widget(Button(text="9", on_press=self.add_namber))
        gl.add_widget(Button(text="X", on_press=self.add_operation))

        # 2 ряд кнопок
        gl.add_widget(Button(text="4", on_press=self.add_namber))
        gl.add_widget(Button(text="5", on_press=self.add_namber))
        gl.add_widget(Button(text="6", on_press=self.add_namber))
        gl.add_widget(Button(text="-", on_press=self.add_operation))

        # 3 ряд кнопок
        gl.add_widget(Button(text="1", on_press=self.add_namber))
        gl.add_widget(Button(text="2", on_press=self.add_namber))
        gl.add_widget(Button(text="3", on_press=self.add_namber))
        gl.add_widget(Button(text="+", on_press=self.add_operation))

        # 4 ряд кнопок
        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", on_press=self.add_namber))
        gl.add_widget(Button(text=".", on_press=self.add_namber))
        gl.add_widget(Button(text="=", on_press=self.calc_result))

        # Клавиатура внутри Бокса
        bl.add_widget(gl)
        return bl


if __name__ in "__main__":
    CalcApp().run()
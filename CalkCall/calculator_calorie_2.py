# import kivy

from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp


class CalculatorCalories(App):
    def build(self):
        # Config.set('graphics', 'width', '350')
        # Config.set('graphics', 'height', '450')
        dropdown = DropDown()
        btn_1 = Button(text='Пюре', size_hint_y=None, height=30)
        btn_1.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn_1)
        btn_2 = Button(text='Рис', size_hint_y=None, height=30)
        btn_2.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn_2)
        btn_3 = Button(text='Греча', size_hint_y=None, height=30)
        btn_3.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn_3)
        btn_4 = Button(text='Макаронные\nизделия', size_hint_y=None, height=30)
        btn_4.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn_4)

        mainbutton = Button(text='Гарнир', size_hint=(.1, .05), pos_hint={'center_x': .07, 'center_y': .95})
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda x: setattr(mainbutton, 'text', x))
        runTouchApp(mainbutton)
        # label = Label(text='Блюдо: ',
        #               size_hint=(.5, .5),
        #               pos_hint={'center_x': .5, 'center_y': .85})
        #
        # return label
        # layout = BoxLayout()
        # btn = Button(text="Button #%s",
        #              background_color=self.blue
        #             )
        #
        # layout.add_widget(btn)
        # return layout


if __name__ == '__main__':
    app = CalculatorCalories()
    app.run()

# self.red = [1, 0, 0, 1]
# self.green = [0, 1, 0, 1]
# self.blue = [0, 0, 1, 1]
# self.purple = [1, 0, 1, 1]

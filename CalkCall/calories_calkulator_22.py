from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton


class CalculatorCalories(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        return screen


CalculatorCalories().run()

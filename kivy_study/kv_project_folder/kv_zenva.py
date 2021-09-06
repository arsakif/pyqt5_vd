# Tutorial with Zena

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()


class GameScreen(Widget):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        pass


if __name__ == '__main__':
    LanguageLearnerApp().run()

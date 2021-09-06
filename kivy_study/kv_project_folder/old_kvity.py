# Tutorial with Zena

from kivy.app import App
from kivy.uix.button import Button


class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text="some text",
            pos=(50, 50),
            size_hint=(.5, .5),
            )





if __name__ == '__main__':
    LanguageLearnerApp().run()

# ===============================================

# Tutorial with Zena

from kivy.app import App
from kivy.uix.button import Button


class LanguageLearnerApp(App):
    def build(self):
        # return FunkyButton(
        #     text='sdfsdf',
        #     pos=(100, 100),
        #     size_hint=(.5, .5)
        #     )
        return FunkyButton()


class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text = "Rezzan's Button"
        self.pos = (100, 100)
        self.size_hint = (.5, .5)


if __name__ == '__main__':
    LanguageLearnerApp().run()

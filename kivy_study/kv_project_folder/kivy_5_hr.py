from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayoutExample, self).__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text='Button-1')
        b2 = Button(text='Button-2')
        b3 = Button(text='Button-3')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)


class TheLabApp(App):
    pass


class MainWidget(Widget):
    pass


# if __name__ == '__name__':
TheLabApp().run()

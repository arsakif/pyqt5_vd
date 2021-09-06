from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class WidgetExample(GridLayout):
    c = 0
    my_text = StringProperty('Rezzan-' + str(c))
    def on_button_click(self):
        self.c += 1
        self.my_text = 'Rezzan-' + str(self.c)


class BoxLayoutExample(BoxLayout):
    pass
    """ def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text="Akif")
        b2 = Button(text="Rezzan")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3) """


class AnchorLayoutExample(AnchorLayout):
    pass
    """ def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text="Akif")
        b2 = Button(text="Rezzan")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3) """


class GridLayoutExample(GridLayout):
    pass
    """ def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text="Akif")
        b2 = Button(text="Rezzan")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3) """


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spacing = (dp(20), dp(20))
        for i in range(1, 100):
            sz = dp(100)
            b = Button(text=f'Rez-{str(i)}', size_hint=(None, None),
                       size=(sz, sz))
            self.add_widget(b)


class TheLabApp(App):
    pass


class MainWidgetExample(Widget):
    pass


# if __name__ == '__name__':
TheLabApp().run()

from kivy.app import App

from MyWindow import MyWindow


class OthelloApp(App):
    def build(self,**kwargs,):
        super().__init__(**kwargs)
        self.root = MyWindow()
        return self.root


if __name__ == '__main__':
    OthelloApp().run()
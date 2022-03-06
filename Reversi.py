from kivy.app import App

from AllOfParts.MyWindow import MyWindow


class ReversiApp(App):
    def build(self,**kwargs,):
        
        super().__init__(**kwargs)
        self.root = MyWindow()
        return self.root


if __name__ == '__main__':
    ReversiApp().run()
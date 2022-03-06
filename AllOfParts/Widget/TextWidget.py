from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.label import Label

class TextWidget(Label):
    def __init__(self, widget_size,**kwargs):
        super().__init__(**kwargs)
        
        self.widget_size = widget_size
       
        self.markup = True
        self.text="Start!"
        self.font_size = 50
        self.size = self.widget_size
        """
        with self.canvas:
                Color(0,0,0,1)
                Rectangle(size=self.widget_size,pos=self.pos)
            self.color=(1,1,1,1)
        """
        
        

    def print_turn(self,turn):
        if(turn):
            self.text="Black"
            
        else:
            self.text="White"
            
            
            

        

    def print_winner(self,winner):
        if winner:
            self.text="Player1\nWin!"
        else:self.text="Player2\nWin!"

    

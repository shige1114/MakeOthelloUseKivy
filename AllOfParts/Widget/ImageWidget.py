from kivy.uix.image import Image

class ImageWidget(Image):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.image_list = dict()
        self.image_list["Start"]="/"
        self.image_list["White"]="/"
        self.image_list["Black"]="/"
        self.image_list["BlackWinner"]="/"
        self.image_list["WhiteWinner"]="/"

       
        
        
    def change_turn_image(self,turn):
        
        if turn:
            self.source = self.image_list["Black"]
        else:
            self.source = self.image_list["White"]
        pass
    def change_action_image(self,turn):
        if turn:
            self.source = self.image_list["BlackAction"]
        else:
            self.source = self.image_list["WhiteAction"]
        pass
    def winner_image(self,turn):
        
        if turn:
            self.source = self.image_list["BlackWinner"]
        else:
            self.source = self.image_list["WhiteWinner"]
        pass
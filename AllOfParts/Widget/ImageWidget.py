from kivy.uix.image import Image
import os


class ImageWidget(Image):
    
    def __init__(self, widget_size, **kwargs):
        super().__init__(**kwargs)
        self.size = widget_size
        self.image_list = dict()
        
        self.image_list["Start"]=None
        self.add_dict(file="WhiteDefault")
        self.add_dict(file="BlackDefault")
        self.add_dict(file="Start")
        self.source = self.image_list["Start"]
        self.image_list["Black"]=None
        
        self.add_dict("BlackWin")
        self.add_dict("WhiteWin")

       
        
        if not os.path.exists(self.image_list["WhiteDefault"]):print("error")
        
    def change_turn_image(self,turn):
        
        if turn:
            self.source = self.image_list["BlackDefault"]
        else:
            self.source = self.image_list["WhiteDefault"]
        
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

    def procing_path(self,file):
        return os.path.join("AllOfParts","Widget","ImageList",file)

    def add_dict(self,**args):
        """
        args {file}
        return {None}
        """
        self.image_list[args["file"]] = self.procing_path(args["file"]+".png")

    def start_faze(self):
        self.source = self.image_list['Start']

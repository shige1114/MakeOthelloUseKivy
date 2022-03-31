from kivy.uix.image import Image
import os


class ImageWidget(Image):
    
    def __init__(self, widget_size, **kwargs):
        super().__init__(**kwargs)
        self.size = widget_size
        self.image_list = dict()
        self.image_list["Test"] = self.procing_path("test.png")
        self.image_list["Start"]=None
        self.add_dict(file="WhiteDefault")
        self.image_list["Black"]=None
        self.image_list["BlackDefault"] = self.image_list["WhiteDefault"]
        self.image_list["BlackWinner"]=None
        self.image_list["WhiteWinner"]=None

       
        
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

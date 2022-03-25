
from kivy.uix.image import Image
import os

class ImageWidget(Image):

    def __init__(self,  widget_size,**kwargs):
        super().__init__(**kwargs)
        self.image_list = dict()
        self.allow_stretch = True
        self.keep_ratio = False

        self.image_list["start_image"] = None
        self.source = self.image_list["start_image"]

    def change_image_def(self,**args):
        if args["turn"]==True:self.source = self.image_list["p1_def"]
        else:self.source = self.image_list["p2_def"]

    def change_image_action(self,**args):
        if args["turn"]==True:self.source = self.image_list["p1_action"]
        else:self.source = self.image_list["p2_action"]

    def processing_path(self,**args):
        return os.path.join("Widget","image",args["file"])

    
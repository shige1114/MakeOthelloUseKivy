from pygame import mixer

import time
import os

SLEEP_TIME = time.sleep(4)
class MV:
    def __init__(self):
        self.mv = mixer

        self.music_list = dict()
        self.music_list = {"test":self.processing_path(file="test.mp3")}
        print(self.music_list["test"])
        super().__init__()
    
    
    def make_sound(self,**args):
        """
        args {turn,}
        retun {None}
        """
        if(args["turn"]):
            self.mv.init()
            self.mv.music.load(self.music_list["test"])
            self.mv.music.play(1)
            SLEEP_TIME

        else:
            self.mv.init()
            self.mv.music.load(self.music_list["test"])
            self.mv.music.play(1)
            SLEEP_TIME
    
    def processing_path(self,**args):
        return os.path.join("ControllMV","music_list",args["file"])
            


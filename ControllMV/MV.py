from pygame import mixer

import time
import os

SLEEP_TIME = time.sleep(1)
class MV:
    def __init__(self):
        self.mv = mixer

        self.music_list = dict()
        self.music_list = {"test":self.processing_path(file="test.mp3")}
        self.add_dict()


        print(self.music_list["test"])
        super().__init__()
    
    def start_sound(self,**args):
        self.make_sound(sound=self.music_list["start"])
        pass

    def action_sound(self,**args):

        if(args["turn"]):
            self.make_sound(self.music_list[""])

        else:
            self.make_sound(self.music_list[""])
            
    def make_sound(self,**args):
        """
        args {file}
        retun {None}
        """
        self.mv.init()
        self.mv.music.load(args["file"])
        SLEEP_TIME
        pass
    
    def add_dict(self,**args):
        """
        args {file}
        return {None}
        """
        self.music_list[args["file"]] = self.processing_path(args["file"])
    
    def processing_path(self,**args):
        return os.path.join("ControllMV","MusicList",args["file"])
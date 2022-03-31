from kivy.event import EventDispatcher

class ControllEvent(EventDispatcher):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_change_image')  # 1

    def on_change_image(self, *args, **kwargs):
        
        pass
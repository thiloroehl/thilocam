'''
Created on 13.09.2016

@author: Thilo
'''

from kivy.uix.video import Video
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import videoplayer
from kivy.core.video import Video



class ThiloVideoApp(App):
    def  update (self,dt):
        self.load_next()
    
    def build(self):
        self.title="Thilo Cam"

        # Create the screen manager
        sm = ScreenManager()
        ms =MenuScreen(name='menu')
        sm.add_widget(ms)
        
        sm.add_widget(SettingsScreen(name='settings'))
        
        return sm
        
    #def build(self):
    #    self.v = Video(source="http://192.168.1.199/mjpg/1/video.mjpg", state='play')
    #    self.v.bind(state=self.replay)
    #    return self.v

    def replay(self, *args):
        if self.v.state == 'stop':
            self.v.state = 'play'

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
            
if __name__ == '__main__':
    ThiloVideoApp().run()
    


             
    
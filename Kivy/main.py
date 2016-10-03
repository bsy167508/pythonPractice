from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):
    def validation(self):
        pass

class Root(BoxLayout):
    pass

class DisplayApp(App):
    pass

if __name__=='__main__':
    DisplayApp().run()
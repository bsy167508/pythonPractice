from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<LoginScreen>:
    id: loginscreen
    uname: unameinput
    passw: passinput
    action: loginbutton
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            id: bottombox
            size_hint_y: 0.40
        
        BoxLayout:
            id: focus
            size_hint_y: 0.15
            
            BoxLayout:
                id: sidebox1
                size_hint_x: 0.15
            
            BoxLayout:
                id:middlebox
                orientation: 'vertical'
                size_hint_x:0.70
                canvas.before: 
                    Color: 
                        rgb: 0.6, 0.6, 0.6
                    Rectangle:
                        size: self.size
                        pos: self.pos
                            
                BoxLayout:
                    id: unamebox
                    Label:
                        id:unamelabel
                        text: 'Username : '
                    TextInput:
                        id:unameinput
                        
                BoxLayout:
                    id: passbox
                    
                    Label:
                        id:passlabel
                        text: 'Password : '
                    TextInput:
                        id:passinput
                        password:True
                        
                Button:
                    id: loginbutton
                    text: 'Login'
                    on_press: loginscreen.validation()
                    
                    
                       
                        
            BoxLayout:
                id:sidebox2
                size_hint_x:0.15
                
        BoxLayout:
            id: bottombox
            size_hint_y: 0.45

<Dashboard>:
    BoxLayout:
        Label:
            text: 'Hello'
""")


class LoginScreen(Screen):
    
    def validation(self):
        if self.action.text=='Login':
            if self.uname.text=='ahm.rimer' and self.passw.text=='password':
                    sm.switch_to(Dashboard(name='screen 2'))
            else:
                    self.action.text='Wrong credentials, click to try again.'
        else:
            self.uname.text=''
            self.passw.text=''
            self.action.text='Login'
            
class Dashboard(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='screen 1'))
sm.add_widget(Dashboard(name='screen2'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
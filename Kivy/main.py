from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from samba.dcerpc.dcerpc import auth
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

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
                        rgba: 0.1, 0.2, 0.3, 1
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
                        multiline: False
                        
                BoxLayout:
                    id: passbox
                    
                    Label:
                        id:passlabel
                        text: 'Password : '
                    TextInput:
                        id:passinput
                        password:True
                        multiline: False
                        
                Button:
                    id: loginbutton
                    text: 'Login'
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.3, 0.4, 1
                            Rectangle:
                                size: self.size
                    on_press: loginscreen.validation()
                    
                    
                       
                        
            BoxLayout:
                id:sidebox2
                size_hint_x:0.15
                
        BoxLayout:
            id: bottombox
            size_hint_y: 0.45

<Dstudent>:
    id: dstudent
    BoxLayout:
        BoxLayout:
            size_hint_x: 0.10
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.80
            padding: [25, 70, 25, 70]
            spacing: 30
            BoxLayout:
                Label: 
                    text: 'Name'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: nameinput
            BoxLayout:
                Label:
                    text: 'Entry No.'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: entryinput
            BoxLayout:
                Label:
                    text: 'Branch'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: branchinput
            BoxLayout:
                Label:
                    text: 'Year of Passing (DD:MM:YYYY)'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: yopinput
            BoxLayout:
                Label:
                    text: 'Address'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: addressinput
            BoxLayout:
                Label:
                    text: 'Subjects'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                BoxLayout:
                    TextInput:
                        id: subjectinput1
                    TextInput:
                        id: subjectsinput2
                    TextInput:
                        id: subjectsinput3
                
            BoxLayout:
                Label:
                    text: 'Marks'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                BoxLayout:
                    TextInput:
                        id: marksinput1
                    TextInput:
                        id: marksinput2
                    TextInput:
                        id: marksinput3
            
                    
        BoxLayout:
            size_hint_x: 0.10
    
        

<Dadmin>:
    id: dadmin
    BoxLayout:
                    
            
<Loginprompt>
    id: loginprompt
    BoxLayout:
        orientation: 'vertical'
        canvas.before: 
            Color: 
                rgb: 0.6, 0.6, 0.6
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            id: logoimage
            source: 'jklogo1.png'
            size_hint_y: 0.32
        BoxLayout:
            id: middlebox
            size_hint_y:0.34
            BoxLayout:
                size_hint_x: 0.2
            Button:
                id: studentlogin
                size_hint_x: 0.6
                text: 'Student Login'
                font_size: 50
                on_press: loginprompt.slogin('studentlogin')
            BoxLayout:
                size_hint_x:0.2
        BoxLayout:
            id: middlebox
            size_hint_y:0.34
            BoxLayout:
                size_hint_x: 0.2
            Button:
                id: adminlogin
                size_hint_x: 0.6
                text: 'Admin Login'
                font_size: 50
                on_press: loginprompt.slogin('adminlogin')
            BoxLayout:
                size_hint_x:0.2
""")
class Loginprompt(Screen):
    def __init__(self, **kwargs):
        super(Loginprompt, self).__init__(**kwargs)
        
    def slogin(self, id):
        print id
        if id=='adminlogin':
            sm.switch_to(LoginScreen(auth='admin'))
        if id=='studentlogin':
            sm.switch_to(LoginScreen(auth='student'))


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        if 'auth' in kwargs:
            self.auth=kwargs['auth']
            
        
    def validation(self):
        if self.auth=='student':
            if self.action.text=='Login':
                if self.uname.text=='bsy167508' and self.passw.text=='password':
                    sm.switch_to(Dstudent(name='screen 3'))
                else:
                    self.action.text='Wrong credentials, click to try again.'
            else:
                self.uname.text=''
                self.passw.text=''
                self.action.text='Login'
        else:
            if self.action.text=='Login':
                if self.uname.text=='ahm.rimer' and self.passw.text=='password':
                    sm.switch_to(Dadmin(name= 'screen 4'))
                else:
                    self.action.text='Wrong credentials, click to try again.'
            else:
                self.uname.text=''
                self.passw.text=''
                self.action.text='Login'
        
            
class Dstudent(Screen):
    def __init__(self, **kwargs):
        print 'admin'
        super(Dstudent, self).__init__(**kwargs)
        
            
class Dadmin(Screen):
    def __init__(self, **kwargs):
        super(Dadmin, self).__init__(**kwargs)
        


sm = ScreenManager()
sm.add_widget(Loginprompt(name='screen 1'))
sm.add_widget(LoginScreen(name='screen 2'))
sm.add_widget(Dstudent(name='screen 3'))
sm.add_widget(Dadmin(name='screen 4'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
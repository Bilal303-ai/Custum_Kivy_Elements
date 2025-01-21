# Custum_Kivy_Elements
This repo contains the custum kivy elements. 

## 1. Circular Icon Button
CircularIconButton class implements a circular buttons for icons. The button supports toggle behaviour. I have added four new properties:

**(1) bg_color_normal:** Color of the button when it is in OFF state.

**(2) bg_color_active:** Color of the button when it is in ON state.

**(3) img_source:** The path to the icon image. 

**(4) rad:** Radius of the button.

https://github.com/user-attachments/assets/9aec5352-1cef-4b01-bfb1-c446db4ec57b

## Code for the app shown in above video:

**Step 1:** Download the file named circular_icon_button.py.

**Step 2:** Create a new file and copy the following snippet into it and run it.

```
from circular_icon_button import CircularIconButton
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''  
<RootWidget>:
    rad: 50
    bg_color_normal: [102/255, 79/255, 161/255, 1]
    bg_color_active: [1, 0, 0, 1]
    img_source: "mic.png" #Replace this with the path to your image
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
'''                   
)

class RootWidget(CircularIconButton):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
```


if __name__ == "__main__":
    MainApp().run()

## 2. Rounded Button
  RoundedButton class implements a rounded corner button. I have added two new properties:
  
**(1) bg_color:** This lets you give a color to the button.

**(2) rad:** This lets you adjust the border radius.


https://github.com/user-attachments/assets/362eae79-c4f3-4f99-b1c8-bcf10f9f60c6

  
## Code for the app shown in above video:

**Step 1:** Download the file named rounded_button.py.

**Step 2:** Create a new file and copy the following snippet into it and run it.

```
from rounded_button import RoundedButton
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    canvas.before:
        Color:
            rgba: [247/255, 242/255, 250/255]

        Rectangle:
            size: self.size
            pos: self.pos    
    RoundedButton:
        rad: 50
        bg_color: [102/255, 79/255, 161/255, 1]
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: (0.8, 0.1)
        text: "Rounded Button"
        font_size: 25'''                   
)

class RootWidget(FloatLayout):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
```

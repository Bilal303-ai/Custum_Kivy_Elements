from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.core.image import Image as CoreImage

class CircularIconButton(ToggleButton):
    bg_color_normal = ListProperty([1, 0, 0, 0.5])
    """Contains the background color of the button when it is inactive
    """
    
    bg_color_active = ListProperty([1, 0, 0, 1])
    """Contains the background color of the button when t is active
    """
    
    rad = NumericProperty(50)
    """Radius of the button
    """
    
    img_source = StringProperty("")
    """Contains the source of the image
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.background_normal = ''
        self.background_down = ''  
        self.size_hint = (None, None)
        self.size = (self.rad * 2, self.rad * 2)
        
        with self.canvas.before:
            self.color_instruction = Color(*self.bg_color_normal)
            self.circ = Ellipse(pos=self.pos, size=self.size)
            
            #Placeholders for image
            self.img_texture = None
            self.img_rect = None
            
            if self.img_source:
                self._update_img_texture()
                
        self.bind(
            pos=self._update_circ, 
            size=self._update_circ, 
            rad=self._update_circ,
            bg_color_normal=self._update_color,
            bg_color_active=self._update_color,
            img_source=self._update_img_texture
            )
        
    def _update_circ(self, *args):
        self.circ.pos = self.pos
        self.circ.size = (self.rad * 2, self.rad * 2)
        
        if self.img_source:
            self._update_img_texture()
        
        
    def _update_color(self, *args):
        self.color_instruction.rgba = self.bg_color_normal
        self.bg_color_active = self.bg_color_active
        
    def _update_img_texture(self, *args):
        if self.img_source:
            self.img_texture = CoreImage(self.img_source).texture
            #Remove old rectangle
            if self.img_rect:
                self.canvas.before.remove(self.img_rect)
            #Define the rectangle to place the image
            margin = self.width / 4
            img_size = (self.width / 2, self.height / 2)
            with self.canvas.before:
                self.img_rect = Rectangle(
                    texture=self.img_texture, 
                    size=img_size, 
                    pos=(self.x + margin, self.y + margin)
                )
        
    def on_press(self, *args):
        if self.state == "down":
            self.color_instruction.rgba = self.bg_color_active
        else:
            self.color_instruction.rgba = self.bg_color_normal

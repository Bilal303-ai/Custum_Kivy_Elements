from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Color, Line, Ellipse, Rectangle
from kivy.core.image import Image as CoreImage
from kivy.graphics.vertex_instructions import RoundedRectangle

class CompoundButton(Widget):
    
    bg_color = ListProperty([1, 0, 0, 1])
    """Contains the backgorund color of an inactive button
    """
    border_color = ListProperty([1, 1, 1, 1])
    """Border color of the compound button
    """
    total_width = NumericProperty(1000)
    """Total width of the compound button
    """
    total_height = NumericProperty(250)
    """Total height of the compound button
    """
    rad = NumericProperty(50)
    """Radius of the corners of the compound button
    """
    
    border_width = NumericProperty(10)
    """Width of the border
    """
    icon_sources = ListProperty(["", "", ""])
    """Contains the paths (strings) to the icons. Icons will be rendered from left to right. 
    There should be exactly three items in the list.
    """

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (self.total_width, self.total_height)
        with self.canvas.before:
            self.bg_color_instruction_rect = Color(*self.bg_color)
            self.rect = RoundedRectangle(
                pos=(self.x, self.y + 0.25 * self.total_height),
                size=(self.total_width, 0.5 * self.total_height),
                radius=[self.rad]
            )
            
        with self.canvas:
            self.border_color_instruction_rect = Color(*self.border_color)
            self.border_line_rect = Line(
                rounded_rectangle=(
                    self.x, 
                    self.y + 0.25 * self.total_height, 
                    self.total_width, 
                    0.5 * self.total_height, 
                    self.rad
                    ),
                width=self.border_width
            )
            
        with self.canvas.after:
            self.bg_color_instruction_circ = Color(*self.bg_color)
            self.circ = Ellipse(
                pos=(self.center_x- self.total_height * 0.5, self.center_y),
                size=(self.total_height * 0.5, self.total_height * 0.5)
            )
            
        with self.canvas.after:
            self.border_color_instruction_circ = Color(*self.border_color)
            self.border_line_circ = Line(
                circle=(
                    self.center_x,
                    self.center_y,
                    self.total_height * 0.5
                ),
                width=self.border_width
            )
        self.left_icon_rect = None
        self.middle_icon_rect = None
        self.right_icon_rect = None
            
        self.put_icons()
            
            
            
        self.bind(
            pos=self._update_graphics,
            size=self._update_graphics,
            rad=self._update_graphics,
            total_width=self._update_graphics,
            total_height=self._update_graphics,
            border_width=self._update_graphics,
            bg_color=self._update_colors,
            border_color=self._update_colors,
            )
        
        self.bind(
            icon_sources=self.put_icons
        )
        
    def _update_graphics(self, *args):
        self.rect.pos = (self.x, self.y + 0.25 * self.total_height)
        self.rect.size = (self.total_width, 0.5 * self.total_height)
        self.rect.radius = [self.rad]
        self.border_line_rect.rounded_rectangle = (
            self.x,
            self.y + 0.25 * self.total_height,
            self.total_width, 0.5 * self.total_height,
            self.rad
            )
        self.circ.pos = (self.center_x- self.total_height * 0.5, self.y)
        self.circ.size = (self.total_height, self.total_height)  
        self.border_line_circ.circle = (
            self.center_x,
            self.center_y,
            self.total_height * 0.5
        )
        
        self.put_icons()
            
        
    def _update_colors(self, *args):
        self.bg_color_instruction_rect.rgba = self.bg_color
        self.bg_color_instruction_circ.rgba = self.bg_color
        self.border_color_instruction_rect = self.border_color
        self.border_color_instruction_circ = self.border_color
        
    def put_icons(self, *args):
        icon_dim = (3 * self.total_height * 0.5 / 4) # 3/4 of the width of the rectangle
        icon_size = (icon_dim, icon_dim)
        
        if self.icon_sources[0]:
            left_icon_pos = (self.x + ((self.total_width / 2 - self.height / 2) / 2 - icon_dim /2), 
                        self.y + self.total_height / 2 - icon_dim /2)
            left_icon_texture = CoreImage(self.icon_sources[0]).texture
                    
            if self.left_icon_rect:
                self.canvas.after.remove(self.left_icon_rect)
                    
            with self.canvas.after:
                Color(1, 1, 1, 1)
                self.left_icon_rect = Rectangle(
                    pos=left_icon_pos,
                    size=icon_size,
                    texture=left_icon_texture
                )
        if self.icon_sources[1]:
            middle_icon_pos = (self.x + (self.total_width / 2 - icon_dim /2), 
                        self.y + self.total_height / 2 - icon_dim /2)
                    
            middle_icon_texture = CoreImage(self.icon_sources[1]).texture
            
            if self.middle_icon_rect:
               self.canvas.after.remove(self.middle_icon_rect)
                    
            with self.canvas.after:
                self.middle_icon_rect = Rectangle(
                    pos=middle_icon_pos,
                    size=icon_size,
                    texture=middle_icon_texture
                )
                
        if self.icon_sources[2]:
            right_icon_pos = (self.x + self.width - ((self.total_width / 2 - self.height / 2) / 2 + icon_dim /2),
                        self.y + self.total_height / 2- icon_dim /2)
                    
            right_icon_texture = CoreImage(self.icon_sources[2]).texture
            
            if self.right_icon_rect:
                self.canvas.after.remove(self.right_icon_rect)
                    
            with self.canvas.after:
                self.right_icon_rect = Rectangle(
                    pos=right_icon_pos,
                    size=icon_size,
                    texture=right_icon_texture
                )
                
            
    

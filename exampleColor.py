'''
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
  Name    : exampleColor.py
  Author  : Eric Araro
  Notice  : MIT Licence
  Date    : 01/04/2022
  Version : 1.0
  Notes   : Example code for colors and styles to use in ubuntu prompt, print().
'''

import color

# Code example to use colors in ubuntu prompt with Python
## You can use any color and style of color.py file
print("This is an example to use colors in ubuntu prompt with Python")
print("-------------------------------------------------------------")

# Normal Text
print(color.red + "This is a red normal text" + color.reset_color)

# Bold Text
print(color.greenb + "This is a green bold text" + color.reset_color)

# Dim Text
print(color.yellowd + "This is a yellow dim text" + color.reset_color)

# Italic Text
print(color.bluei + "This is a blue italic text" + color.reset_color)

# Underline Text
print(color.magentau + "This is a magenta underline text" + color.reset_color)

# Blinking Text
print(color.cyanbl + "This is a cyan blinking text" + color.reset_color)

# Reverses text and background colors 
print(color.whiter + "This is a white reverse text" + color.reset_color)

# Hidden Text
print(color.blackh + "This is a black hidden text" + color.red + "<----- This is a black hidden text, you can copy/paste" + color.reset_color)

# Strikethrough Text
print(color.greens + "This is a green strikethrough text" + color.reset_color)

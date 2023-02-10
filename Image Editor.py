import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO 

def update_image(original, blur, contrast, emboss, contour, flipx, flipy):
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(Image.CONTOUR())
    
    if flipx:
        image = ImageOps.mirror(image)
        
    if flipy:
        image = ImageOps.flip(image)
    
    bio = BytesIO()
    image.save(bio, format = 'PNG')

    window['-IMAGE-'].update(data = bio.getvalue())

image_path = "Test.png"

control_col = sg.Column([
    [sg.Frame('Blur', layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-BLUR-')]])],
    [sg.Frame('Contrast', layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-CONTRAST-')]])],
    [sg.Checkbox('Emboss', key = '-EMBOSS-'), sg.Checkbox('Contour', key = '-CONTOUR-')],
    [sg.Checkbox('Flip x', key = '-FLIPX-'), sg.Checkbox('Flip y', key = '-FLIPY-')],
    [sg.Button('Save image', key = '-SAVE-')]
])
image_col = sg.Column([[sg.Image(image_path, key = '-IMAGE-')]])
layout = [[control_col, image_col]]

original = Image.open(image_path)
window = sg.Window('Image Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    update_image(
        original,
        values['-BLUR-'],
        values['-CONTRAST-'],
        values['-EMBOSS-'],
        values['-CONTOUR-'],
        values['-FLIPX-'],
        values['-FLIPY-'],
    )

window.close()
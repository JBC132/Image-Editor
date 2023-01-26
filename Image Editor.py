import PySimpleGUI as sg

control_col = sg.Column([
    [sg.Frame('Blur', layout = [[sg.Slider(range = (0,10), orientation = 'h')]])],
    [sg.Frame('Contrast', layout = [[sg.Slider(range = (0,10), orientation = 'h')]])],
    [sg.Checkbox('Emboss', key = '-EMBOSS-'), sg.Checkbox('Contour', key = '-CONTOUR-')],
    [sg.Checkbox('Flip x', key = '-FLIPX-'), sg.Checkbox('Flip y', key = '-FLIPY-')],
    [sg.Button('Save image', key = '-SAVE-')]
])
image_col = sg.Column([[sg.Image('test.png')]])

layout = [[control_col, image_col]]

window = sg.Window('Image Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
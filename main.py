import PySimpleGUI as sg      

button_text = ('Space', 'Ground', 'Telem')

def TextButton(text): 
    return sg.Text(text, key=('-B', text), relief='raised', enable_events=True, font='_ 15',text_color='white', background_color='black')

layout1 = [[sg.Text('Space')],
           *[[sg.CB(f'Checkbox {i}')] for i in range(3)]]

layout2 = [[sg.Text('Ground')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('Telem')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(3)]]


layout = [ [ TextButton(text) for text in button_text],
          [sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible = False, key='-COL2-'),sg.Column(layout3, visible = False, key='-COL3-')],
          [sg.Exit()]
          ]

window = sg.Window('Command suite 0.0.1', layout)    
layout = 1
while True: 
    event, values = window.read()
    if event in (None, 'Exit'):
        break
#TODO: onclick, make that layout true and the others false 
    if event in button_text:
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()



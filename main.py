import PySimpleGUI as sg      
# TODO: create skelton code
layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()
# file test 
text_input = values[0]    
sg.popup('You entered', text_input)


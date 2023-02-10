import speedtest as spdt
import PySimpleGUI as sg

# Green & tan color scheme      
sg.theme('GreenTan')      
index = 0

## ---------------------------------------------------- ##
## Função que pega as informações de velocidade da rede ##
## ---------------------------------------------------- ## 
def speed():
    test = spdt.Speedtest()
    
    download = test.download()
    upload = test.upload()
    ping = test.results.ping

    return f'\n\nDownload speed: {download / 1024 / 1024:.2f} Mbit/s \n\nUpload speed: {upload / 1024 / 1024:.2f} Mbit/s \n\nPing: {ping} ms'
## Fim

layout = [[sg.Text('Network information')],
          [sg.Output(size=(50,9), key='-OUTPUT-')],         
          [sg.Button('Start'), sg.Button('Exit')]]

window = sg.Window('Speedtest - Python', layout, element_justification='c', size=(300, 250))

while True:
        
    event, values = window.read()
        
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event.startswith('Start'):
        index += 1

    if index > 0:
        window['-OUTPUT-'].update('')            
        print(speed())

    index += 1     

window.close()

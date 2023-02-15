'''
import string

LC= string.ascii_lowercase
UC= string.ascii_uppercase
Nom= string.digits
import PySimpleGUI as sg
sg.theme('black')
layc=[
        [sg.Checkbox('Lower Case', default=True), sg.Checkbox('Upper Case'), sg.Checkbox('Number'), sg.Checkbox('Symbol',disabled=True)],
        [sg.Text('Max Length:\t\t\t  '), sg.Spin([i for i in range(1,8)], initial_value=4, size=(15,5))],
        [sg.Button('Generate Sample Space',button_color=('White','Grey'),size=('44','1'),font=(10,14,))],]
layr=[
      [sg.Checkbox('ENGLISH DICTIONARY', default=True,key='ENG'),], #sg.Checkbox('Upper Case'), sg.Checkbox('Number'), sg.Checkbox('Symbol',disabled=True)],
      [sg.Text('Max Length:\t\t\t  '), sg.Spin([i for i in range(1,8)], initial_value=4, size=(15,5))],
      [sg.Button('Generate',button_color=('White','Grey'),size=('44','1'),font=(10,14,))],]
layout=[[sg.TabGroup([[sg.Tab('Ready', layr),sg.Tab('Custom', layc,)]])],#disabled=True
        ]
window = sg.Window('Choose Sample Space', layout,size=(385,170),keep_on_top=True,resizable=True,)#no_titlebar=True,element_justifaction='Center'
while True:
        event, values = window.read()
        print(event)
        print(values)
        if values[6]=='Ready':
            pass
        else:
            if values[0] == False and values[1] == False and values[2] == False and values[3] == False :#and values[4] == False
                sg.PopupTimed('Error\nPlease Choose at least one option.',auto_close_duration=5,no_titlebar=True,keep_on_top=True)
            else:
                if event!='Generate' and event!='Generate Sample Space':
                    print('x')
                    #exit()
                SS=''
                if values[0]:
                    SS+=LC
                if values[1]:
                    SS+=UC
                if values[2]:
                    SS+=Nom
                #if values[3]:
                #    FN+=Sym
                LENGTH= values[4]
                if type(LENGTH)!=int or int(LENGTH) < 1:
                    sg.Popup('Length Should Be Upper Than 0 and Integer.',keep_on_top=True)
                elif int(LENGTH) > 8:
                    sg.Popup('Password Length Can Not Be Higher Than 20.',keep_on_top=True)
'''

'''password='mzz'
xxx=rx.record()
import itertools
Letters='abcde'#fghijklmnopqrstuvwxyz

WordsTuple+=itertools.product(Letters, repeat=4)
All=[]
new=''
for tpl in WordsTuple:
    for i in range(len(tpl)):
        new+= tpl[i]
        All.append(new)
    new=''
All=set(All)
print(xxx.lap())
#print(All)
print(len(All))'''


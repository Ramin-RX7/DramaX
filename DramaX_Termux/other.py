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







# HD in PC
    """
     # Reading Word Files
     ENGLISH= rx.read('./HD/english.txt').split('\n')
     ENGLISH_MORE= rx.read(f'./HD/english_more.txt').split('\n')
     ###
     TenK_MCP= rx.read('./HD/10k mcp.txt').split('\n')
     
 
     rx.cls()
     rx.style.print('''
                         88  88    db    .dP"Y8 88  88
                         88  88   dPYb   `Ybo." 88  88
                         888888  dP__Yb  o.`Y8b 888888
                         88  88 dP"" ""Yb 8bodP' 88  88
 
      8888b.  888888  dP""b8 88""Yb d88   88b 88""Yb 888888  dP"Yb  88""Yb
       8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   dP   Yb 88__dP
       8I  dY 88""   Yb      88"Yb     l8l    88"" "    88   Yb   dP 88"Yb 
      8888Y"  888888  YboodP 88  Yb    d8b    88       88    YbodP  88  Yb
      ''','gold_3b')
     # cfa5301358b9fcbe7aa45b1ceea088c6
     # a1b7f6c7d739aa48d5dfaacf54df3994S
     HASH= input('Enter Hashed String:  ')
     
     if HASH in ('99','x'):
         MAIN()
     print('\nRecognizing Hash Type...')
     if len(HASH) in (40,56,64,96,128,32):
         if len(HASH) == 32:
             mi='1'
         if len(HASH) == 40:
             mi='2'
         if len(HASH) == 56:
             mi='3'
         if len(HASH) == 64:
             mi='4'
         if len(HASH) == 96:
             mi='5'
         if len(HASH) == 128:
            mi='6'
         print('Found.  (',end='')
         rx.style.print(str(dichash[mi]),'green',end='')
         print(')\n')
     else:
        ce('Couldnt Recognize the Hash Type.\n','light_red')
        return True
 
     #SS= input('Choose Sample Space: \n1- ENGLISH DICTIONARY\n2- NUMBERS\n>')
     def CSS(*ss):
 
         import win32console
         _stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
         def input_def(prompt, default='T'):
             keys = []
             for c in default:
                 evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
                 evt.Char = c
                 evt.RepeatCount = 1
                 evt.KeyDown = True
                 keys.append(evt)
 
             _stdin.WriteConsoleInput(keys)
             return input(prompt)
 
         print('Choose Sample Space:')
         lst=[]
         for item in ss:
             #if item is SS[1]
             lst.append(bool(input_def(item+': ')))
         return lst
     SS= CSS('ENGLISH DICTIONARY','More on ENG DICT','10K MOST COMMON PASSWORDS','NUMBERS')
     WORDS=[]
     if SS[3]:
         try:     
             rang= int(input('Type Last Number: '))
         except:  
             ce('Number Should be Integer')
             return True
             
     #find=False
     if mi=='1':
         find=False
         if SS[0]:
             WORD=rx.read(f'./HD/ENG/eh_md5.txt')
             WORDS+= WORD.split('\n')
             ENGLISH_LST= ENGLISH
             if SS[1]:
                 WORDS+=rx.read(f'./HD/ENG/MORE/ehm_md5.txt').split('\n')
                 #global ENGLISH_LST
                 ENGLISH_LST+= ENGLISH_MORE
             try:
                 word=ENGLISH_LST[WORDS.index(HASH)]
                 rx.style.print('Found',color='green')
                 print('Decrypted String is:  ',end='')
                 rx.style.print(word,color='green',end='\n\n')
                 find=True
                 ce('')
             except:
                 rx.style.print('Word Not Found in English Dictionary!',color='light_red')
 
         if SS[2] and not find:
             WORD=rx.read(f'./HD/10kmcp/10kmcp_md5.txt')
             WORDS= WORD.split('\n')
             #print(HASH)
             #print(TenK_MCP[WORDS.index(HASH)])
             try:
                 word=TenK_MCP[WORDS.index(HASH)]
                 rx.style.print('Found',color='green')
                 print('Decrypted String is:  ',end='')
                 rx.style.print(word,color='green',end='\n\n')
                 find=True
                 ce('')
                 return True
             except:
                 print()
                 #raise
                 #rx.style.print('Word Not Found in 10K MOST COMMON PASSWORDS!',color='light_red')
 
         if SS[3] and not find:
             for word in range(int(rang)):
                 result = hashlib.md5(str(word).encode()) 
                 rh=result.hexdigest()
                 if rh==HASH:
                     find=True
                     rx.style.print('Done.',color='green')
                     print('Decrypted String is:  ',end='')
                     rx.style.print(word,color='green',end='\n\n')
                     ce('')
                     return True
 
         if not find:
             ce('Not Found',color='red')
             
 
     if int(mi) in range(2,7):
         WORDS=[]
         def decsha(nom,File):
             if File== 'ENG':
                 ENGLISH_LST= ENGLISH
                 if not nom:  
                     WORDS=rx.read(f'./HD/ENG/eh_{dichash[mi]}.txt').split('\n')
                     if SS[1]:
                         WORDS+=rx.read(f'./HD/ENG/MORE/ehm_{dichash[mi]}.txt').split('\n')
                         ENGLISH_LST+=ENGLISH_MORE                   
                 else:
                     try:
                         WORDS=rx.read(f'./HD/ENG/eh_sha3-{dichash[mi][-3:]}.txt').split('\n')
                     except:
                         return False
                     if SS[1]:
                         WORDS+=rx.read(f'./HD/ENG/MORE/ehm_sha3-{dichash[mi][-3:]}.txt').split('\n')
                         ENGLISH_LST+=ENGLISH_MORE                
             if File== '10K MCP':
                 if not nom:  
                     WORDS=rx.read(f'./HD/10kmcp/10kmcp_{dichash[mi]}.txt').split('\n') 
                 else:    
                     WORDS=rx.read(f'./HD/10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt').split('\n') 
 
             #WORDS= WORD.split('\n')
             try:
                 word=ENGLISH_LST[WORDS.index(HASH)] if File=='ENG' else TenK_MCP[WORDS.index(HASH)]
                 print('Decrypted String is:  ',end='')
                 rx.style.print(str(word),color='green',end='')
                 #rx.style.print('Found','green')
                 if len(dichash[mi])==6:
                     typee= f'sha2-{dichash[mi][-3:]}' if not nom else f'sha3-{dichash[mi][-3:]}'
                     rx.style.print(f'  ({typee})','dodger_blue_2',end='\n\n')
                 ce('')
                 #return True
             except:
                 return False
         x=False  
         if SS[0]:
             x= decsha(0,'ENG')
             if not x:
                 rx.style.print('Word Not Found in 1st Try in English Dictionary','light_red')
                 x= decsha(1,'ENG')
             if not x:
                 rx.style.print('Word Not Found in 2nd Try in English Dictionary','light_red')
         if SS[2] and not x:
             x= decsha(0,'10K MCP')
             if not x:
                 rx.style.print('Word Not Found in 1st Try in 10K MCP','light_red')
                 x= decsha(1,'10K MCP')
             if not x:
                 rx.style.print('Word Not Found in 2nd Try in 10K MCP','light_red')
         if SS[3] and not x:
             if mi=='2':
                 enc=hashlib.sha1
             if mi=='3':
                 enc= hashlib.sha224
                 enc2=hashlib.sha3_224
             if mi=='4':
                 enc=hashlib.sha256
                 enc2=hashlib.sha3_256
             if mi=='5':
                 enc=hashlib.sha384
                 enc2=hashlib.sha3_384
             if mi=='6':
                 enc=hashlib.sha512
                 enc2=hashlib.sha3_512
             #time=rx.record()
             for word in range(int(rang)):
                 result= enc(str(word).encode()) 
                 result2=enc2(str(word).encode())
                 rh= result.hexdigest()
                 rh2=result2.hexdigest()
                 #print(rh)
                 if rh==HASH or rh2==HASH:
                     rx.style.print('Found','green')
                     print('Decrypted String is:  ',end='')
                     rx.style.print(word,color='green',end='')
                     if len(dichash[mi])==6:
                         typee= f'sha2-{dichash[mi][-3:]}' if rh==HASH else f'sha3-{dichash[mi][-3:]}'
                         rx.style.print(f'  ({typee})','dodger_blue_2',end='\n\n')
                     x=True
                     ce('')
             if not x:
                 rx.style.print('Word Not Found in Numbers')
         if not x:
             ce('Not Found',color='red')
     #ce('')
    """

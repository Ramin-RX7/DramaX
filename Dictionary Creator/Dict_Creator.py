from rx7 import write,cls,style,p
import subprocess


def CREATE(SS,LENGTH,FILE):
    complete_list = []
    for current in range(LENGTH):
        a = [i for i in SS]
        for y in range(current):
            a = [x+i for i in SS for x in a]
        complete_list = complete_list+a
    p()
    print('Number of Generated Words:  '+str(len(complete_list)))
    if len(complete_list):
        try:
            write('./Dictionary Creator/'+str(LENGTH)+'-'+FILE+'.txt','\n'.join(complete_list))
        except:
            write(str(LENGTH)+'-'+FILE+'.txt','\n'.join(complete_list))
        print('Dictionary File Has Been Created Successfully.')
        print(f'(Address:  ./Dictionary Creator/{str(LENGTH)+"-"+FILE}.txt)')
    print('Nothing to Create.')


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
        return input(' '+prompt+'')
    LENGTH= input_def('Max Length:  ','4')
    if LENGTH=='99':
        global EX
        EX=False 
        return False
    try:
        LENGTH= int(LENGTH)
        if 11>LENGTH > 4:
            print(f'{LENGTH} is High Number. It Can Cause Big Problems to Your Device.')
            CI= input('Type CONFIRM to start operation: ')
            if CI != 'CONFIRM':
                return True
        if LENGTH>10:
            style.print('YOU ARE NOT NASA!')
            os.system('pause')
    except:
        #global EX
        #EX=False 
        return False   
    import string
    dic={'Lower Case:  ':string.ascii_lowercase, 'Upper Case:  ':string.ascii_uppercase,
         'Numbers:     ':string.digits,'Symbols:     ':'!@#$%&*-_.','Symbols2:    ':'/?><}{)(][~^','Space:       ':' '}
    SS=''
    FN=''
    for item in ss:
        x= input_def(item)
        if x.lower() in ('99','tx','x'):
            #global EX
            #EX=False 
            return False   
        if x in ('True','T'):
            SS+= dic[item]
            FN+=FPs[ss.index(item)]

    CREATE(SS,LENGTH,FN)

FPs=['L','U','N','S','~','D']
EX=True
while EX:
    cls()
    style.print('''
    `7MM"""Yb.     .g8"""bgd  
     MM    `Yb.  .dP'     `M  
     MM     `Mb  dM'       `  
     MM      MM  MM           
     MM     ,MP  MM.          
     MM    ,dP'  `Mb.      ,' 
    .JMMmmmdP'     `"bmmmd'   
                             
    ''','red')
    V= CSS('Lower Case:  ','Upper Case:  ','Numbers:     ','Symbols:     ','Symbols2:    ','Space:       ')
    if not V:
        print(' Press any key to continue')
        subprocess.getoutput('pause')
        if not EX:
            EX=False
    if not V and not EX:
        print(' Press any key to Exit')
        subprocess.getoutput('pause')

    

# import getpass, hashlib, os
import rx7 as rx



print = rx.style.print


def pause():
    print()  
    rx.io.getpass('Press Enter to Continue')


def list_lines(filename):
    '''
    return a list that contains every line of file
    '''
    #list_of_words = open(filename).readlines()
    list_of_words= rx.read(filename).splitlines()
    return list_of_words


def get_files(prompt='Enter File Name:  ', check_if_exists=True,
              sort=False, times=100, empty_input_action="error"):
    '''
    Prompt repeated  'Enter File Name:'  input until user enter 'end'
    if check_if_exists is false it will add files even if they do not exist
    by default list of files are sorted by input order 
    but if sort=True they will be sorted by their name
    empty_input_action: what to do if user gives an empty input
    '''
    List = set()
    i = 1
    while i <= times:
        filename = input(prompt)#rx.io.wait_for_input(prompt)
        if filename in ('end',""):
            if  (filename=="end") or (
                (filename == "") and (empty_input_action=="end")):
                    break
        pass
        if check_if_exists:
            if rx.files.exists(filename):
                List.add(filename)
                i+=1
            else:
                rx.style.print('File Does Not Exist.')
        else:
            i+=1
            List.add(filename)
    if sort:
        return sorted(list(List))
    return list(List)


def print_banner(banner:str,colors='auto'):
    if colors == 'auto':
        colors = {'Yellow' :['yellow','gold_1'],  'Blue' :['blue','dodger_blue_2'],
                  'Red'    :['red','red_1'    ],  'Green':['green','green_3a'],
                  'Classic':['grey_46','default']}

    chosen_color_group = rx.random.choose(list(colors.values()))
    print(banner,color=chosen_color_group[0])
    return chosen_color_group


def yesno_input(prompt,default=None):
    # error= not bool(default)
    if default==False:
        default_text = "[y/N]"
    elif default == None:
        default_text = "[y/n]"
    else:
        default_text = "[Y/n]"
    return rx.io.selective_input(f"{prompt} {default_text}?  ",
                                 ['y','yes','n','no'], default,
                                 True,True)

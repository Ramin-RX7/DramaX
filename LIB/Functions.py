import getpass, hashlib, os
import rx7.lite as rx

def list_lines(filename):
    '''
    return a list that contains every line of file
    '''
    #list_of_words = open(filename).readlines()
    list_of_words= rx.read(filename).splitlines()
    return list_of_words


def wait_for_input(prompt):
    '''
    Prompt  input(prompt)  until sth is given
    '''
    answer= ''
    while not answer:
        answer = input(prompt)
    return answer


def pause(prompt='Press Enter To Continue ...'):
    '''
    Disable terminal echo and wait for 'Enter' button
    '''
    print(prompt)#,end='')
    getpass.getpass('')


def get_files(prompt='Enter File Name:  ', check_if_exists=True, sort= False, times=100):
    '''
    Prompt repeated  'Enter File Name:'  input until user enter 'end'
    if check_if_exists is false it will add files even if they do not exist
    by default list of files are sorted by input order 
    but if sort=True they will be sorted by their name
    '''
    List = set()
    i = 1
    while i <= times:
        filename = wait_for_input(prompt)
        if filename == 'end':
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


def cls():
    '''
    You can use this function if you want to clear the environment.
    '''
    import platform
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clear = cls

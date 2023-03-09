import sys, re
if(sys.platform == "win32"):
    import ctypes
    from ctypes import wintypes
else:
    import termios

import rx7 as rx
from tabulate import tabulate



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
    Prompt repeated  'Enter File Name:'  input until user enter '' or 'end'

    if `check_if_exists` is false it will add files even if they do not exist

    by default list of files are sorted by input order

    but if `sort=True` they will be sorted by their name

    `empty_input_action`: what to do if user gives an empty input
    '''
    List = set()
    i = 1
    while i <= times:
        filename = input(prompt)#rx.io.wait_for_input(prompt)
        if (filename=="end") or (
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


def cursorPos():
    if(sys.platform == "win32"):
        OldStdinMode = ctypes.wintypes.DWORD()
        OldStdoutMode = ctypes.wintypes.DWORD()
        kernel32 = ctypes.windll.kernel32
        kernel32.GetConsoleMode(kernel32.GetStdHandle(-10), ctypes.byref(OldStdinMode))
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 0)
        kernel32.GetConsoleMode(kernel32.GetStdHandle(-11), ctypes.byref(OldStdoutMode))
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        OldStdinMode = termios.tcgetattr(sys.stdin)
        _ = termios.tcgetattr(sys.stdin)
        _[3] = _[3] & ~(termios.ECHO | termios.ICANON)
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)
    try:
        _ = ""
        sys.stdout.write("\x1b[6n")
        sys.stdout.flush()
        while not (_ := _ + sys.stdin.read(1)).endswith('R'):
            True
        res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", _)
    finally:
        if(sys.platform == "win32"):
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), OldStdinMode)
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), OldStdoutMode)
        else:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)
    if(res):
        return (int(res.group("x")), int(res.group("y")))
    return (-1, -1)


def clear_lines(n):
    # for _ in range(n):
        # UP = "\x1B[1A"
        # CLR = "\x1B[0K"
        # print(end='\x1B[1A\x1b[2K')
        # sys.stdout.flush()
    output = '\x1B[1A\x1b[2K'*n
    print(end=output)


class tabulate_table:
    def __init__(self, data:list=[], **kwargs) -> None:
        self._data = data
        self._options = kwargs

    def add_row(self, row):
        # self.data = self.data + type(self.data)([row])
        self._data = tabulate_table._add(self._data, row)

    def add_col(self, col, header=None):
        for i,item in enumerate(col):
            # self.data[i] = self.data[i] + type(self.data[i])(item)
            self._data[i] = tabulate_table._add(self._data[i], item)
        if header:
            # self.options["headers"] = self.options["headers"] + type(self.options["headers"])(header)
            self._options["headers"] = tabulate_table._add(self._options["headers"], header)

    def shape(self):
        try:
            cols = (self._options["headers"])
        except:
            if len(self.data):
                cols = len(self._data[0])
            else:
                cols = 0
        return (len(self.data), cols)

    @staticmethod
    def _add(dataset, item):
        return dataset + type(dataset)([item])

    @classmethod
    def merge(cls, first, second):
        return cls(first.data+second.data)

    def set_option(self, **kwargs):
        self._options = {**self._options, **kwargs}

    def __str__(self) -> str:
        return tabulate(self._data, **self._options)
    def __repr__(self) -> str:
        return tabulate(self._data, **self._options)

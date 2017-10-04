"""Command."""
from src.logger.logger import logger
from src.commad.action.init_action import init_action
from src.commad.action.create_action import create_action
from src.commad.action.merge_action import merge_action
from src.commad.action.list_action import list_action
from src.commad.action.edit_action import edit_action
from src.commad.action.set_action import set_action
from src.commad.action.remove_action import remove_action


log = logger()

description = """
Usage: main.py [OPTIONS]

  Host-switcher

Options:
  --init                                                                set current hosts file default hosts file
  --create   [name new file]                                            create new hosts file by current hosts file
  --createby [hosts.{name file}] [name new file]                        create new hosts file from selected file
  --merge    [hosts.{name file}] [hosts.{name file}] [name new file]    merge two exist files
  --edit     [hosts.{name file}]                                        edit hosts file
  --set      [hosts.{name file}]                                        set hosts file
  --list                                                                list of hosts files
  --remove   [hosts.{name file}]                                        remove custom hosts files
  --help                                                                Show this message and exit.
"""


def command(func):
    def getArgs(self, arg):
        try:
            log.log_info('Command cli start')
            func = getattr(function, arg[1][2:])
            func(arg)
        except Exception as e:
            log.log_warning(e)
            function.help()
    return getArgs


class function:

    def help():
        print(description)

    def init(arg=list):
        init_a = init_action()
        init_r = init_a.copy_current_host_file()
        print_cli.print_dict(init_r)

    def create(arg=list):
        try:
            create_a = create_action()
            create_r = create_a.create_new_file_by_current(None, arg[2])
            print_cli.print_dict(create_r)
        except Exception as e:
            create_a = create_action()
            create_r = create_a.create_new_file_by_current()
            print_cli.print_dict(create_r)

    def createby(arg=list):
        try:
            create_a = create_action()
            create_r = create_a.create_new_file_by_select(arg[2], arg[3])
            print_cli.print_dict(create_r)
        except Exception as e:
            create_a = create_action()
            create_r = create_a.create_new_file_by_select()
            print_cli.print_dict(create_r)

    def merge(arg=list):
        try:
            merge_a = merge_action()
            merge_r = merge_a.merge_files(arg[2], arg[3], arg[4])
            print_cli.print_dict(merge_r)
        except Exception as e:
            merge_a = merge_action()
            merge_r = merge_a.merge_files()
            print_cli.print_dict(merge_r)

    def edit(arg=list):
        try:
            edit_a = edit_action()
            edit_r = edit_a.edit_file(arg[2])
            print_cli.print_dict(edit_r)
        except Exception as e:
            edit_a = edit_action()
            edit_r = edit_a.edit_file()
            print_cli.print_dict(edit_r)

    def set(arg=list):
        try:
            set_a = set_action()
            set_r = set_a.set_file(arg[2])
            print_cli.print_dict(set_r)
        except Exception as e:
            set_a = set_action()
            set_r = set_a.set_file()
            print_cli.print_dict(set_r)

    def list(arg=list):
        list_a = list_action()
        lof = list_a.list_of_file()
        lof = list_a.in_use(lof)
        titles = ['File name', 'Create date', 'Update date']
        table.print_table(titles, lof)

    def remove(arg=list):
        try:
            remove_a = remove_action()
            remove_r = remove_a.remove_file(arg[2])
            print_cli.print_dict(remove_r)
        except Exception as e:
            while True:
                remove_a = remove_action()
                remove_r = remove_a.remove_file()
                print_cli.print_dict(remove_r)


class print_cli:
    def print_dict(dict_risp):
        if dict_risp['status'] == 0:
            print(' ' + dict_risp['msg'])
        if dict_risp['status'] == -1:
            print(' ' + dict_risp['msg'])


class table:
    def print_table(titles=list(), data=list()):
        try:
            col_num = len(titles)
            titles = list(titles)
            table = list()
            table.append(titles)
            for row in data:
                table.append(row)
            col_len = 0
            # get max string
            for row in table:
                for i in range(col_num):
                    if len(row[i]) > col_len:
                        col_len = len(row[i])

            col_len = col_len + 2
            # set len string
            print("-"*((col_num*col_len)+col_num))
            count_row = 0
            for row in table:
                string_row = "|"
                for i in range(col_num):
                    add_c = col_len - len(row[i])
                    row[i] = row[i] + (" "*add_c)
                    if row[i].find("*") == 0:
                        row[i] = str('\033[1m' + row[i][1:] + ' \033[0;0m')
                    if count_row == 0:
                        row[i] = str('\033[1m' + row[i] + '\033[0;0m')
                    string_row = string_row + row[i] + "|"
                print(string_row)
                print("-"*((col_num*col_len)+col_num))
                count_row = count_row + 1
            print("\n")
        except Exception as e:
            print(e)

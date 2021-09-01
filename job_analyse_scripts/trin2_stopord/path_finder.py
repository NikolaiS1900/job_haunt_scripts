import os, platform

cwd = os.getcwd()

platform = platform.system()
    

def UNIX_path():
    cwd_split = cwd.split('/')
    to_parent_dir = cwd_split[:-1]
    path = '/'.join(to_parent_dir)
    return path

def Windows_path():
    cwd_split = cwd.split('\\')
    to_parent_dir = cwd_split[:-1]
    path = '\\'.join(to_parent_dir)
    return path


def path_finder():
    if platform == "Windows":
        path = Windows_path()

        return path

    else:
        path = UNIX_path()
        return path

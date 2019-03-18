from time import localtime, strftime
import sys, os


def astr(strobj):
    """
    :param strobj:
    :return a str type value:
    """
    try:
        return str(strobj)
    except:
        return strobj


def anum(numobj):
    """
    :param intobj:
    :return a num type value:
    """
    try:
        return float(numobj)
    except:
        return numobj


def nowf(format='t'):
    """
    :param format: a time format marker:
    :return a str value:
    """
    if format == 's':
        # serial
        format = '%Y%m%d%H%M%S'
    if format == 't':
        # time
        format = '%Y-%m-%d %H:%M:%S'
    if format == 'd':
        # date
        format = '%Y-%m-%d'
    return strftime(format, localtime())


def amkdir(dir_name):
    # curdir=os.path.split(os.path.abspath(sys.argv[0]))[0]
    curdir = os.getcwd()
    credir = os.path.join(curdir, dir_name)
    if not os.path.exists(credir):
        os.mkdir(dir_name)
    return credir


def script(fpath, s):
    """
    Create a executable file include command s.
    :param fpath: file path (include name.)
    :param s: file content.
    :param c: execute command.
    :return: fpath.
    """
    import os
    fpath=os.path.abspath(fpath)
    with open(fpath, 'w') as f:
        f.write(s + '\n')
    os.system('chmod +x ' + fpath)
    return fpath

# print(nowf('s'))
# print(nowf('t'))
# print(nowf('d'))
# print(astr('110'))
# print(astr(110))
# print(anum(110))
# print(anum('110'))

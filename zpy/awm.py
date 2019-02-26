from time import localtime,strftime

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
    if format=='s':
        #serial
        format='%Y%m%d%H%M%S'
    if format=='t':
        #time
        format='%Y-%m-%d %H:%M:%S'
    if format=='d':
        #date
        format='%Y-%m-%d'
    return strftime(format,localtime())


#print(nowf('s'))
#print(nowf('t'))
#print(nowf('d'))
#print(astr('110'))
#print(astr(110))
#print(anum(110))
#print(anum('110'))

def readalltext(filepath):
    try:
        f = open(filepath, 'r')
        res = f.read()
        f.close()
        return res
    except:
        return None


def writealltext(filepath, txt):
    try:
        f = open(filepath, 'w')
        f.write(txt)
        f.close()
        return True
    except:
        return False


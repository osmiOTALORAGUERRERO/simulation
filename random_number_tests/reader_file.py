def read(path):
    fr = open(path,'r')
    content = fr.read()
    fr.close()
    return content

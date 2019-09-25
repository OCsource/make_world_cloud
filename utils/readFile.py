def readFile(path):
    with open(path, 'r', encoding='utf8') as f:
        text = f.read()
    return text
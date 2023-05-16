import pathlib, os

PATH = rf'{pathlib.Path().absolute()}'\

print (PATH, os.listdir(PATH))

content = ''
for x in os.listdir(PATH):
    print(x)
    if 'writeWork' not in x:
        if '.py' in x:
            content += x.upper() + ':\n'
            with open(x, 'r', encoding='utf-8') as curr:
                content += curr.read() + '\n'
            content += '\n'
            print(content)
        elif x == 'pages':
            content += 'PAGES:\n\n'
            p = PATH + '\pages'
            print(os.listdir(p))
            for y in os.listdir(p):
                print(y)
                content += y.upper() + ':\n'
                y = p + '\\' + y
                with open(y, 'r', encoding='utf-8') as curr:
                    content += curr.read() + '\n'
                content += '\n'

with open('project.txt', 'w') as final:
    final.write(content)
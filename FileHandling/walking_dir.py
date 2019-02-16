import os
for (dirname, subshere, fileshere) in os.walk(r'C:\TECHNICAL\MS'):
    print('-----------------------------------------------------')
    print('[' + dirname + ']')
    print('-----------------------------------------------------')
    for fname in fileshere:
        print(os.path.join(dirname, fname))

import os
matches = []
for (dirname, dirshere, fileshere) in os.walk(r'C:\temp\PP3E\Examples'):
    for filename in fileshere:
        if filename.endswith('.py'):
            pathname = os.path.join(dirname, filename)
            if 'mimetypes' in open(pathname).read():
                matches.append(pathname)

for name in matches: 
    print(name)


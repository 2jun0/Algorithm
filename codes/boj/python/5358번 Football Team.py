import sys
for line in sys.stdin.readlines():
    line = line.strip()
    
    line = line.replace('i', '!')
    line = line.replace('I', '@')
    line = line.replace('e', '#')
    line = line.replace('E', '$')
    line = line.replace('!', 'e')
    line = line.replace('@', 'E')
    line = line.replace('#', 'i')
    line = line.replace('$', 'I')
    print(line)

#!/usr/bin/env python3

def blocks(fobj):
    content = []
    counter = 0
    for line in fobj:
        content.append(line)
        counter += 1
        if counter == 10:
            yield content
            content = []
            counter = 0
    if content:
        yield content




if __name__ == '__main__':
    fname='/etc/passwd'
    with open(fname) as fobj:
        for lines in blocks(fobj):
            print(lines)
            print('*' * 20)
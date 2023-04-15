# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    if "I" in input():
        patt =  input().rstrip()
        text = input().rstrip()

    else:
        file = open("tests/06","r")
        patt = file.readline().strip()
        text = file.readline()
        file.close() 
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (patt,text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(patt, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    index = []
    pattern = hash(patt)

    for i in range (len(text) - len(patt)+1):
        texthash = hash(text[i: i + len(patt)])

        if texthash == pattern:
            if text[i:i + len(patt)] == patt:
                index.append(i)
    # and return an iterable variable
    return index


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


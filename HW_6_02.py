

def toString(fileName):
    # This function returns the text from a given file.
    # Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    f.close()
    return out


def longestLine(fileName):
    # Given a file return the longest line from within that file
    f = open(fileName)
    longest = ""
    
    for line in f:
        line = line.strip()
        if len(line) > len(longest):
            longest = line
    
    f.close()
    return longest


def toBinary(fileName):
    # Given a file that is only 0's and 1's return a list of the file broken into bytes.
    # An example return might be ['01101001', '00101010', '1010']
    f = open(fileName)
    text = f.read()
    f.close()
    
    # Remove any spaces or newlines
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    
    # Break into chunks of 8
    bytes_list = []
    i = 0
    
    while i < len(text):
        byte = ""
        for j in range(8):
            if i < len(text):
                byte = byte + text[i]
                i = i + 1
            else:
                break
        bytes_list.append(byte)
    
    return bytes_list

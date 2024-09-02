
def IsUniqueBasic(string):
    return len(set(string)) == len(string)

def IsUniqueASCII(string):
    # Assuming characters are just ASCII
    
    if len(string) > 128:
        return False
    
    checker = [None] * 128
    
    for char in string:
        pos = ord(char)
        
        if checker[pos]:
            return False
        else:
            checker[pos] = True
    
    return True


if __name__ == "__main__":
    print(IsUniqueBasic('asdfghjkas'))
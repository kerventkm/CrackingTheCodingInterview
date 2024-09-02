def IsUniqueBasic(string):
    return len(set(string)) == len(string)


if __name__ == "__main__":
    print(IsUniqueBasic('asdfghjkas'))
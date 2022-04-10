# stringProcess module
print("stringProcess module is initialized")

if __name__ == "__main__":
    print("The stringProcess is used as script")
elif __name__ == "stringProcess":
    print("The stringProcess is used as module")


def stringSplit(string, separator):
    outputString = string.split(sep=separator)
    return outputString
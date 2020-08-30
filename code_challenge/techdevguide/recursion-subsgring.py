string = input("Please enter a word: ")
substring = input("Please enter the substring you wish to find: ")
replacement = input("Please enter a string to replace the give substring: ")

def search_and_replace(string, substring, replacement):
    if not string:  #if the string is empty
        return ""
    elif string[:len(substring)] == substring:
        return replacement + search_and_replace(string[len(substring):],
                                                substring, replacement)
    else:
        return string[0] + search_and_replace(string[1:], substring,
                                              replacement)
print(search_and_replace(string, substring, replacement))

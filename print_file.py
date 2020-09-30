def getFileContent(file_path):
    """
    with open(file_path, "rb") as file_content:
        return file_content
    """
    f = open(file_path, "r")
    #print(f.read())
    return f.read()
gg = getFileContent("json_static.json")
print(gg)
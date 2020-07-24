import os

def readFile(filePath):
    """
    Read the input file.

    Parameters:
        filePath (str): path of the input file

    Returns:
        file (object): content of input file
    """
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            data = file.readlines()

        return data
    raise Exception("File not found..")
    return None

def writeIntoFile(string, filePath):
    """
    Write into file.

    Parameters:
        string (str): String to write into file
        filePath (str): path of the output file

    Returns:
        filePath (str): Path of the output file
    """
    with open(filePath, "w") as text_file:
        text_file.write(string)
    return filePath

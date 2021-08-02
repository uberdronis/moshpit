from datetime import datetime as dt



# main entry point for our script
def main():
    # set variables that we will use throughout our examples!
    board = "Raspberry Pi"
    version = 4
    model = "B"
    released = 2019

    # let's print based on the '%s' string replacement
    print("This is the %s board, version %s model %s, released on %s" % (board, version, model, released))

    # let's print based on adding the strings together
    print("This is the " + board + " board, version " + str(version) + " model " + model + ", released on " + str(released))

    # let's print based on the string format method
    print("This is the {} board, version {} model {}, released on {}".format(board, version, model, released))

    # you can also pass in the variable names on the string.format method
    print("This is the {board_name} board, version {version_name} model {model}, released on {released}".format(
        board_name = board, version_name = version, model=model, released=released))

    # you can also pass in a dictionary for the string.format method
    sample_dict = {
        "board": board, 
        "version": version, 
        "model": model, 
        "released": released }
    print("This is the {board} board, version {version} model {model}, released on {released}".format(**sample_dict))

    # f-strings to the rescue
    print(f"This is the {board} board, version {version} model {model}, released on {released}")

    # this also works, because the 'f' is not case-sensitive
    print(F"This is the {board} board, version {version} model {model}, released on {released}")

    # you can perform operations in the curly mustaches!
    print(f"This is the {board} board, version {version} model {model}, released on {released} ({dt.utcnow().year - released} years ago)")

    # print curly mustaches
    print(f"{{hello}}")

    # print interpreted value in curly mustaches
    print(f"{{{1 + 1}}}")


# we should always check for __name__
if __name__ == "__main__":
    main()
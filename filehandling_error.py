try:
    filename = input("Enter a filename: ")
    if filename == "":
        raise NameError

    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    f.close()
except OSError as e:
    print("File does not exist!")
except NameError as e:
    print("File name cannot be empty!")
finally:
    print("Done with files...")

# better way to handle files
# with open(filename, "r") as f:
#     lines = f.readlines()
#     for line in lines:
#

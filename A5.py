try:
    filename = input("Enter a filename: ")
    if filename == "":
        raise NameError

    with open(filename, "r") as f:
        for line in f.readlines():
            print(line, end="")

    # f = open(filename, "r")
    # lines = f.readlines()
    # for line in lines:
    #     print(line, end="")
    # f.close()

except FileNotFoundError:               # when using `with` to open file
    print("File does not exist!")
except OSError:                         # when opening file directly
    print("File does not exist!")
except NameError:
    print("File name cannot be empty!")
except Exception as e:                  # unhandled exception
    print("Some unexpected error occured!")
    print("Details are...")
    print(e)
finally:
    print("Done with files...")

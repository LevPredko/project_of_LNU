from Backpack import Backpack

def backpack1():
    testpack = Backpack("Barry", "black")
    if testpack.name != "Barry" or testpack.color != "black":
        print("Backpack.name or Backpack.color assigned incorrectly")

    for item in ["pencil", "pen", "paper", "laptop"]:
        testpack.put(item)
    print(testpack.__str__())
    return testpack


def backpack2():
    testpack = Backpack("Tom", "white")
    if testpack.name != "Tom" or testpack.color != "white":
        print("Backpack.name or Backpack.color assigned incorrectly")

    for item in ["workbook", "laptop", "eraser", "pen"]:
        testpack.put(item)
    print(testpack.__str__())
    return testpack


all_backpacks = [backpack1(), backpack2()]

found_backpack = Backpack.find_backpack_color(all_backpacks, "white")

if found_backpack:
    print("\u001B[32m" + "White backpack found:" + "\u001B[0m")
    print(found_backpack)
else:
    print("\u001B[31m" + "White backpack not found."+ "\u001B[0m")

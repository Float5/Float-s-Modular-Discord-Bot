import pickle

def addAdmin(admin):
    adminList = []
    with open("admin.pickle", "rb") as data:
        adminList = pickle.load(data)

    adminList = list(adminList)

    try:
        adminList.index(admin)
        print(f"[{admin}] Admin already listed")
    except:
        adminList.append(admin)

    with open("admin.pickle", "wb") as data:
        pickle.dump(adminList, data)

    printAdmin()


def delAdmin(admin):
    adminList = []
    with open("admin.pickle", "rb") as data:
        adminList = pickle.load(data)

    adminList = list(adminList)
    try:
         adminList.pop(adminList.index(admin))
    except:
        print(f"can't find [{admin}] Admin retry please")

    with open("admin.pickle", "wb") as data:
        pickle.dump(adminList, data)

    printAdmin()


def printAdmin():
    with open("admin.pickle", "rb") as data:
        print(pickle.load(data))




addAdmin("float_1")

def extractValue(value, count, includeSpaceOfLastValue = False):
    values = []
    indexs = []


    if count == 1:
        values.append(value)
        return values

    if includeSpaceOfLastValue == True:
        value += " "

    for i in range(0, count - 1, 1):
        if i == 0:
            indexs.append(value.index(" "))
        else:
            indexs.append(value.index(" ", indexs[i - 1] + 1))

    for i in range(0, count, 1):
        if i == 0:
            values.append(value[:indexs[i]])
        elif i == count - 1:
            values.append(value[indexs[i - 1]+1:])
        else:
            values.append(value[indexs[i - 1]+1:indexs[i]])

    return values
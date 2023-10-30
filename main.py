list1 = []


def recursiveMath(num):
    list1.append(num)
    if (num == 1):
        return
    if (num % 2 == 0):
        recursiveMath(int(num/2))
    else:
        recursiveMath((3*num)+1)


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


def sortNumbers(numberList):
    # sets index before values
    newList = []
    newList = numberList.copy()
    count = 1
    for x in range(0, len(newList)*2, 2):
        newList.insert(x, count)
        count = count + 1
    # converts into a dictionary
    dictionary = Convert(newList)

    # sorts by value

    temp = sorted(dictionary.items(), key=lambda x: x[1])

    sortedDictionary = dict(temp)

    return sortedDictionary


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def printGraph(list1, mod):

    numCount = 1

    final = sortNumbers(list1)

    value = list(final.values())

    # y-axis print
    if (mod == 'Y'):
        print('\n\tGRAPH at High-Accuracy')
        for i in range(value[-1], 0, -1):
            print(str(i).zfill(2), end='')

            # adding in the points
            if (i == value[len(value)-numCount]):
                numCount = numCount + 1
                foo = get_keys_from_value(final, i)
                if (i >= 1000):
                    print(' '*(foo[0]-3)+'   '*(foo[0]-1) + '* ', end='')
                elif (i < 1000 and i >= 100):
                    print(' '*(foo[0]-2)+'  '*foo[0] + '* ', end='')
                else:
                    print(' '*(foo[0]-1)+'  '*foo[0] + '* ', end='')

            print()

    elif (mod == 'N'):
        print('\n\tGRAPH at Low-Accuracy')
        for i in range(value[-1], 0, -1):
            if (i == value[len(value)-numCount]):
                numCount = numCount + 1
                print(str(i).zfill(2), end='')
                foo = get_keys_from_value(final, i)

                if (foo[0] >= 100):
                    if (i >= 1000):
                        print(' '*(foo[0]-3)+'   '*(foo[0]-2) + '* ', end='')
                    elif (i < 1000 and i >= 100):
                        print(' '*(foo[0]-2)+'  '*(foo[0]-1) + '* ', end='')
                    else:
                        print(' '*(foo[0]-1)+'  '*(foo[0]-1) + '* ', end='')
                    print()
                else:
                    if (i >= 1000):
                        print(' '*(foo[0]-3)+'   '*(foo[0]-1) + '* ', end='')
                    elif (i < 1000 and i >= 100):
                        print(' '*(foo[0]-2)+'  '*foo[0] + '* ', end='')
                    else:
                        print(' '*(foo[0]-1)+'  '*foo[0] + '* ', end='')
                    print()

    else:
        print('ERROR')

    # x-axis print
    for j in range(len(list1)+1):
        print(str(j).zfill(2), end=' ')


if __name__ == "__main__":

    ask = True
    while (ask):
        try:
            num = int(input('Enter Num: '))
        except ValueError:
            print("You did not enter a number, please re-enter")
            continue
        new = str(input('Use High-Accuracy on the Y-axis? Y or N: '))
        mod = new.upper()

        if (mod == 'Y' or mod == 'N'):
            ask = False
        else:
            print('\nPlease Enter Values Again.\n')

    recursiveMath(num)
    printGraph(list1, mod)
else:
    print('Error, imported program.')

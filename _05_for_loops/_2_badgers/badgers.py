if __name__ == '__main__':
    badger = 'badger'
    mushroom = 'mushroom'
    for i in range(2):
        for i in range(12):
            if i !=11:
                print(badger, end=", ")
            else:
                print(badger)
        for i in range(2):
            if i == 0:
                print(mushroom, end=", ")
            else:
                print(mushroom)
    print('Snake!!')
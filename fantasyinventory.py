# create fantasy inventory system with dictionaries
import sys

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print()
    print("Inventory:")
    print()
    item_total = 0
    for k, v in inventory.items():
        if v > 0:
            item_total = v
        else:
            item_total = 0
        print(k + ': ' + str(item_total))


def addItem(storage):
    displayInventory(storage)
    print()
    print('Would you like to add an item to inventory?')
    print()
    answer = input('Y/N: ')
    if answer == 'Y':
        print('What would you like to add?')
        loot = input()
        print('How much do you have to add? (Enter negative number to remove that amount)')
        amount = int(input())
        if loot in storage:
            storage[loot] += amount
            displayInventory(storage)
        else:
            storage[loot] = amount
            displayInventory(storage)

    elif answer == 'N':
        print()
        print("Here's what you have.")
        print()
        displayInventory(storage)
    else:
        print('Please enter a valid answer.')


addItem(stuff)

while True:
    print()
    print("Are you done?")
    p = input('Y/N: ')
    if p == 'Y':
        print('Goodbye.')
        sys.exit()
    elif p == 'N':
        addItem(stuff)
    else:
        print('Please enter a valid answer.')
        print()

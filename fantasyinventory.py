# create fantasy inventory system with dictionaries


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
        
displayInventory(stuff)  

def search(items, key):
    low = 0
    high = len(items)-1

    while low <= high:
        mid = (low + high) // 2
        if key == items[mid]:
            return mid
        elif key < items[mid]:
            high = mid - 1
        elif key > items[mid]:
            low = mid + 1

    return -1



def main():
    r = search([2,4,5,6,8],10)
    print(r)








if __name__ == "__main__":
    main()


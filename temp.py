def isValidSubsequence(array, sequence):
    # Write your code here.
    index = 0

    for item in sequence:
        array = array[index:]
        print(array)
        if item in array[index:]:
            currentIndex = array.index(item)
            print(f"currentIndex: {currentIndex} Index: {index}")
            if currentIndex < index:
                print("I'm inside if")
                return False
            index = currentIndex + 1
        else:
            print("I'm inside else")
            return False
    return True


print(isValidSubsequence([1, 1, 1, 1], [1, 1, 1]))

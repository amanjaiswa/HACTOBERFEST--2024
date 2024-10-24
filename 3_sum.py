# Function to find a triplet with a given sum in an array
def find3Numbers(arr, sum):
    n = len(arr)

    # Sort the elements
    arr.sort()

    # Fix the first element one by one
    # and find the other two elements
    for i in range(n - 2):

        # To find the other two elements, start two index
        # variables from two corners of the array and move
        # them toward each other
        l = i + 1  # index of the first element
        r = n - 1  # index of the last element

        while l < r:
            curr_sum = arr[i] + arr[l] + arr[r]
            if curr_sum == sum:
                print(f"Triplet is {arr[i]}, {arr[l]}, {arr[r]}")
                return True
            elif curr_sum < sum:
                l += 1
            else:  # curr_sum > sum
                r -= 1

    # If we reach here, then no triplet was found
    return False


# Driver code
arr = [1, 4, 45, 6, 10, 8]
sum = 22

find3Numbers(arr, sum)

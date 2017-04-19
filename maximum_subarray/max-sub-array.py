

def max_sum_from_middle(array, low, mid, high):
    """
    This function calculates the maximum subarray sum from
    the middle to the left and right
    """
    left_max_sum = float("-inf")
    array_sum = 0
    max_left = mid

    for i in reversed(range(low, mid+1)):
        array_sum = array_sum + array[i]
        if array_sum > left_max_sum:
            left_max_sum = float(array_sum)
            max_left = i

    right_max_sum = float("-inf")
    array_sum = 0
    max_right = mid
    for i in range(mid+1, high+1):
        array_sum = array_sum + array[i]
        if array_sum > right_max_sum:
            right_max_sum = float(array_sum)
            max_right = i
    return max_left, max_right, left_max_sum + right_max_sum

def maximum_sub_array(array, low, high):
    """
    Calculates the maximum_sub_array
    """
    if low == high:
        return low, high, array[low]
    else:
        mid = (low + high) / 2

    left_low, left_high, left_sum = maximum_sub_array(array, low, mid)
    right_low, right_high, right_sum = maximum_sub_array(array, mid+1, high)
    cross_low, cross_high, cross_sum = max_sum_from_middle(array,
                                                           low, mid, high)
    if left_sum >= cross_sum and left_sum >= right_sum:
        return left_low, left_high, left_sum
    elif right_sum >= cross_sum and right_sum > left_sum:
        return right_low, right_high, right_sum
    elif cross_sum > left_sum and cross_sum > right_sum:
        return cross_low, cross_high, cross_sum

def kadane(array):
    """
    Kadane algo can find maximum_sub_array in O(n) time
    """
    max_so_far = max_till_here = array[0]
    for item in array[1:]:
        max_till_here = max(item, max_so_far + item)
        max_so_far = max(max_so_far, max_till_here)
    return max_so_far

if __name__ == "__main__":
    INPUT_NUMBERS = [2, 10, 30, -200]
    print maximum_sub_array(INPUT_NUMBERS, 0, len(INPUT_NUMBERS)-1)
    print kadane(INPUT_NUMBERS)

import sys


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -sys.maxsize - 1
    sum_ = 0

    for i in range(mid, low - 1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum = -sys.maxsize - 1
    sum_ = 0

    for j in range(mid + 1, high + 1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = \
            find_max_subarray(A, low, mid)

        right_low, right_high, right_sum = \
            find_max_subarray(A, mid+1, high)

        cross_low, cross_high, cross_sum = \
            find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return(left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return(left_low, left_high, left_sum)
        else:
            return(cross_low, cross_high, cross_sum)


def max_subarray_2(A):
    max_so_far = max_ending_here = A[0]

    for i in A[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_subarray(A):
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
    low = high = 0

    for i in range(0, len(A)):
        max_ending_here = max_ending_here + A[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            high = i

        if max_ending_here < 0:
            max_ending_here = 0
            low = i + 1
    return low, high, max_so_far


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 100]
    print(find_max_subarray(A, 0, len(A) - 1))
    print(max_subarray(A))
    print(max_subarray_2(A))

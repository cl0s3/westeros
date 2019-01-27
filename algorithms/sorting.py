import unittest


def insertion_sort(A):
    A = list(A)

    for j in range(1, len(A)):
        key = A[j]

        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1

        A[i+1] = key

    return A


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        L = l[:mid]
        R = l[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1


class TestSortingMethods(unittest.TestCase):
    def setUp(self):
        global A
        self.A = list(A)

    def tearDown(self):
        pass

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(A), sorted(A))

    def test_merge_sort(self):
        merge_sort(self.A)
        self.assertEqual(self.A, sorted(A))


if __name__ == '__main__':
    A = [7, 5, 2, 4, 77, 38, 6, 1, 3]
    unittest.main()

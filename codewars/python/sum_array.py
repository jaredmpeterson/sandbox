"""
Sum all the numbers of the array except the highest and the lowest element:

(The highest/lowest element is respectively only one element at each edge,
even if there are more than one with the same value!)
"""


def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    return sum(arr) - max(arr) - min(arr)


def main():
    test = sum_array([-6, -20, -1, -10, -12])
    print(test)


if __name__ == '__main__':
    main()


# Test.describe("Basic tests")
# Test.it("None or Empty")
# sum_array(None)
# sum_array([])

# Test.it("Only one Element")
# sum_array([3])
# sum_array([-3])

# Test.it("Only two Element")
# sum_array([3, 5])
# sum_array([-3, -5])

# Test.it("Real Tests")
# sum_array([6, 2, 1, 8, 10])
# sum_array([6, 0, 1, 10, 10])
# sum_array([-6, -20, -1, -10, -12])
# sum_array([-6, 20, -1, 10, -12])

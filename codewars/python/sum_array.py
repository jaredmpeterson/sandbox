# Sum all the numbers of the array except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)


def sum_array(arr):
    # your code here
    if not arr or len(arr) <= 2:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)


def main():
    test = sum_array([-6, -20, -1, -10, -12])
    print(test)


if __name__ == '__main__':
    main()


# Test.describe("Basic tests")
# Test.it("None or Empty")
# Test.assert_equals(sum_array(None), 0)
# Test.assert_equals(sum_array([]), 0)

# Test.it("Only one Element")
# Test.assert_equals(sum_array([3]), 0)
# Test.assert_equals(sum_array([-3]), 0)

# Test.it("Only two Element")
# Test.assert_equals(sum_array([3, 5]), 0)
# Test.assert_equals(sum_array([-3, -5]), 0)

# Test.it("Real Tests")
# Test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
# Test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
# Test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
# Test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)

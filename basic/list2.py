#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def _remove_adjacent_gen(list):
    iterator = iter(list)
    last = next(iterator)
    yield last
    while True:
        n = next(iterator)
        while n == last:
            n = next(iterator)
        yield n
        last = n


def remove_adjacent(nums):
    return list(_remove_adjacent_gen(nums))


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def _merge_gen(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)

    # accepts empty lists
    try:
        n1 = next(it1)
    except StopIteration:
        yield from it2
        return
    try:
        n2 = next(it2)
    except StopIteration:
        yield n1
        yield from it1
        return

    while True:
        if n1 < n2:
            yield n1
            try:
                n1 = next(it1)
            except StopIteration:
                yield n2
                yield from it2
                return
        else:
            yield n2
            try:
                n2 = next(it2)
            except StopIteration:
                yield n1
                yield from it1
                return

def linear_merge(list1, list2):
    return list(_merge_gen(list1, list2))


# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
    test(linear_merge([], ['aa', 'bb', 'bb']),
         ['aa', 'bb', 'bb'])
    test(linear_merge(['aa', 'bb', 'bb'], []),
         ['aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()

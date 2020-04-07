#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0

    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        index = int(index)
        if(index < 0 or index >= self.size):
            raise Exception(f'Error: {index} is not within the bounds of the current array.')


    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if(self.size == len(self.data)): 
            self.data = memcpy(alloc(self.size + 5), self.data, self.size)
            return True
        return False


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        if((len(self.data) - self.size) == 5):
            self.data = memcpy(alloc(self.size), self.data, self.size)
            return True
        return False


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()
        self.data[self.size] = item
        self.size += 1
        return self.data


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        self._check_bounds(index)
        self._check_increase()
        for i in range(self.size, 0, -1):
            if(i == int(index)):
                self.data[i] = item
                self.size += 1
                return self.data
            else:
                self.data[i] = self.data[i - 1]


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        self._check_bounds(index)
        self.data[int(index)] = item
        return self.data


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        self._check_bounds(index)
        return self.data[int(index)]


    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        self._check_bounds(index)
        for i in range(int(index), self.size):
            if(i == (self.size - 1)):
                self.data[i] = None
            else:
                self.data[i] = self.data[i + 1]
        self.size -= 1
        self._check_decrease()
        return self.data


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        index1 = int(index1)
        index2 = int(index2)
        self._check_bounds(index1)
        self._check_bounds(index2)
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp
        return self.data



###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    data = []
    for i in range(size):
        data.append(None)
    return data


def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    for i in range(size):
        dest[i] = source[i]
    return dest


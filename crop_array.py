"""Array resizing/cropping algorithm."""


class GridArray:
    """Create a two dimensional array with numbered values or 0."""

    def __init__(self, size, empty=False, values=None):
        """Create the array itself as a list of lists."""
        if size % 2 != 0:
            raise ValueError("Grid sizes must be even integers.")

        self.__size = size
        self.__grid = [
            # x will be 0 for an empty grid else the values
                      [x if not empty else 0 for x in range(self.__size ** 2)]
            # Second list comp splits the above list into the rows [:] splicing
                      [self.__size * i:self.__size * (i + 1)]
            # Values is used to store custom values from a list
            for i in range(self.__size)] if values is None else values

    def __str__(self):
        """Override str to print the grid values in grid form."""
        result = ''
        for i in self.__grid:
            for j in i:
                result += f"{j:02}" + ' '
            result += '\n'
        return result

    def __len__(self):
        """Override len to show grid size, all grids are square."""
        return self.__size

    def values(self):
        """Return the list of list with grid values."""
        return self.__grid  # list of list of the array values


def crop(big_array, small_array_size):
    """Crops a larger array and keeps the centered values."""
    # crop is the amount that needs to be cropped
    crop = (len(big_array) - small_array_size) // 2
    # big_values is already cropped by rows
    big_values = big_array.values()[crop:-crop]
    # now big_values is cropped by columns
    small_values = [x[crop:-crop] for x in big_values]
    return GridArray(small_array_size, False, small_values)


big = GridArray(8)
small = crop(big, 4)
print(big)
print(small)

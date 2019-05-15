<<<<<<< HEAD
'''
Created on Dec 27, 2018

@author: omid
A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love rectangles. They suspect finding that intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook or Obama or something.
'''


import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    left_x, width = find_x_overlap(rect1, rect2)
    bottom_y, height = find_y_overlap(rect1, rect2)
    overlap = {}
    # to have a rectangular in common both width and height of the rectangular should be greater than zero!!
    if width and height:
        overlap['left_x'] = left_x
        overlap['width'] = width
        overlap['bottom_y'] = bottom_y
        overlap['height'] = height
    else:
        overlap['left_x'] = None
        overlap['width'] = None
        overlap['bottom_y'] = None
        overlap['height'] = None

    return overlap

# As the logic for both x and y is the same we can have only one range_overlap_finder!!   
def find_x_overlap(rec1, rec2):
    start_x1 = rec1['left_x']
    start_x2 = rec2['left_x']
    end_x1 = start_x1 + rec1['width']
    end_x2 = start_x2 + rec2['width']
    highest_start_point = max(start_x1, start_x2)
    lowest_end_point = min(end_x1, end_x2)
    if highest_start_point < lowest_end_point:
        # There is a overlap
        start_x_overlap = highest_start_point
        width_overlap = lowest_end_point - highest_start_point
    else:
        return (None, None)
    return (start_x_overlap, width_overlap)
    
def find_y_overlap(rec1, rec2):
    start_y1 = rec1['bottom_y']
    start_y2 = rec2['bottom_y']
    end_y1 = start_y1 + rec1['height']
    end_y2 = start_y2 + rec2['height']
    highest_start_point = max(start_y1, start_y2)
    lowest_end_point = min(end_y1, end_y2)
    if highest_start_point < lowest_end_point:
        start_y_overlap = highest_start_point
        height_overlap = lowest_end_point - highest_start_point
    else:
        return (None, None)
    return (start_y_overlap, height_overlap)


















# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


=======
'''
Created on Dec 27, 2018

@author: omid
A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love rectangles. They suspect finding that intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook or Obama or something.
'''


import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    left_x, width = find_x_overlap(rect1, rect2)
    bottom_y, height = find_y_overlap(rect1, rect2)
    overlap = {}
    # to have a rectangular in common both width and height of the rectangular should be greater than zero!!
    if width and height:
        overlap['left_x'] = left_x
        overlap['width'] = width
        overlap['bottom_y'] = bottom_y
        overlap['height'] = height
    else:
        overlap['left_x'] = None
        overlap['width'] = None
        overlap['bottom_y'] = None
        overlap['height'] = None

    return overlap

# As the logic for both x and y is the same we can have only one range_overlap_finder!!   
def find_x_overlap(rec1, rec2):
    start_x1 = rec1['left_x']
    start_x2 = rec2['left_x']
    end_x1 = start_x1 + rec1['width']
    end_x2 = start_x2 + rec2['width']
    highest_start_point = max(start_x1, start_x2)
    lowest_end_point = min(end_x1, end_x2)
    if highest_start_point < lowest_end_point:
        # There is a overlap
        start_x_overlap = highest_start_point
        width_overlap = lowest_end_point - highest_start_point
    else:
        return (None, None)
    return (start_x_overlap, width_overlap)
    
def find_y_overlap(rec1, rec2):
    start_y1 = rec1['bottom_y']
    start_y2 = rec2['bottom_y']
    end_y1 = start_y1 + rec1['height']
    end_y2 = start_y2 + rec2['height']
    highest_start_point = max(start_y1, start_y2)
    lowest_end_point = min(end_y1, end_y2)
    if highest_start_point < lowest_end_point:
        start_y_overlap = highest_start_point
        height_overlap = lowest_end_point - highest_start_point
    else:
        return (None, None)
    return (start_y_overlap, height_overlap)


















# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
unittest.main(verbosity=2)
import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles


    ttx, tty = 0,0
    gg = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    if(rect2['left_x']>=rect1['left_x'] and rect2['left_x']<=rect1['left_x']+rect1['width']):
    	ttx += 1

    if (rect2['left_x']+rect2['width']>=rect1['left_x'] and rect2['left_x']+rect2['width']<=rect1['left_x']+rect1['width']):
    	ttx += 1

    if(rect2['bottom_y']>=rect1['bottom_y'] and rect2['bottom_y']<=rect1['bottom_y']+rect1['height']):
    	tty += 1
    
    if (rect2['bottom_y']+rect2['height']>=rect1['bottom_y'] and rect2['bottom_y']+rect2['height']<=rect1['bottom_y']+rect1['height']):
    	tty += 1



    if(rect1['width'] == rect2['left_x']-rect1['left_x']) or (rect2['width'] == rect1['left_x']-rect2['left_x']):
    	return gg
    elif(rect1['height'] == rect2['bottom_y']-rect1['bottom_y']) or (rect2['height'] == rect1['bottom_y']-rect2['bottom_y']):
    	return gg
    else:
    	if(ttx==0 and tty==0):
    		return gg
    	else:
    		if(rect1['left_x']<=rect2['left_x']):
    			xx = rect2['left_x']
    			gg['left_x'] = rect2['left_x']
    			if(rect2['left_x']+rect2['width']>=rect1['width']+rect1['left_x']):
    				ww = rect1['width']+rect1['left_x']-rect2['left_x']
    				gg['width'] = rect1['width']+rect1['left_x']-rect2['left_x']
    			else:
    				ww = rect2['width']
    				gg['width'] = rect2['width']
    		else:
    			xx = rect1['left_x']
    			gg['left_x'] = rect1['left_x']
    			if(rect1['left_x']+rect1['width']>=rect2['width']+rect2['left_x']):
    				ww = rect2['width']+rect2['left_x']-rect1['left_x']
    				gg['width'] = rect2['width']+rect2['left_x']-rect1['left_x']
    			else:
    				ww = rect1['width']
    				gg['width'] = rect1['width']
    		if(rect1['bottom_y']<=rect2['bottom_y']):
    			yy = rect2['bottom_y']
    			gg['bottom_y'] = rect2['bottom_y']
    			if(rect2['bottom_y']+rect2['height']>=rect1['height']+rect1['bottom_y']):
    				hh = rect1['height']+rect1['bottom_y']-rect2['bottom_y']
    				gg['height'] = rect1['height']+rect1['bottom_y']-rect2['bottom_y']
    			else:
    				hh = rect2['height']
    				gg['height'] = rect2['height']
    		else:
    			yy = rect1['bottom_y']
    			gg['bottom_y'] = rect1['bottom_y']
    			if(rect1['bottom_y']+rect1['height']>=rect2['height']+rect2['bottom_y']):
    				hh = rect2['height']+rect2['bottom_y']-rect1['bottom_y']
    				gg['height'] = rect2['height']+rect2['bottom_y']-rect1['bottom_y']
    			else:
    				hh = rect1['height']
    				gg['height'] = rect1['height']
    		return gg



















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



        def test_overlap_edges(self):
	        rect1 = {
	            'left_x': 1,
	            'bottom_y': 0,
	            'width': 5,
	            'height': 4,
	        }
	        rect2 = {
	            'left_x': 2,
	            'bottom_y': 3,
	            'width': 3,
	            'height': 4,
	        }
	        expected = {
	            'left_x': 2,
	            'bottom_y': 3,
	            'width': 3,
	            'height': 1,
	        }
	        actual = find_rectangular_overlap(rect1, rect2)
	        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
from leetcode.heap.median_finder import MedianFinder


def test_median_finder():
    median_finder = MedianFinder()
    median_finder.add_num(1)
    median_finder.add_num(2)
    assert median_finder.find_median() == 1.5
    median_finder.add_num(3) 
    assert median_finder.find_median() == 2.0
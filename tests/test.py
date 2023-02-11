from mypackage import myModule

def test_top_n():

    """make sure top_n works correctly
    """

    assert myModule.top_n([8,3,2,7,4]) == [8,7,4], "Incorrect"
    assert myModule.top_n([10, 7, 2, 9, 8]) == [10, 9, 8], "Incorrect"
    
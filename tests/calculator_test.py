from main import inc

def inc(x_value):
    """Increment function adds one to the x_value"""
    return x_value + 1
def test_answer():
    """This tests the function"""
    assert inc(4) == 5
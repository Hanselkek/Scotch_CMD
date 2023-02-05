MIN_SIZE = 1

def set_previous(a: list):
    assert len(a) >= MIN_SIZE, AssertionError
    a.pop()
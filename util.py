MIN_SIZE = 1

def get_previous(a: list):
    assert len(a) >= 1, AssertionError
    a.pop()
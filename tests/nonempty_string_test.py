from main import is_non_empty_string


def test_nonempty_string():
    empty_string = "   "
    normal_string = " hello   "
    newline_string = "\n   "
    assert is_non_empty_string(empty_string) == False
    assert is_non_empty_string(normal_string) == True
    assert is_non_empty_string(newline_string) == False

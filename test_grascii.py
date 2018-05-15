import grascii as G


def test_make_node():
    assert G.make_node('Test') == '+------+\n| Test |\n+------+'

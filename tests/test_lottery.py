from backend.lottery import lucky

def test_lucky():
    assert lucky(5) == "SORRY"
    assert lucky(15) == "WON"

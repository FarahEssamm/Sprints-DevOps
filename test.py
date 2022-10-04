import sprints as sp


def test1():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1.1, 2.2, 3.4, 5.5, 10.1]
    result = sp.myFunc(l1, l2)
    assert result[0] == (2+4+6) / 3, f"Should be {(2+4+6) / 3}"
    assert result[1] == 10.1, "Should be 10.1"


def test2():
    l1 = [10, 20, 30, 40, 50, 60]
    l2 = [-230.0, -102.0, 1.0, -10.0]
    result = sp.myFunc(l1, l2)
    assert result[0] == (10+20+30+40+50+60) / 6, f"Should be {(10+20+30+40+50+60) / 6}"
    assert result[1] == 1.0, "Should be 1.0"


def test3():
    l1 = [1, 2, 3, "hello", "hel", 'h', 1.0, 2.0, 4, 5, 6]
    l2 = [1.1, "bishoy", 1, 2.2, 100, 3.4, 5.5, 10.1]
    result = sp.myFunc(l1, l2)
    assert result[0] == (2+4+6) / 3, f"Should be {(2+4+6) / 3}"
    assert result[1] == 10.1, "Should be 10.1"


if __name__ == "__main__":
    test1()
    test2()
    test3()
    print("Finished testing - everything passed")

from Dean.video.functions.bigger import bigger


def test_bigger():
    assert bigger(34, 78) == 78
    assert bigger(54, 23) == 54
    assert bigger(-12, 0) == 0

    print("All tests passed 3/3")


if __name__ == '__main__':
    test_bigger()

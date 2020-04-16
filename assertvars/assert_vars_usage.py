from assertvars.assert_vars import show_vars


def foo(a, b):
    try:
        assert a + b < 1, "Wrong values!"
    except AssertionError as e:
        show_vars(e)


if __name__ == "__main__":
    foo(1, 2)

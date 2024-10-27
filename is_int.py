def is_int(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        int(s)
        return True
    except:
        return False


if __name__ == "__main__":
    # тесты
    if True:
        s = ""
        print(f"{s}->{is_int(s)}")

        s = None
        print(f"{s}->{is_int(s)}")

        s = "1"
        print(f"{s}->{is_int(s)}")

        s = 2
        print(f"{s}->{is_int(s)}")

        s = "0.3"
        print(f"{s}->{is_int(s)}")

        s = "четыре"
        print(f"{s}->{is_int(s)}")

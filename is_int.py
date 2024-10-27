def is_int3(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        if type(s) is int:
            return True
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def is_int4(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


if __name__ == "__main__":
    # тесты

    # тест быстродействия функции
    import time

    n = 10000

    def test(s, f):
        t = 0.0
        res = f(s)
        start_time = time.time()
        for i in range(n):
            f(s)
        t += time.time() - start_time
        print("%5s->%s %.0f ms (%5s)" % (s, res, t*1000, f.__name__))


    if True:
        test("", is_int3)
        test(None, is_int3)
        test("1", is_int3)
        test(2, is_int3)
        test("0.3", is_int3)
        test("f", is_int3)

        print('')

        test("", is_int4)
        test(None, is_int4)
        test("1", is_int4)
        test(2, is_int4)
        test("0.3", is_int4)
        test("f", is_int4)

        """
     ->False 2 ms (is_int3)
 None->False 14 ms (is_int3)
    1->True 5 ms (is_int3)
    2->True 1 ms (is_int3)
  0.3->False 2 ms (is_int3)
    f->False 2 ms (is_int3)

     ->False 2 ms (is_int4)
 None->False 2 ms (is_int4)
    1->True 4 ms (is_int4)
    2->True 2 ms (is_int4)
  0.3->False 2 ms (is_int4)
    f->False 2 ms (is_int4)
        """

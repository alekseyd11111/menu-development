def is_int(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        int(s)
        return True
    except:
        return False


def is_int2(s):
    """
    Проверка на то, что s - целое число
    """
    try:
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
        test("", is_int)
        test(None, is_int)
        test("1", is_int)
        test(2, is_int)
        test("0.3", is_int)
        test("f", is_int)

        print('')

        test("", is_int2)
        test(None, is_int2)
        test("1", is_int2)
        test(2, is_int2)
        test("0.3", is_int2)
        test("f", is_int2)

        """
     ->False 18 ms (is_int)
 None->False 12 ms (is_int)
    1->True 3 ms (is_int)
    2->True 2 ms (is_int)
  0.3->False 20 ms (is_int)
    f->False 19 ms (is_int)

     ->False 18 ms (is_int2)
 None->False 14 ms (is_int2)
    1->True 3 ms (is_int2)
    2->True 2 ms (is_int2)
  0.3->False 17 ms (is_int2)
    f->False 17 ms (is_int2)
        """
        
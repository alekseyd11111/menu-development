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
    if False:
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

    # тест быстродействия функции
    import time
    def test(s, f, n):
        t = 0.0
        res = f(s)
        start_time = time.time()
        for i in range(n):
            f(s)
        t += time.time() - start_time
        print("%5s->%s %.0f ms (%5s)" % (s, res, t*1000, f.__name__))

    n = 10000

    if True:
        test("", is_int, n)
        test(None, is_int, n)
        test("1", is_int, n)
        test(2, is_int, n)
        test("0.3", is_int, n)
        test("f", is_int, n)
        
        """
             ->False 16 ms (is_int)
         None->False 10 ms (is_int)
            1->True 3 ms (is_int)
            2->True 2 ms (is_int)
          0.3->False 15 ms (is_int)
            f->False 16 ms (is_int) 
        """
        
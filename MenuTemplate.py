# Exception
class ExMenu(Exception):
    """
    Класс ошибок для MenuTemplate
    """
    def __init__(self, *args, **kwargs):
        message = self._do_message(*args, **kwargs)
        # тут можно логировать ошибки в файл
        super().__init__(message)

    def _do_message(self, *args, **kwargs) -> str:
        """
        Сообщение об ошибке.
        Переопределяется в потомках
        """
        return ''


class ExMenuInvalidKey(ExMenu):
    """
    Повтор названия пункта меню
    """
    def _do_message(self, key):
        return f'the key "{key}" already exists'


class ExMenuEmpty(ExMenu):
    """
    Запуск меню без пунктов
    """
    def _do_message(self):
        return 'Меню пустое'
# Exception-------------------


class MenuTemplate:
    """
    Класс для создания меню
    """

    def __init__(self,
                 start_message="",
                 key_separator=".",
                 invalid_key_message='invalid_key'):
        self._message_start = start_message
        self._key_separator = key_separator
        self._message_invalid_key = invalid_key_message

        # пункты меню
        self._items = {}

    def add_item(self,
                 key: str,
                 message: str,
                 command=None,
                 is_exit=False):
        """
        Добавление пункта меню
        :param key:     уникальный символ пункта меню
        :param message: текст пункта меню
        :param command: функция, которая вызовется
        :param is_exit: выход из меню после выполнения этого пункта
        """
        if key in self._items:
            raise ExMenuInvalidKey(key)

        if command is None:
            def _pass():
                pass
            command = _pass

        self._items[key] = {'message': message, 'command': command, 'is_exit': is_exit}

    def start(self):
        """
        Запуск вечного цикла меню
        """
        if len(self._items) == 0:
            raise ExMenuEmpty()

        is_exit = False
        while not is_exit:
            # печать меню
            self._show()
            # Ввод пункта меню
            key = input()
            if key in self._items:
                # Выбор действия
                self._items[key]['command']()
                # выход из меню
                is_exit = self._items[key]['is_exit']
            else:
                print(self._message_invalid_key)

    def _show(self):
        """
        Вывод в консоль названия меню и его пунктов
        """
        print(self._message_start)
        for key, value in self._items.items():
            print(f"{key}{self._key_separator} {value['message']}")


if __name__ == "__main__":

    menu = MenuTemplate(start_message="menu_main",
                        key_separator=")"
                        )

    # menu.start()
    # menu.add_item("1", "f11(x)", lambda: print("f11"))
    menu.add_item("1", "f1(x)", lambda: print("f1"))
    menu.add_item("2", "f2(x)", lambda: print("f2"))
    menu.add_item("0", "exit", is_exit=True)
    # print(menu._items)
    # menu.items["2"]['command']()
    menu.start()

    exit(0)

class MenuTemplate:
    """
    Класс для создания меню
    """

    def __init__(self,
                 start_message="",
                 key_separator=".",
                 invalid_key_message='invalid_key'):
        self.message_start = start_message
        self.key_separator = key_separator
        self.message_invalid_key = invalid_key_message

        # пункты меню
        self.items = {}

    # 5)
    # menu.add_item("1", "f11(x)", lambda: print("f11"))
    # menu.add_item("1", "f1(x)", lambda: print("f1"))
    def add_item(self,
                 key: str,
                 message: str,
                 command=None,
                 is_exit=False):
        """
        Добавление пункта меню
        :param key:     уникальный символ пункта меню
        :param message: текст пункта меню
        :param command: функция, которая вызовиться
        :param is_exit: выход из меню после выполненения этого пункта
        """
        if key in self.items:
            raise Exception(f'the key "{key}" already exists')

        if command is None:
            def _pass():
                pass
            command = _pass

        self.items[key] = {'message': message, 'command': command, 'is_exit': is_exit}

    # 6)
    def start(self):
        """
        Запуск вечного цикла меню
        """
        is_exit = False
        while not is_exit:
            # печать меню
            self.show()
            # Ввод пункта меню
            key = input()
            if key in self.items:
                # Выбор действия
                self.items[key]['command']()
                # выход из меню
                is_exit = self.items[key]['is_exit']
            else:
                print(self.message_invalid_key)

    def show(self):
        """
        Вывод в консоль названия меню и его пунктов
        """
        print(self.message_start)
        for key, value in self.items.items():
            print(f"{key}{self.key_separator} {value['message']}")


if __name__ == "__main__":

    menu = MenuTemplate(start_message="menu_main",
                        key_separator=")"
                        )
    #menu.add_item("1", "f11(x)", lambda: print("f11"))
    menu.add_item("1", "f1(x)", lambda: print("f1"))
    menu.add_item("2", "f2(x)", lambda: print("f2"))
    menu.add_item("0", "exit", is_exit=True)
    menu.start()

    #menu.items["2"]['command']()
    exit(0)

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.unique = []
        self.items = iter(items)
        if len(kwargs) == 0:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs.values()
        pass

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            item = self.items.__next__()
            smth = None
            if self.ignore_case and type(item) is str:
                smth = item.lower()
            else:
                smth = item
            if smth not in self.unique:
                self.unique.append(smth)
                return smth
        pass

    def __iter__(self):
        return self
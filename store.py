from storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, qnt):
        if self.get_free_space() < qnt:
            return False

        if name in self.get_unique_items_count():
            self._items[name] += qnt
        else:
            self._items[name] = qnt

        return True

    def remove(self, name, qnt):
        if name not in self.get_unique_items_count():
            return False

        new_qnt = self._items[name] - qnt

        if new_qnt < 0:
            new_qnt = 0

        self._items[name] = new_qnt

        return True

    def get_free_space(self):
        total_qnt = sum([x for x in self._items.values()])

        free_space = self._capacity - total_qnt

        return free_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        items_names = [item for item in self._items.keys()]
        return items_names

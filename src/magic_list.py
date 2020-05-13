from typing import List


class MagicList(list):

    def __init__(self, cls_type: type = None):
        self.cls_type = cls_type
        if cls_type is None:
            self._list = []
        else:
            self._list: List[cls_type] = []
        list.__init__(self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, y):
        return self._list[y]

    def __call__(self):
        return self._list

    def __setitem__(self, key, value):
        if len(self._list) == key:
            self._list.append(value)
        else:
            self._list[key] = value

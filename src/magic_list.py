

class MagicList(list):

    def __init__(self, cls_type: type = None):
        self.cls_type = cls_type
        list.__init__(self)

    def __getitem__(self, y):
        if len(self) == y and self.cls_type is not None:
            self.append(self.cls_type())
        return super().__getitem__(y)

    def __setitem__(self, key, value):
        if len(self) == key:
            if self.cls_type is not None:
                self.append(self.cls_type())
            else:
                self.append(value)
        else:
            self[key] = value

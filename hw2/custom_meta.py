class CustomMeta(type):
    def __new__(mcs, name, bases, attrs, **extra_kwargs):
        new_attrs = {}
        for attr, val in attrs.items():
            if not attr.startswith("__"):
                new_attrs[f"custom_{attr}"] = val
            else:
                new_attrs[attr] = val
        return super().__new__(mcs, name, bases, new_attrs)

    def __call__(cls, *args, **kwargs):
        a = super().__call__(*args, **kwargs)
        new_attrs = {}
        for attr, val in a.__dict__.items():
            if not attr.startswith("__"):
                new_attrs[f"custom_{attr}"] = val
            else:
                new_attrs[attr] = val
        a.__dict__ = new_attrs
        return a

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val
    
    def line(self):
        return 100

if __name__ == "__main__":
    inst = CustomClass(300)
    print(
    inst.custom_x,
    inst.custom_val,
    inst.custom_line(),
    # inst.x,  # ошибка
    # inst.val,  # ошибка
    # inst.line(), # ошибка
    )

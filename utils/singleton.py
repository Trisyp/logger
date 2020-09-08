import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


# def singleton(cls):
#     _instance = {}
#
#     def inner():
#         if cls not in _instance:
#             _instance[cls] = cls()
#         return _instance[cls]
#     return inner

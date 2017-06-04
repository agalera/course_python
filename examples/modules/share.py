class Idgenerator():
    n = -1

    @classmethod
    def new_id(cls):
        cls.n += 1
        return cls.n

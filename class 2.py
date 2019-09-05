class Fruit:
    pass
class Orange(Fruit):
    pass
class Tste(Orange):
    pass
class good(Tste):
    pass
class how(good):
    pass
class apple(Fruit):
    pass

print(issubclass(apple,Fruit))
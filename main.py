from antigravity import geohash as g
import typing
import attrs
import antigravity, sys, abc
from deprecated import deprecated

@deprecated
@attrs.define
class MyClass:
    my_attr: list = attrs.field(default=[])


@deprecated
def dep_method():
    pass

def main():
    print("hello dangerous world")

    my_class = MyClass()
    my_class2 = MyClass()
    my_list = typing.List()
    dep_method()

if __name__ == "__main__":
    main()

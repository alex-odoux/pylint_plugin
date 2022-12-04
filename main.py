from antigravity import geohash as g
import typing
import attrs
import antigravity, sys, abc


@attrs.define
class MyClass:
    my_attr: list = attrs.field(default=[])


def main():
    print("hello dangerous world")

    my_class = MyClass()
    my_class2 = MyClass()
    my_list = typing.List()


if __name__ == "__main__":
    main()

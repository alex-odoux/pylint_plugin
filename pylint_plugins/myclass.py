

def example_function(a:str="", b:str="", c:str=""):
    print(a)




def old_way_to_call():
    example_function(b="x", c="z")


def new_way_to_call():
    example_function(a="yes")


def try_find_the_issue():
    example_function(b="xxx",c="xxxxxx")
    example_function(b="xxx", c="xxxxxx")
    example_function(b="xxx", c="xxxxxx")


old_way_to_call()


old_way_to_call()


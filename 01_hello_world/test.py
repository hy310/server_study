@decorator
def test():
    print("hello")

print("pre")
test()
print("post")

def decorator(func):
    print("pre")
    func()
    print("post")
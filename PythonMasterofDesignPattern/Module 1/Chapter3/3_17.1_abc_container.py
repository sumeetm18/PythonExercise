from _collections_abc import Container

class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

odd_container = OddContainer()        
print(isinstance(odd_container, Container))
print(issubclass(OddContainer, Container))

print(3 in odd_container)
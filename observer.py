# implement observer pattern
from abc import ABCMeta, abstractmethod

# Subject
class Subject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# ConcreteSubject
class ConcreteSubject(Subject):
    def __init__(self):
        self.product = []
        self._observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        print("Notifying observers...{length} observers in total".format(length=len(self._observers)))
        for observer in self._observers:
            observer.update(self)    
    
    def add_product(self, product):
        self.product.append(product)
        self.notify()
        
    def receive_product(self, product):
        self.product.remove(product)
        self.notify()
        
    def get_product(self):
        return self.product

# Observer
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, subject):
        pass

# User
class User(Observer):
    def __init__(self, name):
        self.name = name
        self.product = []
    
    def update(self, subject):
        self.product = subject.get_product()
        print("User {name} has {length} products".format(name=self.name, length=len(self.product)))
        
    def buy_product(self, product):
        self.product.append(product)
        print("User {name} has bought {product}".format(name=self.name, product=product))
        
    def receive_product(self, product):
        self.product.remove(product)
        print("User {name} has received {product}".format(name=self.name, product=product))
        
    def get_product(self):
        return self.product

# Supplier
class Supplier(Observer):
    def __init__(self, name, subject):
        self.name = name
        self.product = []
        self.subject = subject
        self.subject.register(self)
        
    def add_product(self, product):
        self.product.append(product)
        self.subject.add_product(product)
        print("Supplier {name} has added {product}".format(name=self.name, product=product))
        
    def update(self, subject):
        self.product = subject.get_product()
        print("Supplier {name} has {length} products".format(name=self.name, length=len(self.product)))
    
    def receive_product(self, product):
        self.product.remove(product)
        self.subject.receive_product(product)
        print("Supplier {name} has received {product}".format(name=self.name, product=product))
    
    def get_product(self):
        return self.product

# main
if __name__ == "__main__":
    
    # create subject
    subject = ConcreteSubject()
    
    # create observers
    user1 = User("user1")
    
    # create supplier
    supplier1 = Supplier("supplier1", subject)
    
    # receive product
    supplier1.add_product("product1")
    
    # buy product
    user1.buy_product("product1")
        
            



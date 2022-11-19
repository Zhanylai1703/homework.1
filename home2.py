# Создайте иерархию классов для описания фауны со следующими требованиями:

# Обязательное присутствие классов птиц, рыбы и млекопитающих. Напишите для них методы и парамметры
#  свойственные для животных этих классов. Так же обязательное присутствие классов хищников и травоядных. 
# У классов хищник и травоядное обязательно должен быть метод eat. Этот метод должен показывать, чем питается животное.

# Создайте классы сокол, пингвин, форель, кит. Наследуйте эти классы от вышеуказанных классов, при наследовании обратите 
# внимание на природные свойства животных этих классов. Если есть необходимость, перепишите методы родителя для того чтобы 
# эти методы соответствовали свойствам животного. Создайте экземпляры классов сокол, пингвин, форель, кит. 
# Вызовите все доступные им методы

# Пример:

# >>>p = Penguin(type='royal', age='1 year')
# >>>p.eat()
# I eat fish
# >>>p.can_swim()
# True
# >>>p.can_fly()
# I cannot fly

class birds:
    
    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def fly(self):
        print(f'{True}')
        
    def swim(self):
        print(f'{False}')
    
    def run(self):
        print(f'{False}') 

class fishes:

    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def swim(self):
        print(f'{True}')
        
    def fly(self):
        print(f'{False}')
    
    def run(self):
        print(f'{False}')

class mammals:

    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def run(self):
        print(f'{True}')
        
    def swim(self):
        print(f'{False}')
    
    def fly(self):
        print(f'{False}') 



class predator:
    
    def eat(self):
        print('I hunt and eat meat')
    
class herbivores:

    def eat(self):
        print('I eat only the grasses')


class Falcon(birds, predator):
    pass

class Pengiun(birds, predator):
    def swim(self):
        print(f'{True}')

class Trout(fishes, predator):
    pass

class Whale(mammals, predator):
    def swim(self):
        print(f'{True}')
    pass
    
f = Falcon("newtoni", 2)
f.eat()
f.fly()
f.swim()
f.run()

p = Pengiun("royal", 3)
p.eat()
p.fly()
p.swim()
p.run()

t = Trout("royal", 4)
t.eat()
t.fly()
t.swim()
t.run()

w = Whale("Blue Whale", 20)
w.eat()
w.fly()
w.swim()
w.run()
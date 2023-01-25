class Test:
    degree = 3

    def __init__(self, age, year):
        self.age = age
        self.year = year

    def drop_down(self):
        self.degree -= 1

    def move_up(self):
        self.degree += 1


new = Test(3, 4)
print(new.degree)
new.drop_down()
print(new.degree)
Test.degree = 6
print(new.degree)
neww = Test(6, 7)
print(neww.degree)

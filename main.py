class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:list, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self, name):
        # self.name = name
        print("This is my updated name", str(name))

    def change_age(self, newAge):
        # self.name = newAge
        print("This is my updated age", int(newAge))

    def add_track(self, tracks):
        self.tracks.append(tracks)
        print("This are my updated tracks",list(self.tracks))

    def get_score(self):
        print("This is my score", float(self.score))


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

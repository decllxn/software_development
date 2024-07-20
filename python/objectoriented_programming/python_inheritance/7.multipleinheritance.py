# Let's use a more realistic example involving real life instances

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Employee:
    def __init__(self, company, job_title):
        self.company = company
        self.job_title = job_title

    def work(self):
        return f"I work at {self.company} as a {self.job_title}."

class SportsPerson:
    def __init__(self, sport, achievements):
        self.sport = sport
        self.achievements = achievements

    def play(self):
        return f"I play {self.sport} and have achieved {self.achievements}."

class PersonEmployeeSportsPerson(Person, Employee, SportsPerson):
    def __init(self, name, age, company, job_title, sport, achievements):
        Person.__init__(self, name, age)
        Employee.__init__(self, company, job_title)
        SportsPerson.__init__(self, sport, achievements)

# Example usage

Declan = PersonEmployeeSportsPerson("Declan Munene", 20, "Microsoft", "Software Engineer", "Football", "3 trophies")

print(Declan.introduce())
print(Declan.work())
print(Declan.play())

import random

feet_in_mile = 5200
meters_in_kilometer = 1000

beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]
# pass a file name, it'll give you extension of a file

def roll_dice(num):
    return random.randint(1, num)


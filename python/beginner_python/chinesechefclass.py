# This is where we will be practising
# Say the chinese chef can do everything the other chef can do
from chefclass import Chef
class ChineseChef(Chef): # I have imported the functions from chef class
    # This is called inheritance
    # Any functions written here will override inherited functions
    #for example
      # make_special_dish

    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")
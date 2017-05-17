class animalia(object):
    '''animalia has two class attributes: level and heterotroph; they can be
       accessed by "self.level" and "self.heterotroph" inside the class and
       by "instancevariablename.level" and "instancevariablename.heterotroph"
       just like instance variables.
    '''
    level = "kingdom"
    heterotroph = True
    
class plantae(object):
    level = "kingdom"
    autotroph = True
    
class chordata(animalia):
    level = "phylum"
    notochord = True
    
class dinosauria(chordata):
    level = "clade"
    legs = 4
    
    def eat(self, food):
        '''Instance method which outputs a description of how dinosaurs eat.
        The first parameter is by convention called self, but there is no
        restriction on its name.'''
        print("Eating {f} with a mouth.".format(f=str(food)))
        
class tyrannoraptora(dinosauria):
    level = "clade"
    hollow_tail = True
    
class aves(tyrannoraptora):
    level = "taxonomical class"
    heart_chambers = 4
    
    def __init__(self, flight):
        '''When instantiating an aves we want to define whether it is capable
        of flight or not and save this information in an instance attribute
        "flight", note that instance attributes always need to be prefixed by
        "self." or whatever the name of the first parameter of the method is.
        Unprefixed variables become method local and cannot be seen from the
        outside.
        '''
        self.flight = flight
        
magpie=aves(True)
print("A {name} is an instance of {klass}.".format(name="magpie",
                                                   klass=magpie.__class__.__name__))
inheritancelist = magpie.__class__.mro()
for idx,_class in enumerate(inheritancelist[:-1]):
    print("The class {child} derives from {parent}.".format(
        child=_class.__name__, parent=inheritancelist[idx+1].__name__))

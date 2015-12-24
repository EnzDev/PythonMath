class Complex:
    '''
    Class type : Math class
    Complex implementation with methods :
        * initialisation
        * representation
    '''
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __repr__(self):
        if i==0:
            ret = str(self.r)
        else:
            ret = str(self.i)+"i" if r==0 else str(self.r)+"+"+str(self.i)+"i"
        return ret

class Matrix:
    '''
    Class type : Math class
    Matrix implementation with methods :
        * initialisation
        * representation
        * addition
        * substraction
        * negation
        * multiplication
        * transmutation (__invert__)
        * contain (python "in" funtion)
        * setitem (via matrix[(i,j)]=value)
        * len ()
    '''
    def __init__(self, component):
        assert type(component) is list, str(type(component))+" n'est pas suporté par <class 'Matrix'>, n'est pas de type <class 'list'>"

        h = len(component)
        assert h>0, "Empty matrix"

        l = max([len(i) for i in component]) # Search the max row size
        assert l>0, "Empty matrix"

        for i in range(len(component)): # Look in the entire matrix
            component[i]=component[i]+[0]*(l-len(component[i])) # Add missing 0

        self.comp = component # Correctly shaped matrix (fill w missing 0)
        self.l = l # Usefull because its often called in the Matrix class
        self.h = h # Same

    def __repr__(self):
        return "\n".join(["\t".join([str(n) for n in i]) for i in self.comp])

    ## magic methods
    #  Main magic methods
    def __add__(self, other):
        assert self.h==other.h and self.l==other.l, "Size error"
        return Matrix([[self.comp[i][j]+other.comp[i][j] for j in range(self.l)] for i in range(self.h)])

    def __sub__(self, other):
        return self+(-other)

    def __neg__(self):
        return self.scal(-1)

    def __mul__(self, other):
        assert self.l==other.h and self.h==other.l, "Size error"
        return Matrix([[sum([self.comp[rowN][i]*other.comp[i][colN] for i in range(self.l)]) for colN in range(other.l)] for rowN in range(self.h)])
        '''
        The line above is a little bit too long so i split it here just for reader

        for rowN in range(self.h):
            for colN in range(other.l): #Change the name just for readability (cuz it's same as self.h)
                for i in range(self.l)  #or range(other.h)
                    self.comp[rowN][i]*other.comp[i][colN]
        '''

    def __invert__(self):
        return Matrix([[self.comp[j][i] for j in range(self.h)] for i in range(self.l)])

    # Additional methods
    transpose = __invert__ #Create an alias of ~self

    def __contains__(self, item):
        checklist = set()
        for i in self.comp:  # Create a set with one occurence of each item in the matrix
            checklist = checklist | set(i)
        return (item in checklist) #Check item is in the set (python know this)

    def __setitem__(self, key, value): #use to redifine a value
        assert type(key) is tuple and len(key)==2, "The key is badly set please use mat[(i,j)]"
        self.comp[key[0]][key[1]] = value
        return self
    set = __setitem__
    ## Other methods
    def len(self):
        return (self.h,self.l)

    def scal(self, scal):
        return Matrix([[scal*self.comp[i][j] for j in range(self.l)] for i in range(self.h)])

## Actually there are too many assertions here ! (do not see that py in Pyzo, it's ugly)

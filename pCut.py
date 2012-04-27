# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

import re

class Plasmid:
    #class variables
    
    #class methods
    def __init__(self, sequence):
        self.sequence = sequence
        
    def cut(self, RE_site):
        fragments = self.sequence.split(RE_site)
        n = len(fragments)
        for x in range (n-1):
            fragments[x] += RE_site
        fragments[n-1] += fragments[0]
        fragments[0] = fragments[n-1]
        del(fragments[n-1])
        
        return fragments
    
    def number_of_fr(self, RE_site):
        return len(self.cut(RE_site))
        
    def fr_length(self, RE_site):
        x = self.cut(RE_site)
        # Use list comprehension.
        return [len(string) for string in x]
    

    

    

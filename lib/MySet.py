class MySet:
  
    def __init__(self, enumerable = None):

        if enumerable is None:
            enumerable = []
        self.dictionary = {}

        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value]=True  #Add a value as a key on the dictionary
        return self                  # Return the updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self
    
    def __str__(self):
         return f'MySet: {{{",".join(str(key) for key in self.dictionary.keys())}}}'


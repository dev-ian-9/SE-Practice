class Director(object):
    
    def __init__(self, builder):
        self.__builder = builder
        
    def construct(self):
        self.__builder.make_title("Greeting")
        self.__builder.make_string("From the morning to the afternoon")
        self.__builder.make_items(["Good morning", "Hello"])
        self.__builder.make_string("In the evening")
        self.__builder.make_items(["Good evening", "Good night", "Good bye"])
        self.__builder.close()
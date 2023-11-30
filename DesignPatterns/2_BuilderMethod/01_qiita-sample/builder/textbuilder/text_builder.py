from builder.builder import Builder

class TextBuilder(Builder):
    
    def __init__(self):
        self.buffer = []
        
    def make_title(self, title):
        self.buffer.append("=================")
        self.buffer.append(f"{title}\n")
        self.buffer.append("\n")
        
    def make_string(self, str):
        self.buffer.append(f"*** {str} ***\n")
        
    def make_items(self, items):
        for i in items:
            self.buffer.append(f"- {i}\n")
            
    def close(self):
        self.buffer.append("=================")
        
    def getResult(self):
        return "".join(self.buffer)
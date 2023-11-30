import sys

from builder.director import Director
from builder.htmlbuilder.html_builder import HtmlBuilder
from builder.textbuilder.text_builder import TextBuilder

def startMain(opt):
    if opt == "plain":
        builder = TextBuilder()
        director = Director(builder)
        director.construct()
        result = builder.getResult()
        print(result)
        
    else:
        builder = HtmlBuilder()
        director = Director(builder)
        director.construct()
        result = builder.getResult()
        print(result)
        
        
if __name__ == "__main__":
    startMain("plain")
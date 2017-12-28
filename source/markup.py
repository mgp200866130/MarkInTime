import sys,re
import handlers
import rulers
import util


class Parser:
    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name), block)
        self.filters.append(filter)

    def parse(self,file):
        self.handler.start('document')
        for block in util.blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(rulers.ListRule())
        self.addRule(rulers.ListItemRule())
        self.addRule(rulers.TitleRule())
        self.addRule(rulers.HeadingRule())
        self.addRule(rulers.ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+)', 'mail')


handler = handlers.HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin) 



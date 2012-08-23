
#! coding: utf-8

from lxml import etree

ns = '{http://www.mediawiki.org/xml/export-0.7/}'
class TitleTarget(object):
    def __init__(self):
        self.text = []
    def start(self, tag, attrib):
        self.is_title = True if tag == '%stitle'%ns else False
    def end(self, tag):
        pass
    def data(self, data):
        if self.is_title:
            self.text.append(data.encode('utf-8'))
            #self.text.append(data)
    def close(self):
        return self.text

parser = etree.XMLParser(target = TitleTarget())

# This and most other samples read in the Google copyright data
#infile = 'jawiki-pages-meta.xml'
#infile = 'jawiki-20120806-pages-meta-current.xml'
infile = 'tmp.xml'

results = etree.parse(infile, parser)    

# When iterated over, 'results' will contain the output from 
# target parser's close() method

out = open('titles_sax.txt', 'w')
out.write('\n'.join(results))
out.close()


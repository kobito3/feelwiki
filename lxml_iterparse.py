
#! codign: utf-8

from lxml import etree

ns = '{http://www.mediawiki.org/xml/export-0.7/}'
#infile = 'jawiki-20120806-pages-meta-current.xml'
infile = 'tmp.xml'

tag = '%s%s' % (ns, 'title')
context = etree.iterparse(infile, events=('end',), tag=tag)

cnt = 0
out = open('titles_iter.txt', 'w')
#out.write('\n'.join(results))
for action, elem in context:
    out.write('%s\n' % elem.text.encode('utf-8'))
    #print elem.text.encode('utf-8')
    #print(elem.text)
    #cnt += 1
    #if cnt > 300:
    #    break

out.close()

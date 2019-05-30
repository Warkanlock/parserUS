# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup #PARSER OF HTML (pip install beautifulsoup4, html5lib, html5)
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import sys
import math
import random

reload(sys)
sys.setdefaultencoding('utf8')

#get HTM file by HTTP REQUEST
response = requests.get("https://www.govinfo.gov/content/pkg/USCODE-2017-title26/html/USCODE-2017-title26z.htm")
soup = BeautifulSoup(response.content, features="html5lib")

#delete unusefull SPAN|BR|A|DIV tags
element = soup.body.find_all(re.compile("^(?!.*(span|br|a|div)).*$"))

#example anytree
# root = Node('199A. Qualified business income')
# subsection = Node('(a) In general', parent=root)
# paragraph = Node('In the case of a taxpayer other than a corporation, there shall be allowed as a deduction for any taxable year an amount equal to the sum of—', parent=subsection)
# paragraph_child_1 = Node("(1) the lesser of—", parent=paragraph)
# paragraph_child_2 = Node("(2) the lesser of—", parent=paragraph)
# text_paragraph_child_1 = Node("(A) the combined qualified business income amount of the taxpayer, or", parent=paragraph_child_1)
# text_paragraph_child_2 = Node("(B) an amount equal to 20 percent of the excess (if any) of—", parent=paragraph_child_1)
# subsection_2 = Node("(c) Qualified business income", parent=root)
# paragraph_2 = Node("For purposes of this section—", parent=subsection_2)
# text_paragraph_2 = Node(" > (1) In general", parent=paragraph_2)


root_node = None
subsection_node = None
paragraph_node = None
subparagraph_node = None
clause_node = None
statutory_node = statutory_1_node = statutory_2_node = statutory_3_node = statutory_4_node = statutory_5_node = None
statutory_block_node = statutory_block_2_node = statutory_block_3_node = None

node_list = []
id = 0

#main loop, detect elements by his tags
for a in element:

    parts_texts = a.text.split()
    text = " "

    if(len(parts_texts) > 5):
        for b in range(0, len(parts_texts)/2):
            text += parts_texts[b] + ' '
        text += '\n'
        for b in range((len(parts_texts)/2)+1, len(parts_texts)):
            text += parts_texts[b] + ' '
    else:
        text = a.text

    id += 1

    if(a.name == 'h3'):
        root_node = Node(str(id) + ":" + a.text)
        print(root_node)
        print(a.text)
    elif(a.name == 'h4'):
        if (a['class'][0] == 'subsection-head'):
            subsection_node = Node(str(id) + ":" +text, root_node)
            print("\t" + " " + a.text)
        elif(a['class'][0] == 'paragraph-head'):
            paragraph_node = Node(str(id) + ":" + text, subsection_node)
            print("\t >" +" " + a.text)
        elif(a['class'][0] == 'subparagraph-head'):
            subparagraph_node = Node(str(id) + ":" +text, paragraph_node)
            print("\t -->"+" " + a.text)
        elif(a['class'][0] == 'clause-head'):
            clause_node = Node(str(id) + ":" + text, subparagraph_node)
            print("\t ----->" + " " + a.text)
    elif(a.name == 'p'):
        #CONDICION DE PARAGRAPH
        if a.has_attr('class'):
            if(a['class'][0] == 'statutory-body'):
                statutory_node = Node(str(id) + ":" + text, subsection_node)
                print("\t \t" +" " + a.text)
            elif(a['class'][0] == "statutory-body-1em"):
                #statutory_1_node = Node(str(id) + ":" + text, statutory_node)
                print("\t \t \t" +" " + a.text)
            elif(a['class'][0] == "statutory-body-2em"):
                #statutory_2_node = Node(str(id) + ":" + a.text.replace('"', " "), statutory_1_node)
                print("\t \t \t \t" + " " + a.text)
            elif(a['class'][0] == "statutory-body-3em"):
                #statutory_3_node = Node(str(id) + ":" + a.text.replace('"', " "), statutory_2_node)
                print("\t \t \t \t \t" + " " + a.text)
            elif (a['class'][0] == "statutory-body-4em"):
                #statutory_4_node = Node(str(id) + ":" + a.text, statutory_3_node)
                print("\t \t \t \t \t \t" + " " + a.text)
            elif (a['class'][0] == "statutory-body-5em"):
                #statutory_5_node = Node(a.text, statutory_4_node)
                print("\t \t \t \t \t \t \t" + " " + a.text)
            elif (a['class'][0] == "statutory-body-block"):
                statutory_block_node = Node(str(id) + ":" + text, subsection_node)
                print("[[ " + " " + a.text + "]]")
            elif (a['class'][0] == "statutory-body-block-2em"):
                #statutory_block_2_node = Node(a.text, statutory_block_node)
                print("[[[[ " + " " + a.text + "]]]]")
            elif (a['class'][0] == "statutory-body-block-1em"):
                #statutory_block_3_node = Node(a.text, statutory_block_2_node)
                print("[[ " + " " + a.text + "]]")
        else:
            print(" -- ")



#for pre, fill, node in RenderTree(root_node):
#    print("%s%s" % (pre, node.name))

#DotExporter(root_node, graph="graph", nodeattrfunc=lambda node : "shape=box").to_dotfile("tree.dot")
#DotExporter(root_node, graph="digraph", nodeattrfunc=lambda node: "shape=rect, nojustify=true, fontsize=10, fixedsize=false, maxiter=200, width=1.5, len=2").to_picture("tree3.png")
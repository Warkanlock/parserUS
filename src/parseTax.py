from anytree import Node, RenderTree
from anytree.exporter import JsonExporter
import datetime


class ParserTaxCode(object):

    """
    CONSTRUCTOR
    """

    def __init__(self, element, uriTemp):
        self.tagElements = element
        self.root = None
        self.URI = uriTemp

    """
    PARSE THE FILE
    """

    def parseEntire(self):
        # for other porpuse
        # nameFile = self.URI[:len(self.URI)-4]
        # namePos = nameFile.find("/html")
        # nameClean = nameFile[namePos+6:]

        root_node = None
        subsection_node = None
        paragraph_node = None
        subparagraph_node = None
        clause_node = None
        statutory_node = (
            statutory_1_node
        ) = (
            statutory_2_node
        ) = statutory_3_node = statutory_4_node = statutory_5_node = None
        statutory_block_node = statutory_block_2_node = statutory_block_3_node = None

        id = 0

        if self.tagElements:
            for a in self.tagElements:
                parts_texts = a.text.split()
                text = " "

                if len(parts_texts) > 5:
                    for b in range(0, len(parts_texts) // 2):
                        text += parts_texts[b] + " "
                    text += "\n"
                    for b in range((len(parts_texts) // 2) + 1, len(parts_texts)):
                        text += parts_texts[b] + " "
                else:
                    text = a.text

                id += 1

                if a.name == "h3":
                    if root_node is None:
                        root_node = Node("ID:" + str(id) + ":" + a.text)
                    else:
                        root_node = Node("ID:" + str(id) +
                                         ":" + a.text, root_node)
                    # print(root_node)
                    # print(a.text)
                    txt = open("data/" + a.text + ".txt", "w+")
                    txt.write(a.text + "\n")
                elif a.name == "h4":
                    if a["class"][0] == "subsection-head":
                        subsection_node = Node(
                            "ID:" + str(id) + ":" + text, root_node)
                        # print("\t" + " " + a.text)
                    elif a["class"][0] == "paragraph-head":
                        paragraph_node = Node(
                            "ID:" + str(id) + ":" + text, subsection_node
                        )
                        # print("\t >" + " " + a.text)
                    elif a["class"][0] == "subparagraph-head":
                        subparagraph_node = Node(
                            "ID:" + str(id) + ":" + text, paragraph_node
                        )
                        # print("\t -->"+" " + a.text)
                    elif a["class"][0] == "clause-head":
                        clause_node = Node(
                            "ID:" + str(id) + ":" + text, subparagraph_node
                        )
                        # print("\t ----->" + " " + a.text)
                elif a.name == "p":
                    # CONDICION DE PARAGRAPH
                    if a.has_attr("class"):
                        if a["class"][0] == "statutory-body":
                            statutory_node = Node(
                                "ID:" + str(id) + ":" + text, subsection_node
                            )
                            # print("\t \t" + " " + a.text)
                            txt.write("\t \t" + " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-1em":
                            statutory_1_node = Node(
                                "ID:" + str(id) + ":" + text, statutory_node
                            )
                            # print("\t \t \t" + " " + a.text)
                            txt.write("\t \t \t" + " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-2em":
                            statutory_2_node = Node(
                                "ID:" + str(id) + ":" +
                                a.text.replace('"', " "),
                                statutory_1_node,
                            )
                            # print("\t \t \t \t" + " " + a.text)
                            txt.write("\t \t \t \t" + " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-3em":
                            statutory_3_node = Node(
                                "ID:" + str(id) + ":" +
                                a.text.replace('"', " "),
                                statutory_2_node,
                            )
                            # print("\t \t \t \t \t" + " " + a.text)
                            txt.write("\t \t \t \t \t" + " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-4em":
                            statutory_4_node = Node(
                                "ID:" + str(id) + ":" +
                                a.text, statutory_3_node
                            )
                            # print("\t \t \t \t \t \t" + " " + a.text)
                            txt.write("\t \t \t \t \t \t" +
                                      " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-5em":
                            statutory_5_node = Node(a.text, statutory_4_node)
                            # print("\t \t \t \t \t \t \t" + " " + a.text)
                            txt.write("\t \t \t \t \t \t \t" +
                                      " " + a.text + "\n")
                        elif a["class"][0] == "statutory-body-block":
                            statutory_block_node = Node(
                                "ID:" + str(id) + ":" + text, subsection_node
                            )
                            # print("[[ " + " " + a.text + "]]")
                            txt.write("[[ " + " " + a.text + "]]\n")
                        elif a["class"][0] == "statutory-body-block-2em":
                            statutory_block_2_node = Node(
                                a.text, statutory_block_node)
                            # print("[[[[ " + " " + a.text + "]]]]")
                            txt.write("[[[[ " + " " + a.text + "]]]]\n")
                        elif a["class"][0] == "statutory-body-block-1em":
                            statutory_block_3_node = Node(
                                a.text, statutory_block_2_node
                            )
                            # print("[[ " + " " + a.text + "]]")
                            txt.write("[[ " + " " + a.text + "]]\n")
                    else:
                        continue
                        # print(" -- ")

                exporter = JsonExporter(indent=2, sort_keys=True)
                name = root_node.name
                pos = name.find("§")
                name_clean = name[pos:]
                with open("data/" + name_clean + "-tree.json", "w+") as fp:
                    exporter.write(root_node, fp)
        else:
            raise ValueError("NO TAG elements in the file")

        self.root = root_node
        return self.root

    """
    PRINT NODES
    """

    def printNodes(self):
        if self.root is not None:
            for pre, fill, node in RenderTree(self.root):
                print("%s%s" % (pre, node.name))
        else:
            raise ValueError("not value in the root node")

    """
    NOT IMPLEMENT YET
    """

    def exportTree(self, root):
        # DotExporter(root_node, graph="graph", nodeattrfunc=lambda node : "shape=box").to_dotfile("tree.dot")
        # DotExporter(root_node, graph="digraph", nodeattrfunc=lambda node: "shape=rect, nojustify=true, fontsize=10, fixedsize=false, maxiter=200, width=1.5, len=2").to_picture("tree3.png")
        return 0

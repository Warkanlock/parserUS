# coding: utf-8
from src import getFile
from src import parseTax
import sys
import argparse


def main():
    response, URI = getFile.GetFiles(
        title=args.title, subtitle=args.subtitle, chap=args.chapter, subchap=args.subchapter, part=args.part, section=args.section).getFile()

    # parse the US CODE
    treeSection = parseTax.ParserTaxCode(response, uriTemp=URI)
    # get the nodes
    nodesSection = treeSection.parseEntire()
    # print the tree
    # treeSection.printNodes()
    if nodesSection:
        print("PARSE COMPLETE --> sections into data folder")


parser = argparse.ArgumentParser("Parse the US CODE -> Made by Ignacio Brasca")
parser.add_argument("-title", metavar='T', type=str)
parser.add_argument("-subtitle", metavar='ST', type=str)
parser.add_argument("-chapter", metavar='C', type=str)
parser.add_argument("-subchapter", metavar='SC', type=str)
parser.add_argument("-part", metavar='P', type=str)
parser.add_argument("-section", metavar='SEC', type=str)

args = parser.parse_args()
main()

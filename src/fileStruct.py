"""
URI Form = USCODE-2017-titleX-subtitleY-chapZ-subchapW-partXX-secYY.htm
URI Form = USCODE-2017-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm
"""


class FileStruct:
    def __init__(self, title, subtitle, chapter, subchapter, part, section):
        self.__title = title
        self.__subtitle = subtitle
        self.__chap = chapter
        self.__sec = section
        self.__subchap = subchapter
        self.__part = part

    def getURI(self):
        root = "USCODE-2017-title" + self.__title + "/html/"
        if self.__title:
            root += "USCODE-2017-title" + self.__title
        if self.__subtitle:
            root += "-subtitle" + self.__subtitle
        if self.__chap:
            root += "-chap" + self.__chap
        if self.__subchap:
            root += "-subchap" + self.__subchap
        if self.__part:
            root += "-part" + self.__part
        if self.__sec:
            root += "-sec" + self.__sec
        root += ".htm"
        return root

import requests
from src import fileStruct
from bs4 import BeautifulSoup
import re

HOST_BASED = "https://www.govinfo.gov/content/pkg/"


class GetFiles(object):

    """
    CONSTRUCTOR
    """

    def __init__(self, title="", subtitle="", chap="", subchap="", part="", section=""):
        self.manageFiles = fileStruct.FileStruct(
            title, subtitle, chap, subchap, part, section
        )
        self.URI = self.manageFiles.getURI()
        print(self.URI)

    """
    GET file
    """

    def getFile(self):
        response = requests.get(HOST_BASED + self.URI)
        soup = BeautifulSoup(response.content, features="html5lib")
        elementwithouttags = soup.body.find_all(
            re.compile("^(?!.*(span|br|a|div)).*$"))
        return elementwithouttags, self.URI

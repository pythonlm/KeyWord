#encoding = utf-8
from ConfigParser import ConfigParser
from ProjectVar.Var import page_object_repository_path

class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_repository_path)

    def getItemsFromSection(self,sectionName):
        print self.cf.items(sectionName)
        return dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__=="__main__":
    xxxx
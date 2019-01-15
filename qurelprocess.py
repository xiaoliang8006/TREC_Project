import xml.etree.ElementTree as ET
import os
import shutil

def process(path):
    #读取文件
    tree = ET.parse(path)
    root = tree.getroot()
    root2 = ET.Element('topics')  # 设置标签
    #查找指定数据并保存数据
    # topic
    for topic in root.iter('topic'):
        son = ET.SubElement(root2,'TOP')
        NUM = ET.SubElement(son,'NUM')
        NUM.text = topic.get('number')
        disease = ET.SubElement(son,topic.find('disease').tag)
        disease.text = topic.find('disease').text
        gene = ET.SubElement(son,topic.find('gene').tag)
        gene.text = topic.find('gene').text
        demographic = ET.SubElement(son,topic.find('demographic').tag)
        demographic.text = topic.find('demographic').text
        other = ET.SubElement(son,topic.find('other').tag)
        other.text = topic.find('other').text
        #son.text = topic.get('number')





    #添加换行功能
    def indent(elem, level=0):
        i = "\n" + level*"\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    # 保存xml文件
    indent(root2,0)
    tree = ET.ElementTree(root2)
    target='topics2017.xml'
    #print(target)
    tree.write(target)


#开始处理
path = 'topics2017_raw.xml'
process(path)




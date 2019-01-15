import xml.etree.ElementTree as ET
import os
import shutil

def process(path):
    #读取文件
    tree = ET.parse(path)
    root = tree.getroot()
    root2 = ET.Element('DOC')#设置标签

    #查找指定数据并保存数据
    #DOCNO
    for DOCNO in root.iter('nct_id'):
        print(DOCNO.tag,DOCNO.text)
        son = ET.SubElement(root2,'DOCNO')
        son.text = DOCNO.text
    #verification_date
    for node in root.iter('verification_date'):
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'verification_date')
        son.text = node.text
    # minimum_age
    for node in root.iter('minimum_age'):
        #print(node.tag, node.text)
        son = ET.SubElement(root2, 'minimum_age')
        son.text = node.text
    # maximum_age
    for node in root.iter('maximum_age'):
        #print(node.tag, node.text)
        son = ET.SubElement(root2, 'maximum_age')
        son.text = node.text
    # gender
    for node in root.iter('gender'):
        #print(node.tag, node.text)
        son = ET.SubElement(root2, 'gender')
        son.text = node.text
    # mesh_term
    for node in root.iter('mesh_term'):
        # print(node.tag, node.text)
        son = ET.SubElement(root2, 'mesh_term')
        son.text = node.text


    #brief_title
    for node in root.iter('brief_title'):
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'brief_title')
        son.text = node.text
    #official_title
    for node in root.iter('official_title'):
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'official_title')
        son.text = node.text
    #brief_summary
    for node in root.iter('brief_summary'):
        node = node.find('textblock')
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'brief_summary')
        son.text = node.text
    #detailed_description
    for node in root.iter('detailed_description'):
        node = node.find('textblock')
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'description')
        son.text = node.text
    #criteria
    for node in root.iter('criteria'):
        node = node.find('textblock')
        #print(node.tag,node.text)
        son = ET.SubElement(root2,'criteria')
        son.text = node.text


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
    target='./data/'+DOCNO.text+'.xml'
    #print(target)
    tree.write(target)


#批量获取某路径文件夹及子文件夹下的指定类型文件
soundfile = []
def eachfile(filepath):
    pathdir = os.listdir(filepath)
    for s in pathdir:
        newdir = os.path.join(filepath, s)  # 将文件名加入到当前文件路径后面
        if os.path.isfile(newdir):  # 如果是文件
            if os.path.splitext(newdir)[1] == ".xml":  # 如果文件是".xml"后缀的
                soundfile.append(newdir)
        elif os.path.isdir(newdir):  # 如果是路径
            eachfile(newdir)  # 递归
    return soundfile

#开始处理
fp = './clinicaltrials_xml'
os.chdir(fp)
f = eachfile(fp)
fail=0
for i in range(len(f)):
    path=f[i]
    print(path)
    try:
        process(path)
    except Exception as e:
        print(e)
        fail+=1
        continue

print('总文件数:',len(f))
print('失败文件数:',fail)



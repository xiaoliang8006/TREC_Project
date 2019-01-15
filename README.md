
## 《现代信息检索》 TREC 2018

## 本课程大作业要求：

在 TREC Precision Medicine (PM)2017 数据上进行检索竞赛。
TREC 的 PM 评测任务就是为解决临床中的现实需求、促进医疗文献文本检索技术的发展
与交流而设立。PM 评测任务致力于解决病人信息匹配，相关文档检索问题，主要有两个子
任务：科学文献子任务和临床试验子任务。Scientific Abstract 是医疗文献的摘要部分，
目标是为医生提供学术研究上相关的治疗信息。Clinical trials 是病人病历数据库，目标是
为医生提供与此病是病人病历数据库，目标是为医生提供与此病人相关的电子病历。大作业
要求完成第二个任务，即 Clinical trials。

## code

#### clinicaltrials_xml文件夹(可以有子文件夹)是要训练的数据

#### data文件夹是预处理后的训练数据

#### dataprocess.py 处理训练数据clinicaltrials_xml文件夹里的文档，抽取一些主要特征，存入data文件夹，用于文档收集和建立索引

#### qurelprocess.py 处理查询文档topics2017_raw.xml，存入到topics2017.xml，用于查询

#### qrels-final-trials.txt 用于结果评估

#### finally.res 相关反馈

#### finally.eval 结果评估

#### terrier-project-5.0文件夹里的runTerrier脚本最重要！！！

## 使用方式

1.运行dataprocess.py处理训练数据

2.运行qurelprocess.py处理查询文档

3.cd到terrier-project-5.0文件夹，运行runTerrier.sh脚本即可

4.可自行修改runTerrier.sh脚本

#### 注意: 需要修改程序中的路径



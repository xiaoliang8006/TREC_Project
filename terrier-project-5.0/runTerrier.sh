#!/bin/bash

#删除之前生成的文件
echo 删除之前生成的文件
rm -rf ./terrier-project-5.0/var/results ./terrier-project-5.0/var/index/data* ./finally*
cd ./terrier-project-5.0/

#收集文档
echo 收集文档
./bin/trec_setup.sh ../data/

#建立索引
echo 建立索引
./bin/trec_terrier.sh -i

#检索
echo 搜索query
#In_expB2模型
./bin/trec_terrier.sh -r -Dtrec.model=In_expB2 -Dtrec.topics=../topics2017.xml

#检验结果
#echo query结果评估
./bin/trec_eval.sh ../qrels-final-trials.txt ./var/results/In_expB2_0.res  >> ../eval_res/In_expB2.eval

#相关反馈
echo 相关反馈
#BM25 + In_expB2模型
./bin/trec_terrier.sh -r -Dtrec.model=BM25 -c 0.5 -Dtrec.topics=../topics2017.xml -q -Dqe.feedback.filename=./var/results/In_expB2_0.res

#检验结果
echo 相关反馈结果评估
./bin/trec_eval.sh ../qrels-final-trials.txt ./var/results/BM25_d_3_t_10_1.res  >> ../finally.eval

cp ./var/results/BM25_d_3_t_10_1.res ../finally.res



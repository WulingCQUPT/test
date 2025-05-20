# -*- coding: utf-8 -*-
"""
Created on Wed May 14 14:59:20 2025
conda env list  # 显示虚拟环境名字
conda activate llm2e  # 激活本项目的虚拟环境llm2e，以安装python包
conda list  # 虚拟环境llm2e中所有的已安装的包
conda install numpy # 使用conda 命令安装
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple # 使用pip命令安装
@author: ling

"""
import requests



textquestion = "请使用中文回答，历年欧冠冠军是谁？"
 
data = {
    "model": "llama3.2:1b",
    "prompt": textquestion,
    "stream": False # 是否以流式返回（可设为 True/False）
}
 
response = requests.post(
    "http://localhost:11434/api/generate",
    json=data
)
print(response.json()['response'])

from rag import Rag

rag = Rag('llama3.2:1b', '私人知识库.txt')
msg = rag.chat('请介绍下刘芳')
print(msg)




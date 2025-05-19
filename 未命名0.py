# -*- coding: utf-8 -*-
"""
Created on Wed May 14 14:59:20 2025

@author: ling
"""
import numpy as np
import requests



textquestion = "请使用中文回答，历年欧冠冠军是谁？"
 
data = {
    "model": "gemma3:4b",
    "prompt": textquestion,
    "stream": False # 是否以流式返回（可设为 True/False）
}
 
response = requests.post(
    "http://localhost:11434/api/generate",
    json=data
)
print(response.json()['response'])

from rag import Rag

rag = Rag('deepseek-r1:14b', '私人知识库.txt')
msg = rag.chat('请介绍下刘芳')
print(msg)




#!/usr/bin/env python

import os
import sys

# from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

if len(sys.argv) == 3:
    directory_path = sys.argv[1]
    if not os.path.isabs(directory_path):
      directory_path = os.path.join(os.getcwd(), directory_path)
    query = sys.argv[2]
else:
    directory_path = os.getcwd()
    query = sys.argv[1]

loader = DirectoryLoader(directory_path, glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query))
print(index.query(query, llm=ChatOpenAI()))

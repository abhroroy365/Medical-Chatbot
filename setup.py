from setuptools import find_packages, setup

setup(name='Medical Chatbot',
      version='0.0.0',
      description="A Retrieval-Augmented Generation (RAG) based Medical Chatbot.\
          With the base model as Llama2 from Meta, the Retrieval system uses a medical\
              document as corpus to generate context-rich output. ",
      author='Abhra Ray Chaudhuri',
      author_email='hyperparameter21@gmail.com',
      packages=find_packages(),
      install_requires=[])
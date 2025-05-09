from setuptools import find_packages,setup

setup(
    name='tutormind',
    version='0.1.1',
    author='rohit krishnan',
    author_email='rohitkrishnanm@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
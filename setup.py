from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='0.1.0',
    author='Samarth Jayakumar',
    author_email='samarth4python@gmail.com',
    description='its a calculator',
    long_description=open('README.md').read(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_library',  # Optional
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
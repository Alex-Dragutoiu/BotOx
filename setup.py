import os
from distutils.core import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='bot.ox',
    author='Alexandru Dragutoiu',
    author_email='alexdragutoiu99@gmail.com',
    version='0.1.0',
    license='MIT',
    description='BotOx sends emails to participants',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Alex-Dragutoiu/BotOx',
    keywords='bot',
    python_requires='>=3.8.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8.8',
    ]
)

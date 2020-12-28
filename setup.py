from setuptools import find_packages, setup

setup(
    name                ='skoopy',
    packages            =find_packages(include=['skoopy']),
    version             ='0.1.0',
    description         ='API to extract user\'s desired books from Skoob.com.br',
    long_description    = README,
    long_description_content_type='text/markdown',
    author              ='Diego da Silva Lourenço',
    email               ='diego.lourenco15@gmail.com',
    license             ='MIT',
    url                 ='https://github.com/Diegoslourenco/skooby',
    platforms           =['Any'],
    py_modules          =['skoopy'],
    install_requires    =[],
    classifiers         =[
        'Development Status:: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
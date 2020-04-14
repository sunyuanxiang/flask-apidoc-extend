from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='Flask-Apidoc-Extend',
    version='0.1.2',
    packages=['flask_apidoc_extend'],
    url='https://github.com/sunyuanxiang/flask-apidoc-extend',
    license='MIT',
    author='sun yuanxiang',
    author_email='apidocer@163.com',
    description='Add ApiDoc support to Flask',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['flask', 'apidoc', 'doc', 'documentation','restful'],
    install_requires=['flask>=0.11'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    python_requires='>=3.5',
)

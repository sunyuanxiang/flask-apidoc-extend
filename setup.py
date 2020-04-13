from setuptools import setup

setup(
    name='flask-apidoc-extend',
    version='0.1.0',
    packages=['flask_apidoc_extend'],
    url='https://github.com/sunyuan_xiang/flask-apidoc-extend',
    license='MIT',
    author='sun yuanxiang',
    author_email='apidocer@163.com',
    description='Add ApiDoc support to Flask',
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

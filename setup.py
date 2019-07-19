import setuptools
from distutils.core import setup
setup(
    name='z-py',
    version='0.4.7',
    author='Haiyang Zheng',
    author_email='wnfdsfy@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/zhenghy/zpy',
    license='MIT',
    description='AWM :Always With Me Function',
    long_description=open('README.MD','r').read(),
    long_description_content_type='text/markdown',
    install_requires=['pymysql'],
    keywords=['always', 'function'],
    platforms='any',
)

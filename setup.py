import setuptools
from distutils.core import setup
print(setuptools.find_packages())
setup(
    name='z-py',
    version='0.2.0',
    author='Haiyang Zheng',
    author_email='wnfdsfy@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/zhenghy/zpy',
    license='MIT',
    description='AWM :Always With Me Function',
    long_description=open('README.MD').read(),
    install_requires=[],
    keywords=('always', 'function'),
    platforms='any',
)

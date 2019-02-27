import setuptools
from distutils.core import setup
print(setuptools.find_packages())
setup(
    name='z-py',
    version='0.2.0',
    author='Haiyang Zheng',
    author_email='wnfdsfy@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/zhenghy/gxhy',
    license='MIT',
    description='always with me function',
    long_description=open('README.txt').read(),
    install_requires=[],
    keywords=('always', 'function'),
    platforms='any',
)

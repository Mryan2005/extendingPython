from setuptools import setup, find_packages

setup(
    name='extendingPython',
    version='0.0.1',
    author='Mryan2005',
    author_email='zhizhongyan@qq.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mryan2005/extendingPython',
    packages=find_packages(),
    install_requires=[
        # 列出你的包依赖，例如：
        # 'requests>=2.25.1',
        'setuptools~=68.2.0',
        'pyhttpx~=2.10.12',
        'requests~=2.32.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License-Expression: MIT AND (Apache-2.0 OR BSD-2-clause)',
        'Operating System :: All OS',
    ],
    python_requires='>=3.6',
)

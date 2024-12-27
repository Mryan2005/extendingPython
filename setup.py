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
        open('./requirements.txt').read().splitlines()
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: All OS',
    ],
    python_requires='>=3.6',
)

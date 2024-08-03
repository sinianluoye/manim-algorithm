from setuptools import setup, find_packages

import os
commit_hash = os.environ.get("MANIM_ALGORITHM_COMMIT_HASH")
if commit_hash:
    commit_hash = commit_hash.strip()
version = "0.0.4"
if commit_hash:
    version = f"{version}.dev{int(commit_hash[:7],base=16)}"

setup(
    name='manim-algorithm',
    version=version,
    packages=find_packages(exclude=["test", "test.*", "examples", "examples.*"]),
    install_requires=[
        "manim>=0.18.0"
    ],
    author='sinianluoye',
    author_email='sinianluoye@outlook.com',
    description='computer science lib for manim(ce version)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sinianluoye/manim-algorithm',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)

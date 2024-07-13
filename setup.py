from setuptools import setup, find_packages

setup(
    name='manim-algorithm',
    version='0.0.2',
    packages=find_packages(),
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

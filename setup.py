import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='phlood',
    version='1.0',
    author='cwilkc',
    author_email='cbw182@gmail.com',
    description='Fake username and password generator/sender to phishing scam websites.',
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU v3",
        "Operating System :: OS Independent"
    ],
    entry_points={
        'console_scripts': [
            'phlood = phloodthephish.phlood:main',
        ]
    }
)

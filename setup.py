from os.path import join, dirname
from setuptools import find_packages, setup

try:
    long_description = open(join(dirname(__file__), "README.md"), encoding="utf8").read()
except Exception:
    long_description = None

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='t5s',
    packages=find_packages(include=['t5s*']),
    version='2.0.0',
    description="T5 Summarisation Using Pytorch Lightning",
    license='MIT License',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://dagshub.com/gagan3012/summarization.git",
    entry_points={
        'console_scripts': [
            't5s=t5s.cli:main',
        ]
    },
)

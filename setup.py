import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='stale-prs',
    version='0.0.1',
    author='Sandy Chapman',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SandyChapman/UpgradeChallengeSolution',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'keyring==23.0.1',
        'requests==2.25.1',
        'dateparser==1.0.0'
    ],
)

from setuptools import setup, find_packages

requirements = ['requests']

setup(
    name="gaipy",
    version="0.10",
    description="GaisDB Python API",
    author="GAIS LAB",
    url="",
    license="MIT",
    include_package_data=True,
    packages=find_packages(include=["gaipy","gaipy.*"]),
    install_requires=requirements
    # scripts=["scripts/test.py"],
)

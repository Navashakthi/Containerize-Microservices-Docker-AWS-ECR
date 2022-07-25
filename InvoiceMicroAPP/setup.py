from setuptools import find_packages, setup

setup(name="microservices",
      version = "0.1",
      description = "Example of Microservices using Flask",
      author = "Navashakthi Gnanasekaran",
      platforms = ["any"],
      packages = find_packages(),
      install_requires = ["Flask==2.0.3", "requests==2.20.0"],
      )
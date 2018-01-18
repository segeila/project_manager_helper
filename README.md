# Project Manager Helper
Helping project manager to find similar project descriptions from an existing dataset of projects.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
python 2.7 or higher

Required libraries:
* watson-developer-cloud
* pandas
* ipython

The most convinient way to have an environment set up is to follow these instructions:

https://ipython.org/install.html

which will guide you through the installation process.

To install Watson Developer Cloud Python SDK in command line type:
```
pip install --upgrade watson-developer-cloud
```

## How to use
Clone this repository to your computer.
Run iPython notebook to see an example of keyword extraction and comparison.
You may edit the content of ```new_project.txt``` which serves as an example of a project description to compare against.

To open iPython notebook locally, navigate to the project folder and type in command line:
```
jypiter notebook
```
After you will be able to open iPython notebook in a browser and execute cells within the notebook to see how the script works.

## Authors

* **Timofeeva Polina** - *Initial work* 

## Acknowledgments

* I would also like to acknowledge with much appreciation the crucial role of **Kimmo Kaskikallio (IBM)** for introducing to IBM Watson services and providing with reference materials and code examples.
**Mikael Lindblad (Nokia)** for inviting to the IBM Watson training where idea of the project was developed. **Risto Kauppinen (Nokia)** and **Roope Takala (Nokia)** for developing the idea of the project and
testing it.


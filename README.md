# Rank Estimation of University Entrance Exam
[![userinfobot](https://img.shields.io/badge/Requirements-See%20Here-green)](https://github.com/matinazhir/rank-estimation/blob/master/requirements.txt)

It's a program to calculate the approximate result of your university entrance exam.
You should give your exam results statistics data to the program to calculate the result.
I put the results of the master economics exam data to project to show how it works.
The program has a simple ui to work with. You can get the average and standard deviation of each book in your exam,
to know how much you should to answer to get good grades. And you can enter your desired grades to know with them, what your rank will be.

# How to Run

1. Install python3, pip3, virtualenv, in your system.
2. Clone the project ```git clone https://github.com/matinazhir/rank-estimation.git && cd rank-estimation```.
3. In the project folder create a virtual environment using ```python3 -m venv .yourenvname``` for linux and ```python -m venv .yourenvname``` for windows.
4. Connect to your virtual environment using ```source .yourenvname/bin/activate```.
5. From the project folder, install packages using ```pip install -r requirements.txt```.
6. Add your exam results statistics data to ```data``` folder with name ```data.csv```.
7. Now environment is ready. Run it by ```python app/main.py```.

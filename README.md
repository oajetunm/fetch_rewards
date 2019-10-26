There are two ways to go about running the code.

Option 1:

Before running, please make sure you have the latest version of python on your computer (python 3.7).
Run the text_similarity.py code in the terminal or command prompt by running 'python text_similarity.py'.
When you run this code you will be asked to enter the path for two text files.
The text (txt) files are stored in the directory text_files. If you want to enter the path for  sample1 text file enter
'text_files/sample1.txt' and 'text_files/sample2.txt' for sample 2 text file. Once you've entered both of paths for
the text files you would like to compare, the code will run and a sentence will print out with the similarity score.


Option 2:

This option addresses the first Bonus question

Option 2 is a web service created in flask.
To use this webservice you can past the path, http://oajetunm.pythonanywhere.com/, to your web browser.
This webpage will allow users to enter two strings and compare them.  Once you press 'Do calculation'
then it will return the similarity score of the two documents. The code for this webpage can be found in the path ~projects/api of this repository.
The api.py file has the flask app code and the processing.py file has the code for the program.


If you want to run the api code directly in your terminal:

You can also run the api.py file on your machine. Before doing so make sure flask package is pip installed on your computer and also make sure your computer has latest portion of python (python 3.7).
To do so cd to the folder ~projects/api. Then run python api.py. This will give you a website address you can paste in your web browser. The path will be in on of the lines that print out that looks like
'Running on http://127.0.0.1:5000/'. Paste the ip address (http://127.0.0.1:5000/) in your web browser. Paste the path that is returned into your server and it will take you to a screen where you can enter your two strings.
and then click 'Do Calculation' and the website will return the similarity score.


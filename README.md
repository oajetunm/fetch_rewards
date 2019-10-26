There are two ways to go about running the code.

Option 1:

Run the test_similarity.py code. when you run this code you will be asked to enter two file names.
The text (txt) files are stored in the directory text_files. For sample1 text file enter 'text_files/sample1.txt'
and 'text_files/sample2.txt' for sample 2 text file. Once you enter both of the text files you would like to compare,
a sentence will print out with the similarity score.


Option 2:

Address first Bonus question

Option 2 is a web service created in flask. To use this webservice go to http://oajetunm.pythonanywhere.com/
At this webpage will allow users to enter two strings and compare them. The webpage will return the similarity
score of the two documents. The code for this webpage can be found in the path ~projects/api of this repository.
The api.py file has the flask app code and the processing.py file has the code for the program.

You can also run the api.py file on your machine. This will give you a website address you can paste in your server. The
path will look like this http://127.0.0.1:5000/. Paste this into into your server and enter your strings.

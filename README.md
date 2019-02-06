# Malicious Web Content Detection using Machine Learning

### Steps for reproducing the project -
* Install all the required packages using the following command - ```pip install -r requirements.txt```.
Make sure your pip is consistent with the Python version you are using by typing ```pip -V```.
* Move the project folder to the correct localhost location. For eg. ```/Library/WebServer/Documents``` in case of Macs.
* (If you are using a Mac) Give permissions to write to the markup file ```sudo chmod 777 markup.txt```.
* Modify the path of your Python 2.x installation in ```clientServer.php```.
* (If you are using **anything other than** a Mac) Modify the localhost path in ```features_extraction.py``` to your localhost path (or host the application on a remote server and make the necessary changes).
* Go to ```chrome://extensions```, activate developer mode, click on load unpacked and select the 'Extension' folder from our project.
* Now, you can go to any web page and click on the extension in the top right panel of your Chrome window. Click on the 'Safe of not?' button and wait for a second for the result.
* Done!

### Research paper - http://ieeexplore.ieee.org/document/8256834/

#### Abstract -
* Naive users using a browser have no idea about the back-end of the page. The users might be tricked into giving away their credentials or downloading malicious data.
* Our aim is to create an extension for Chrome which will act as middleware between the users and the malicious websites, and mitigate the risk of users succumbing to such websites.
* Further, all harmful content cannot be exhaustively collected as even that is bound to continuous development. To counter this we are using machine learning - to train the tool and categorize the new content it sees every time into the particular categories so that corresponding action can be taken.

### Take a look at the [demo](https://youtu.be/0-wky0h3hmM)

A few snapshots of our system being run on certain webpages -

![spit_safe](https://user-images.githubusercontent.com/18022447/35985360-7cd910f2-0cc4-11e8-9edf-d38bf83d19a1.png)
_**Fig 1.** A safe website - www.spit.ac.in (College website)_

![drive_phishing](https://user-images.githubusercontent.com/18022447/35985366-81a9c5b8-0cc4-11e8-887d-7f427ffa8a8e.png)
_**Fig 2.** A phishing website which looks just like Google Drive._

![dropbox_phishing](https://user-images.githubusercontent.com/18022447/35985373-84056c86-0cc4-11e8-8751-cf511d5b8aa0.png)
_**Fig 3.** A phishing website which looks just like Dropbox_

![moodle_safe](https://user-images.githubusercontent.com/18022447/35985384-881ea85a-0cc4-11e8-9bea-cf71b3089364.png)
_**Fig 4.** A safe website - www.google.com_

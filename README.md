# Malicious Web Content Detection using Machine Learning
### (Paper published at - http://ieeexplore.ieee.org/document/8256834/)

Naive users using a browser have no idea about the back-end of the page. The users might be tricked into giving away their credentials or downloading malicious data. Our aim is to create an extension for Chrome which will act as middleware between the users and the malicious websites, and mitigate the risk of users succumbing to such websites. Further, all harmful content cannot be exhaustively collected as even that is bound to continuous development. To counter this we are using machine learning - to train the tool and categorize the new content it sees every time into the particular categories so that corresponding action can be taken.

A few examples of our system being run on certain webpages -

![spit_safe](https://user-images.githubusercontent.com/18022447/35985360-7cd910f2-0cc4-11e8-9edf-d38bf83d19a1.png)
Fig 1. A safe website - www.spit.ac.in (College website)

![drive_phishing](https://user-images.githubusercontent.com/18022447/35985366-81a9c5b8-0cc4-11e8-887d-7f427ffa8a8e.png)
Fig 2. A phishing website which looks just like Google Drive.

![dropbox_phishing](https://user-images.githubusercontent.com/18022447/35985373-84056c86-0cc4-11e8-8751-cf511d5b8aa0.png)
Fig 3. A phishing website which looks just like Dropbox

![moodle_safe](https://user-images.githubusercontent.com/18022447/35985384-881ea85a-0cc4-11e8-9bea-cf71b3089364.png)
Fig 4. A safe website - www.google.com

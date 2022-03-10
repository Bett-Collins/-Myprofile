# Myprofile

## Author
[kiprotich Collins]
# Description
It An application that allows users to pitch ideas that could impress other people.The user is be able to submit a new pitch,comment and likes them and are able to login and sign up too.

## Live Link
[View Site]((https://github.com/Bett-Collins))

## User Story

* Comment on the different pitches posted py other uses.
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.
* Register to be allowed to log in to the application
* See the pitches posted by other uses.
*Vote on s pitch they have viwed by giving it a upvote or a downvote.


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
https://github.com/Bett-Collins/-Myprofile
  ```
2. Move to the folder and install requirements
  ```bash
  cd myprofile
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```



## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## License
* *MIT License:*

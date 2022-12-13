# Library
> Replicates a library system where items (books/movies/albums) can be added to the library, and the items that are added can be checked out by existing users. New users are given a member id and name. These user profiles will keep track of checked out items and the library will eventually fine members that do not return items before the specified due date.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- The purpose of this project is to reinforce concepts related to polymorphism, inheritance, and composition.


## Technologies Used
- N/A


## Features
List the ready features here:
- Items can be added (books/movies/albums) to the library. Depending on the item added, it will have a different day limit for how long it can be checked out.
- When a user does not return the item in time, the fine will begin to increment until the user returns the item.
- Users are given a member ID and that member ID is utilized when looking up who has what checked out if another user would like to check out something not in the library at the moment.

## Screenshots
![Example screenshot](https://user-images.githubusercontent.com/50156212/207272761-83159d38-a0d1-409a-8cc3-c0c775b9bdf6.PNG)


## Setup
IDE needed to read and run python program. Pycharm website linked for download:
https://www.jetbrains.com/pycharm/

## Usage
Follow these steps and refer to the screenshot to see how to use the program

- Use the Book(), Album(), or Movie() class to create items. Ex. book1 = ("345", "Phantom Tollbooth", "Juster")
- Use the Patron() class to create new members and give them a member id. Ex. p1 = Patron("abc", "Waldo")
- Create the library class and add in the previously created members and items. Ex. lib = library()
- Now you can utilize the library method check_out_library_item to begin checking out books. Ex. lib.check_out_library_item("bcd", "456")
- The days can be incremented with the increment_current_date() function in the library class
- The location of specific items can be found with the get_location() method in the library class. Will print out ON_SHELF, or ON_HOLD, or CHECKED_OUT depending on the status of the book



## Project Status
Project is: _complete_


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Ideally I'd like to have a method that shows a list of all current items and all current members of the library
- It would be good to have member IDs and item IDs being randomly generated instead of assigned



## Acknowledgements
Give credit here.
- This project idea was created by OSU CS 162 class.


## Contact
Created by Michael Vuong. https://www.linkedin.com/in/vuong-michael/ - feel free to contact me!


<!-- ## License -->
-  N/A

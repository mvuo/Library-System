# Author Michael Vuong
# GitHub username: mvuo
# Date: 10/11/2022
# Description: This object-oriented program will create multiple classes to replicate a library system where users can
# do things such as check out a book, hold a book, get fined for late check-outs, and keep track of
# members and book locations.


class LibraryItem:
    """
    Represents a library item object. This object includes the library item ID and the title of the objects.
    """

    def __init__(self, library_item_id, title):
        """Initializes a library item object with the item id and title"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"  # set to the current location of the item
        self._checked_out_by = None  # set to the patron object
        self._requested_by = None  # set to the patron object
        self._date_checked_out = 0  # set to 0

    def get_location(self):
        """Returns the current location of the library item object"""
        return self._location

    def set_location(self, location):
        """Sets the location of the library item object to the location parameter"""
        self._location = location

    def get_ID(self):
        """Returns the library item ID of the library item object"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of the library item object"""
        return self._title

    def set_checked_out_by(self, name):
        """Sets the checked out by variable to the name parameter"""
        self._checked_out_by = name

    def get_checked_out_by(self):
        """Returns the checked out by variable"""
        return self._checked_out_by

    def set_date_checked_out(self, date):
        """Sets the date checked out variable to the date parameter"""
        self._date_checked_out = date

    def get_date_checked_out(self):
        """Returns the date checked out variable"""
        return self._date_checked_out

    def get_requested_by(self):
        """Returns the requested by variable"""
        return self._requested_by

    def set_requested_by(self, name):
        """Sets the requested by variable to the name parameter"""
        self._requested_by = name


class Book(LibraryItem):
    """
    This class inherits from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, author):
        """Initializes same init method as library item but includes author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_check_out_length(self):
        """Returns number to reflect the object"""
        return 21

    def get_author(self):
        """returns the author of the book object"""
        return self._author


class Album(LibraryItem):
    """
    This class inherits from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, artist):
        """Initializes same init method as library item but includes artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_check_out_length(self):
        """returns the number to reflect the object"""
        return 14

    def get_artist(self):
        """returns the artist of the album object"""
        return self._artist


class Movie(LibraryItem):
    """
    This class inherits from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, director):
        """Initializes same init method as library item but includes director"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_check_out_length(self):
        """returns the number to reflect the object"""
        return 7

    def get_director(self):
        """returns the director of the movie object"""
        return self._director


class Patron:
    """
    This class represents a library patron who is a member of the library.
    """

    def __init__(self, patron_id, name):
        """Initializes the patron object with their ID and their name. Initializes list for checked
        out items and integer for fine amount"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns fine amount"""
        return self._fine_amount

    def add_library_item(self, item):
        """adds a library item to patron's checked out items"""
        return self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """removes a library item to patron's checked out items"""
        return self._checked_out_items.remove(item)

    def amend_fine(self, value):
        """Takes a value parameter and adds it to the total fine"""
        self._fine_amount += value

    def get_ID(self):
        """returns patron's ID"""
        return self._patron_id

    def get_checked_out_items(self):
        """returns list of checked out items"""
        return self._checked_out_items


class Library:
    """
    This class represents a library with members and an assortment of books. The user will be able to
    check out books, return checked out books, request for holds, and pay fines.
    """

    def __init__(self):
        """Initializes a list for the library item objects and the member objects. Sets current date
        to 0."""
        self._holdings = []  # library item objects
        self._members = []  # patron objects
        self._current_date = 0

    def add_library_item(self, library_item_object):
        """Takes the library item object and adds it to the holdings list"""
        self._holdings.append(library_item_object)

    def add_patron(self, patron_object):
        """Takes the patron object and adds it to the members list."""
        self._members.append(patron_object)

    def get_holdings(self):
        """returns the holdings list of library item objects"""
        return self._holdings

    def get_members(self):
        """returns the members list of patron objects"""
        return self._members

    def lookup_library_item_from_id(self, ID):
        """searches for the library item from the ID number"""
        for item in self._holdings:
            if item.get_ID() == ID:
                return item
        return None

    def lookup_patron_from_id(self, ID):
        """searches for the patron name from the ID number"""
        for person in self._members:
            if person.get_ID() == ID:
                return person
        return None

    def check_out_library_item(self, patron_ID, item_ID):
        """Checks out a library item to a patron while also handling potential errors"""
        if self.lookup_patron_from_id(patron_ID) == None:
            return "patron not found"
        if self.lookup_library_item_from_id(item_ID) == None:
            return "item not found"
        for item in self._holdings:
            if item.get_ID() == item_ID:
                if item.get_location() != "ON_SHELF":
                    return "item already checked out"
                if item.get_requested_by() != None:
                    return "item on hold by other patron"
                else:
                    item.set_checked_out_by(patron_ID)
                    item.set_date_checked_out(self._current_date)
                    item.set_location("CHECKED_OUT")
                    if item.get_requested_by() == patron_ID:
                        item.set_requested_by(None)
                    self.lookup_patron_from_id(patron_ID).add_library_item(item)
                    return "check out successful"

    def return_library_item(self, item_ID):
        """removes the item from the parameter that the patron has back to the library"""
        if self.lookup_library_item_from_id(item_ID) == None:
            return "item not found"
        for item in self._holdings:
            if item.get_ID() == item_ID:
                if item.get_location() != "CHECKED_OUT":
                    return "item already in library"
                person = self.lookup_patron_from_id(item.get_checked_out_by())
                person.remove_library_item(item)
                if item.get_requested_by != None:
                    item.set_location("ON_HOLD_SHELF")
                item.set_checked_out_by(None)
                return "return successful"

    def request_library_item(self, patron_ID, library_item_ID):
        """sets an object to be on hold for the patron"""
        if self.lookup_patron_from_id(patron_ID) == None:
            return "patron not found"
        if self.lookup_library_item_from_id(library_item_ID) == None:
            return "item not found"
        for item in self._holdings:
            if item.get_ID() == library_item_ID:
                if item.get_requested_by() != None:
                    return "item already on hold"
                item.set_requested_by(self.lookup_patron_from_id(patron_ID))
                if item.get_location() == "ON_SHELF":
                    item.set_location("ON_HOLD_SHELF")
                return "request successful"

    def pay_fine(self, patron_ID, fee):
        """takes a fee parameter that the patron uses to pay any fines"""
        if self.lookup_patron_from_id(patron_ID) == None:
            return "patron not found"
        self.lookup_patron_from_id(patron_ID).amend_fine(-fee)
        return "payment successful"

    def increment_current_date(self):
        """increments the current date and amending the fine value based on how overdue the libraryItem
        objecct is"""
        self._current_date += 1
        for people in self._members:
            for item in people.get_checked_out_items():
                if ((self._current_date - item.get_date_checked_out()) > item.get_check_out_length()):
                    people.amend_fine(0.1)

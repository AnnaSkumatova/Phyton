from random import choice
from unittest import mock
import View, Model

def start():
    choice = 1
    while choice !=9:
        choice = View.Show_Menu()
        match(choice):
            case 0:
                phone_book = Model.get_phone_book()
                View.show_phone_book(phone_book)
            case 1:
                path = View.input_path()
                Model.set_path(path)
                Model.open_file()
            case 2:
                path = View.input_path_record()
                Model.record_file(path)
            case 3:
                contact = View.input_contact()
                Model.new_contact(contact)
            case 4:
                contact = View.input_change()
                Model.change_contact(*contact)
            case 5:
                id = View.input_delete()
                Model.delete_contact(id)
            case 6:
                my_search = View.input_search()
                Model.search_contact(*my_search)
                search_phone_book = Model.get_search_phone_book()
                View.show_Search_phone_book(search_phone_book)
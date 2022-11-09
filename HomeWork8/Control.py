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
                pass
            case 3:
                


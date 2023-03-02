from models.main import Model
from views.main import View
from controllers.main import Controller

def main():
    mainModel = Model()
    mainView = View()
    controller = Controller(mainModel, mainView)
    controller.start()

if __name__ == "__main__":
    main()




# todo: ablak becsukás
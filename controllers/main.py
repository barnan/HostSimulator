
from .othercontroller import OtherController
from .frameselectorcontroller import FrameSelectorController
from .photowatthostcontroller import PhotowattHostController


class Controller :

    def __init__(self, mainModel, mainView) -> None :
        self.mainView = mainView
        self.mainModel = mainModel
        self.frameSelectorController = FrameSelectorController(None, mainView.frameselector, mainView)
        self.photowattHostController = PhotowattHostController(mainModel.photowattHostModel, mainView.frames['PhotowattHostFrame'])
        self.otherController = OtherController(mainModel.photowattHostModel, mainView.frames['OtherFrame'])

        self.cancel_mainwindow_onclosing = self.mainView.add_event_listener('mainwindow_onclosing', self.mainwindow_onclosing)
        self.cancel_after_startup = self.mainView.add_event_listener('after_startup', self.after_startup)
        

    def start(self) -> None :
        self.mainView.start_mainloop()


    def mainwindow_onclosing(self, data) -> None :
        self.photowattHostController.stop()
        self.otherController.stop()
        self.mainView.destroyroot()


    def after_startup(self, data) -> None :
        self.frameSelectorController.initialize()
        self.photowattHostController.initialize()

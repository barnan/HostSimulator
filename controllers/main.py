
from .frameselectorcontroller import FrameSelectorController
from .photowatthostcontroller import PhotowattHostController


class Controller :

    def __init__(self, mainModel, mainView) -> None :
        self.mainView = mainView
        self.mainModel = mainModel
        self.frameSelectorController = FrameSelectorController(mainModel.frameSelectorModel, mainView.frameselector, mainView)
        self.photowattHostController = PhotowattHostController(mainModel.photowattHostModel, mainView.frames['PhotowattHostFrame'])

        # self.mainModel.frameSelectorModel.add_event_listener('frame_selector_changed', self.frameselectorchanged)
    

    def start(self) -> None :
        self.mainView.start_mainloop()

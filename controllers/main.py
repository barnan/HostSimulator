
from .hanwhakoreacontroller import HanwhaKoreaController
from .photowatthostcontroller import PhotowattHostController


class Controller :

    def __init__(self, mainModel, mainView) -> None :
        self.mainView = mainView
        self.mainModel = mainModel
        self.photowattHostController = PhotowattHostController(mainModel.photowattHostModel, mainView.frames['PhotowattHostFrame'])
        self.hanwhaKoreaController = HanwhaKoreaController(mainModel.hanwhaHostModel, mainView.frames['HanwhaKoreaFrame'])

        self.cancel_mainwindow_onclosing = self.mainView.add_event_listener('mainwindow_onclosing', self.mainwindow_onclosing)
        self.cancel_after_startup = self.mainView.add_event_listener('after_startup', self.after_startup)
        
        self.mainView.frameselector.photowattRadioButton.config(command=self._switchframe)
        self.mainView.frameselector.hanwhaRadioButton.config(command=self._switchframe)


    def start(self) -> None :
        self.mainView.start_mainloop()


    def mainwindow_onclosing(self, data) -> None :
        self.photowattHostController.stop()
        self.hanwhaKoreaController.stop()
        self.mainView.destroyroot()


    def after_startup(self, data) -> None :
        self._selectFirstRadioButton()

        self.photowattHostController.initialize()
        self.hanwhaKoreaController.initialize()

########################### frame handling ############################

    def _switchframe(self) -> None :
        currentRadioButtonValue = self.mainView.frameselector.radioButtonVariable.get()
        self.mainView.switch_frame(currentRadioButtonValue)


    def _selectFirstRadioButton(self) -> None : 
        self.mainView.frameselector.photowattRadioButton.select()
        self.mainView.frameselector.photowattRadioButton.invoke()



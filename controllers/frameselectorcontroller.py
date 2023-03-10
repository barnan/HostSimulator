
class FrameSelectorController : 

    def __init__(self, model, frame, mainView) -> None :
        self.model = model
        self.mainView = mainView
        self.frame = frame
        self._bind()


    def _bind(self) -> None :       # itt köti rá magát a view widget-eire 
        self.frame.photowattRadioButton.config(command=self._switchframe)
        self.frame.otherRadioButton.config(command=self._switchframe)
     
  
    def initialize(self) -> None :
        self._selectFirstRadioButton()


    def _switchframe(self) -> None :
        currentRadioButtonValue = self.frame.radioButtonVariable.get()
        self.mainView.switch_frame(currentRadioButtonValue)


    def _selectFirstRadioButton(self) -> None : 
        self.frame.photowattRadioButton.select()
        self.frame.photowattRadioButton.invoke()


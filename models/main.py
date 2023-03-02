from .photowatthostmodel import PhotowattHostModel
from .frameselectormodel import FrameSelectorModel


class Model :
    
    def __init__(self) -> None :
        self.photowattHostModel = PhotowattHostModel()
        self.frameSelectorModel = FrameSelectorModel()

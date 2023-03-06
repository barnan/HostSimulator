from .othermodel import OtherModel
from .photowatthostmodel import PhotowattHostModel


class Model :
    
    def __init__(self) -> None :
        self.photowattHostModel = PhotowattHostModel()
        self.otherModel = OtherModel()

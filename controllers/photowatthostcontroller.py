from tkinter import DISABLED, NORMAL


class PhotowattHostController : 

    def __init__(self, model, frame) -> None :
        self.model = model
        self.frame = frame
        self._bind()


    def _bind(self) -> None :       # itt köti rá magát a view widget-eire 
        self.frame.startServerButton.config(command=self.startserver)
        self.frame.stopServerButton.config(command=self.stopserver)
        self.frame.changeMessageButton.config(command=self.changemessage)
        self.cancel_message_changed = self.model.add_event_listener('message_changed', self.model_on_message_changed)
        self.cancel_message_changed = self.model.add_event_listener('server_started', self.model_on_server_started)
        self.cancel_message_changed = self.model.add_event_listener('server_stopped', self.model_on_server_stopped)


    def startserver(self) -> None :
        self.changemessage()
        port_number = self.frame.port_number.get()
        host_address = self.frame.host_address.get()
        self.model.startmessagesending(host_address, port_number)


    def stopserver(self) -> None :
        self.model.stopmessagesending()


    def changemessage(self) -> None :
        number1 = self.frame.batchId.get()
        number2 = self.frame.theoreticalCounter.get()
        number3 = self.frame.singulationCounter.get()
        self.model.changemessagetosend(number1, number2, number3)


    def model_on_message_changed (self, data) -> None :
        
        text = list()
        for b in data.message_to_send :
            text.append(hex(b))

        self.frame.sentTextMessage.set(' '.join(text))


    def model_on_server_started (self, data) -> None :
        self.frame.startServerButton['state'] = DISABLED
        self.frame.stopServerButton['state'] = NORMAL
        self.frame.host_addressEntry['state'] = DISABLED
        self.frame.portEntry['state'] = DISABLED
        

    def model_on_server_stopped (self, data) -> None :
        self.frame.startServerButton['state'] = NORMAL
        self.frame.stopServerButton['state'] =  DISABLED
        self.frame.host_addressEntry['state'] = NORMAL
        self.frame.portEntry['state'] = NORMAL
        
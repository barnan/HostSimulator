from tkinter import DISABLED, END, NORMAL


class PhotowattHostController : 

    def __init__(self, model, frame) -> None :
        self.model = model
        self.frame = frame
        self._bind()


    def _bind(self) -> None :       # itt köti rá magát a view widget-eire 
        self.frame.startServerButton.config(command=self.start)
        self.frame.stopServerButton.config(command=self.stop)
        self.frame.changeMessageButton.config(command=self._changemessage)
        self.cancel_message_changed = self.model.add_event_listener('message_changed', self._model_on_message_changed)
        self.cancel_server_started = self.model.add_event_listener('server_started', self._model_on_server_started)
        self.cancel_server_stopped = self.model.add_event_listener('server_stopped', self._model_on_server_stopped)
        self.cancel_connection_changed = self.model.add_event_listener('connection_list_changed', self._model_on_connection_changed)


    def start(self) -> None :
        port_number = self.frame.port_number.get()
        host_address = self.frame.host_address.get()
        self.model.start(host_address, port_number)


    def stop(self) -> None :
        self.model.stop()


    def initialize(self) -> None :
        self._changemessage()


    def _changemessage(self) -> None :
        number1 = self.frame.batchId.get()
        number2 = self.frame.theoreticalCounter.get()
        number3 = self.frame.singulationCounter.get()
        self.model.changemessagetosend(number1, number2, number3)


    def _model_on_message_changed (self, data) -> None :
        text = list()
        for b in data.message_to_send :
            text.append(hex(b))

        self.frame.sentTextMessage.set(' '.join(text))


    def _model_on_server_started (self, data) -> None :
        self.frame.startServerButton['state'] = DISABLED
        self.frame.stopServerButton['state'] = NORMAL
        self.frame.host_addressEntry['state'] = DISABLED
        self.frame.portEntry['state'] = DISABLED
        

    def _model_on_server_stopped (self, data) -> None :
        self.frame.startServerButton['state'] = NORMAL
        self.frame.stopServerButton['state'] =  DISABLED
        self.frame.host_addressEntry['state'] = NORMAL
        self.frame.portEntry['state'] = NORMAL

    def _model_on_connection_changed(self, data) -> None :
        self.frame.connectionEntry.delete('0', END)
        for item in data.last_conn_list :
            self.frame.connectionEntry.insert(END, f'{item[0]} {item[1]}\n')
        pass

        
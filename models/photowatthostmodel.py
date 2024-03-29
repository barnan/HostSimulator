
import sys
from threading import Event, Lock
import select
import socket
from threading import Thread
import time
from .observablemodel import ObservableModel

MESSAGE_SENDING_CYCLETIME_SEC = 0.5
CONNECTION_CHECK_CYCLETIME_SEC = 1

class PhotowattHostModel(ObservableModel) :

    def __init__(self) -> None:
        super().__init__()
        
        self.lock = Lock()
        self.stopEvent = Event()
        self.conn = []
        self.message_to_send = ''
        self.thread_open = Thread()
        self.thread_send = Thread()
        self.last_conn_list = []

    
    def start(self, host_address:str, port_number:int) -> None :
        self.stopEvent.clear()

        self.thread_open = Thread(target = self._opensocket, args=(self.stopEvent, host_address, port_number, ))
        self.thread_open.start()
    
        self.thread_send = Thread(target = self._sendmessageperiodically, args=(self.stopEvent, ))
        self.thread_send.start()
        
        self.trigger_event('server_started')


    def stop(self) -> None :
        self.stopEvent.set()

        time.sleep(CONNECTION_CHECK_CYCLETIME_SEC)

        if self.thread_open.is_alive() :
            self.thread_open.join()
        if self.thread_send.is_alive() :
            self.thread_send.join()

        self.trigger_event('server_stopped')
        # PrintAndLog(f'The host simulator is stopped')
        return


    def _opensocket(self, stopEvent:Event, host_address:str, port_number:int) -> None :
        server_address = (host_address, port_number)
        # PrintAndLog(f'starting up on {server_address}') 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_address)
        sock.listen(1)

        # PrintAndLog('Waiting for a client to connect') 

        while True:
            readingList, writingList, exceptionalConditionList = select.select((sock,), (), (), 1)
            
            for l in readingList :
                connection, client_address = sock.accept()
                
                self.lock.acquire()
                try :
                    self.conn.append((connection, client_address))
                    self._copyconn()
                    
                finally :
                    self.lock.release()

                # print("Accepting connection from {}:{}".format(*client_address))
            
            if stopEvent.is_set():
                try :
                    sock.close()
                except : 
                    exception_type, exception_object, exception_traceback = sys.exc_info()
                return

            time.sleep(CONNECTION_CHECK_CYCLETIME_SEC)


    def _sendmessageperiodically(self, stopEvent:Event) -> None :
        while True :
            self.lock.acquire()
            try :
                if stopEvent.is_set() :
                    self._closesockets()
                    return
            
                listToRemove = []
                
                for connection in self.conn :
                    try :
                        connection[0].send(self.message_to_send)
                    except : 
                        listToRemove.append(connection)
                
                if len(listToRemove) > 0 :
                    for itemToRemove in listToRemove :
                        self.conn.remove(itemToRemove)
    
                    self._copyconn()

            finally :
                self.lock.release()

            # PrintAndLog(f'Message was sent at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} to {client_address}:  {message_to_send}')
            time.sleep(MESSAGE_SENDING_CYCLETIME_SEC)


    def changemessagetosend(self, number1:int, number2:int, number3:int) -> None :
        szam1 = number1.to_bytes(4, 'big')
        szam2 = number2.to_bytes(3, 'big')
        szam3 = number3.to_bytes(3, 'big')

        xs = bytearray(b'\x01\x0c')
        xs.append(szam1[0])
        xs.append(szam1[1])
        xs.append(szam1[2])
        xs.append(szam1[3])

        xs.append(szam2[0])
        xs.append(szam2[1])
        xs.append(szam2[2])

        xs.append(szam3[0])
        xs.append(szam3[1])
        xs.append(szam3[2])

        self.message_to_send = bytes(xs)
        self.trigger_event('message_changed')


    def _copyconn(self) -> None :
        self.last_conn_list.clear()
        for element in self.conn :
            self.last_conn_list.append(element[1])
        
        self.trigger_event('connection_list_changed')


    def _closesockets(self) -> None :
        try :
            for connection in self.conn :
                connection[0].shutdown(socket.SHUT_RDWR)
                connection[0].close()
            self.conn.clear()
        except : 
            exception_type, exception_object, exception_traceback = sys.exc_info()

        self._copyconn()


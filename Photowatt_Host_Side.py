from asyncio import Event
import select
import sys
import socket
import logging
import datetime
from threading import Thread, Event
import time

DATETIME_FORMAT = '%Y%m%d_%H%M%S'
MESSAGE_SENDING_CYCLETIME_SEC = 0.5
message_to_send = b'\x01\x0c\x04K\x1f\x01\x00\x0b\xac\x00\x00\x9b'
event = Event()
openEvent = Event()

thread_send = Thread()
thread_open = Thread()
conn = socket.socket()
client_address = tuple()


def OpenSocket(port:int) -> None :
    global conn
    global client_address

    server_address = ('localhost', port)
    PrintAndLog(f'starting up on {server_address}') 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(1)

    PrintAndLog('Waiting for a client to connect') 

    while True:
        readingList, writingList, exceptionalConditionList = select.select((sock,), (), (), 1)
        for l in readingList :
            conn, client_address = sock.accept()
            print("Accepting connection from {}:{}".format(*client_address))
            openEvent.set()
            return
        else:
            # should we quit?
            if openEvent.is_set():
                return

def StartMessageSending(port_number:int) -> None :
    global thread_send
    global thread_open
    global conn
    global client_address
    
    openEvent.clear()
    event.clear()

    thread_open = Thread(target = OpenSocket, args=(port_number, ))
    thread_open.start()
    
    thread_send = Thread(target = SendMessagePeriodically, args=())
    thread_send.start()

    return

def StopMessageSending() -> None :
    global thread_send

    event.set()
    openEvent.set()
    if thread_send.is_alive() :
        thread_send.join()
    if thread_open.is_alive() :
        thread_open.join()
    PrintAndLog(f'The host simulator is stopped')
    return 


def PrintAndLog(message:str, level=logging.INFO) :
    print(message)
    match level :
        case logging.CRITICAL :
            logging.critical(message)
        case logging.FATAL :
            logging.critical(message)
        case logging.ERROR :
            logging.error(message)
        case logging.WARN :
            logging.warning(message)
        case logging.WARNING :
            logging.warning(message)
        case logging.INFO :
            logging.info(message)
        case logging.DEBUG :
            logging.debug(message)
    return None

def SendMessagePeriodically() -> None :
    global message_to_send
    global conn
    global client_address

    openEvent.wait() 

    while True :
        if event.is_set() :
            break
        conn.send(message_to_send)
        PrintAndLog(f'Message was sent at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} to {client_address}:  {message_to_send}')
        time.sleep(MESSAGE_SENDING_CYCLETIME_SEC)

    return

def ChnageMessageToSend(number1:int, number2:int, number3:int) -> list :
    global message_to_send
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

    message_to_send = bytes(xs)

    text = list()
    for b in message_to_send :
        text.append(hex(b))

    return text

def main(args) :

    try:
        now = datetime.datetime.now()
        port_number = args[0]
        wait_sec = args[1]

        PrintAndLog(f'Photowatt host side simulator was started')
        
        StartMessageSending(port_number)
        time.sleep(wait_sec)
        StopMessageSending()
    except Exception as ex:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        PrintAndLog(f'The following exception occured: {ex} at line:{line_number} in file:{filename}')
    return

if __name__ == "__main__" :

    logging.basicConfig(filename='Photowatt_' + f'{datetime.datetime.now().strftime(DATETIME_FORMAT)}' +'.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    main((3333, 60))

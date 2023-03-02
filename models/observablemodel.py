
class ObservableModel :

    def __init__(self) :
        self._event_listeners = {}          # create empty dictionary


    def add_event_listener(self, event_name, fn) :
        if event_name not in self._event_listeners.keys() :     # check if the dict already contains the given key
            self._event_listeners[event_name] = [fn]
        else :
            self._event_listeners[event_name].append(fn)

        return lambda : self._event_listeners.remove(fn)        # give back the delegate with the removal


    def trigger_event(self, event_name) -> None :
        if event_name not in self._event_listeners.keys() :
            return

        for func in self._event_listeners[event_name] :
            func(self)

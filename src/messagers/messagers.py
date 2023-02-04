from abc import ABC, abstractmethod


class AbstractNotificator(ABC):

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def notificator_setup(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def send_notification(self, message):
        raise NotImplementedError

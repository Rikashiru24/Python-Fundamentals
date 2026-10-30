# Abstract Base Class = Purpose is to provide common code to its derivatives
# We must always not able to create an instance of the base class. Only the subclass or child should be instantiated.
# Abstract class cannot be instantiated
# To make the class normal that derives from the Abstract base class, it needs to implement the @abstractmethod
# @abstractmethod, makes our classes to have the same method interface
# In Abstract Base Class, the child or subclass cannot be instantiated unless the abstractmethod is implemented into that child class

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __int__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading date from a memory.")


stream = MemoryStream()
stream.read()

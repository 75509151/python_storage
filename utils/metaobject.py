#-*- coding:utf-8 -*-
'''
MetaObejct class is the base class of all object needs to serialize. 
    
@authors: U{Eric.Li<mailto:eric.li@cereson.com>},
@organization: U{Cereson inc.<http://www.cereson.com>}
@copyright: copyright (c) 2010 Cereson inc.

@version: 0.1.5
@status: beta
@change: 2010-04-19 : add __str__

'''


class MetaObject(object):
    """Base class of all serialize object
    """

    def to_dict(self):
        """Collect all attribute key-value pairs into diction, inner attribute excluded

        @return: diction of all attribute
        @rtype: dict
        """
        return dict((key, self.__dict__[key])
                    for key in self.__dict__
                    if not key.startswith("_"))

    def from_dict(self, dict):
        """Construct a object from diction.

        @param dict: diction containing all attribute key-value pairs.
        """
        self.__dict__ = dict

    def serialize(self):
        """serialize this class, exclude inner attribute.

        @return: diction of all attribute
        @rtype: dict
        """
        meta_dict = dict((key, self.__dict__[key])
                         for key in self.__dict__
                         if not key.startswith("_"))
        meta_dict["_meta_object"] = __name__
        return meta_dict

    def __str__(self):
        """String value of this object

        @return: string
        @rtype: str
        """
        return "; ".join(["%s: %s" % (k, v) for k, v in self.to_dict().items()])

#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from thrift.py3.server cimport ServiceInterface


cdef class MyServiceInterface(ServiceInterface):
    cdef public bint _pass_context_hasDataById
    cdef public bint _pass_context_getDataById
    cdef public bint _pass_context_putDataById
    cdef public bint _pass_context_lobDataById
    pass

cdef class MyServiceFastInterface(ServiceInterface):
    cdef public bint _pass_context_hasDataById
    cdef public bint _pass_context_getDataById
    cdef public bint _pass_context_putDataById
    cdef public bint _pass_context_lobDataById
    pass


#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import folly.iobuf as __iobuf
import typing as _typing
from thrift.py3.server import RequestContext, ServiceInterface
from abc import abstractmethod, ABCMeta

import module.types as _module_types

_RaiserInterfaceT = _typing.TypeVar('_RaiserInterfaceT', bound='RaiserInterface')


class RaiserInterface(
    ServiceInterface
    , metaclass=ABCMeta
):

    @staticmethod
    def pass_context_doBland(
        fn: _typing.Callable[
                [_RaiserInterfaceT, RequestContext],
                _typing.Coroutine[_typing.Any, _typing.Any, None]
        ]
    ) -> _typing.Callable[
        [_RaiserInterfaceT],
        _typing.Coroutine[_typing.Any, _typing.Any, None]
    ]: ...

    @abstractmethod
    async def doBland(
        self
    ) -> None: ...

    @staticmethod
    def pass_context_doRaise(
        fn: _typing.Callable[
                [_RaiserInterfaceT, RequestContext],
                _typing.Coroutine[_typing.Any, _typing.Any, None]
        ]
    ) -> _typing.Callable[
        [_RaiserInterfaceT],
        _typing.Coroutine[_typing.Any, _typing.Any, None]
    ]: ...

    @abstractmethod
    async def doRaise(
        self
    ) -> None: ...

    @staticmethod
    def pass_context_get200(
        fn: _typing.Callable[
                [_RaiserInterfaceT, RequestContext],
                _typing.Coroutine[_typing.Any, _typing.Any, str]
        ]
    ) -> _typing.Callable[
        [_RaiserInterfaceT],
        _typing.Coroutine[_typing.Any, _typing.Any, str]
    ]: ...

    @abstractmethod
    async def get200(
        self
    ) -> str: ...

    @staticmethod
    def pass_context_get500(
        fn: _typing.Callable[
                [_RaiserInterfaceT, RequestContext],
                _typing.Coroutine[_typing.Any, _typing.Any, str]
        ]
    ) -> _typing.Callable[
        [_RaiserInterfaceT],
        _typing.Coroutine[_typing.Any, _typing.Any, str]
    ]: ...

    @abstractmethod
    async def get500(
        self
    ) -> str: ...
    pass



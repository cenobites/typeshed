from collections.abc import Callable
from typing import Any

from .site import JSONRPCSite
from .views import JSONRPCView

class JSONRPCDecoratorMixin:
    def get_jsonrpc_site(self) -> JSONRPCSite: ...
    def get_jsonrpc_site_api(self) -> type[JSONRPCView]: ...
    def register_view_function(
        self, view_func: Callable[..., Any], name: str | None = ..., validate: bool = ..., **options: Any
    ) -> Callable[..., Any]: ...
    def method(self, name: str | None = ..., validate: bool = ..., **options: Any) -> Callable[..., Any]: ...
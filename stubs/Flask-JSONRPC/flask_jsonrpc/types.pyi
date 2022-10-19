from typing import Any

class JSONRPCNewType:
    name: str
    types: type | tuple[type | tuple[type, ...], ...]
    def __init__(self, name: str, *types: type | tuple[type | tuple[type, ...], ...]) -> None: ...
    def check_expected_type(self, expected_type: Any) -> bool: ...
    def check_expected_types(self, expected_types: Any) -> bool: ...
    def check_type_var(self, expected_type: Any) -> bool: ...
    def check_new_type(self, expected_type: Any) -> bool: ...
    def check_union(self, expected_type: Any) -> bool: ...
    def check_args_type(self, expected_type: Any) -> bool: ...
    def check_type(self, o: Any) -> bool: ...

String: JSONRPCNewType
Number: JSONRPCNewType
Object: JSONRPCNewType
Array: JSONRPCNewType
Boolean: JSONRPCNewType
Null: JSONRPCNewType
Types: list[JSONRPCNewType]

from dataclasses import dataclass
from typing import Any

@dataclass
class AnnotatedParameter:
    doc: str
    value: Any

@dataclass
class AnnotatedFunction:
    doc: str
    fn: str
    

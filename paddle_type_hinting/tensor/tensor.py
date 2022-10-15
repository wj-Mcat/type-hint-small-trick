from __future__ import annotations
from typing import List, Union, Tuple

class Tensor:
    """Tensor for python Type hinting"""
    def reshape(self, shape: Union[List[int], Tuple[int]]) -> Tensor: ...
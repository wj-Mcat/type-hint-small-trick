from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tensor.tensor import Tensor
else:
    from paddle import Tensor

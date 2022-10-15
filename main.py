import paddle
from paddle_type_hinting import Tensor

tensor: Tensor = paddle.randn([2,3])
new_tensor = tensor.reshape([3,2])

assert new_tensor.shape == [3, 2]
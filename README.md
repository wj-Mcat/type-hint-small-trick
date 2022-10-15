# type-hint-small-trick

a magic hinting trick for paddle `Tensor` in IDE. Please enjoy the [`main.py`](./main.py) to get more details.

## Feature

* enhance the type hinting for Paddle Tensor in Dev & Runtime mode
* add stub file for IDE to detect members of Tensor

## What I have Done

1. define the tensor.pyi to define the members of `Tensor`, which is not sensitive how the `Tensor` is implemented.
2. use `TYPE_CHECKING` to detect the `DEV` or `Runtime` mode.


## Creators

- [@wj-Mcat](https://github.com/wj-Mcat) - Jingjing WU (吴京京)

## Copyright & License

- Code © 2022 <https://github.com/wj-Mcat>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons

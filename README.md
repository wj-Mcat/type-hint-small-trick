# type-hint-small-trick

a magic hinting for python methods/attributes in IDE

## Feature

* enhance the type hinting for Paddle Tensor in Dev & Runtime mode
* add stub file for IDE to detect members of Tensor

## What I have Done

1. define the tensor.pyi to define the members of `Tenosr`, which is not sensitive how the `Tensor` is implemented.
2. use `TYPE_CHECKING` to detect the `DEV` or `Runtime` mode.


Please enjoy the `main.py` to get more details.

## Creators

- [@wj-Mcat](https://github.com/wj-Mcat) - Jingjing WU (吴京京)

## Copyright & License

- Code © 2022 <https://github.com/wj-Mcat>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# henlo: machine readable crypto exchange API in OpenAPI/AsyncAPI YAML

there are way too many crypto exchanges and programming languages. we should try standardise the way we implement the exchange library.

I will add a bunch of AsyncAPI YAML here. In the near future I will set up a codegen that generates the rust exchange lib for python and crate for rust.

# generate code
install async api code generator
```
npm install -g @asyncapi/generator
```
## rust model
```
asyncapi generate models rust example_2.yml -o output/example_rust_model
```
## python model
```
asyncapi generate models python example_2.yml -o output/example_python_model
```
## python paho
```
asyncapi generate fromTemplate example_2.yml @asyncapi/python-paho-template -o output/example_python_paho
```
## python sanic (failing)
```
asyncapi generate fromTemplate example_2.yml @asyncapi/python-sanic-template -o output/example_python_sanic
```




# note
- apparently the these templates only work on AsyncAPI v2, not v3 (kraken_3.yml does not work)
- model gen supports: typescript, csharp, golang, java, javascript, dart, python, rust, kotlin, php, cplusplus, scala
- the `ag` command seems to be deprecated and cannot generate code properly
- you can install `asyncapi-preview` extension on vs code for preview

# todo
- gather binance asyncAPI
- verify if the binance models can be generated on python/rust
- verify if traits could be implemented on top of the generated model
- package model with its version
#!/usr/bin/env python3
import asyncio
import os
import re
from enum import Enum


class Parser(Enum):
    ASYNC_API = 'asyncapi'
    OPEN_API = 'openapi'


class Language(Enum):
    PYTHON = 'python'
    RUST = 'rust'


def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text  # Return unchanged if suffix not found or doesn't match


async def generate_rust_models(yaml_file, parser):
    # for testing
    # output_dir = "output/"
    # for production
    languages = [Language.PYTHON, Language.RUST]
    if parser == Parser.ASYNC_API:
        output = remove_suffix(yaml_file, '_asyncapi.yml')
        for language in languages:
            output_dir = f"target/{language.value}/{output}/model"
            command = f"asyncapi generate models {language.value} {yaml_file} -o {output_dir}"
            print(f"command: {command}")
            proc = await asyncio.create_subprocess_shell(command)
            await proc.communicate()
    elif parser == Parser.OPEN_API:
        # todo implement the naming convension
        print("todo implement open API parser")
    else:
        raise ValueError(f"Unknown parser type: {parser}")


def list_yaml(yaml_directory):
    [f for f in os.listdir(yaml_directory) if re.match(
        r'.yaml$', f)]


async def main():
    # async api
    parser = Parser.ASYNC_API
    asyncapi_yaml_directory = './asyncapi/'
    yaml_list = list_yaml(asyncapi_yaml_directory)
    for yaml in yaml_list:
        print(f"generating {yaml}")
        await generate_rust_models(os.path.join(asyncapi_yaml_directory, yaml), parser)

    # open api
    parser = Parser.OPEN_API
    openapi_yaml_directory = './openapi/'
    yaml_list = list_yaml(openapi_yaml_directory)
    for yaml in yaml_list:
        print(f"generating {yaml}")
        await generate_rust_models(os.path.join(openapi_yaml_directory, yaml), parser)

if __name__ == "__main__":
    asyncio.run(main())

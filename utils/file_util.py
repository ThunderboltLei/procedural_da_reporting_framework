"""
@author raymanlei
@since 2022-05-09 16:31:08
"""
from functools import singledispatch
from typing import Union

from consts import symbol_constants
from utils import PYTHON_SCRIPT_TARGET_PATH


@singledispatch
def writestr(filename, content) -> Union[str, str, str]:
    with open(PYTHON_SCRIPT_TARGET_PATH + symbol_constants.SLASH + filename, 'w', encoding='UTF-8') as fw:
        fw.write(content)
        fw.close()


@writestr.register
def _(filename: str, content: str, charname: str):
    with open(PYTHON_SCRIPT_TARGET_PATH + symbol_constants.SLASH + filename, 'w', encoding=charname) as fw:
        fw.write(content)
        fw.close()


if __name__ == '__main__':
    writestr('hello.py', '# hello world')

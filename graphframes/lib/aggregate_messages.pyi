#
# Copyright 2021 zero323
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject
from pyspark import SparkContext
from pyspark.sql import Column, DataFrame
from typing import Any, Callable, Type, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")

def _java_api(jsc: Type[SparkContext]) -> JavaObject: ...

class _ClassProperty:
    f: Callable[[_U], _T]
    __doc__: str
    def __init__(self, f: Callable[[_U], _T]) -> None: ...
    def __get__(self, instance: Any, owner: _U) -> _T: ...

class AggregateMessages:
    def src(cls) -> Column: ...
    def dst(cls) -> Column: ...
    def edge(cls) -> Column: ...
    def msg(cls) -> Column: ...
    @staticmethod
    def getCachedDataFrame(df: DataFrame) -> DataFrame: ...

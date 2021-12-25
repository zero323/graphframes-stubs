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

from graphframes.graphframe import GraphFrame as GraphFrame
from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject
from pyspark.ml.wrapper import JavaWrapper, _jvm as _jvm  # type: ignore[attr-defined]
from pyspark.sql import Column, DataFrame

basestring = str

class Pregel(JavaWrapper):
    graph: GraphFrame
    _java_obj: JavaObject
    def __init__(self, graph: GraphFrame) -> None: ...
    def setMaxIter(self, value: int) -> Pregel: ...
    def setCheckpointInterval(self, value: int) -> Pregel: ...
    def withVertexColumn(
        self, colName: str, initialExpr: Column, updateAfterAggMsgsExpr: Column
    ) -> Pregel: ...
    def sendMsgToSrc(self, msgExpr: Column) -> Pregel: ...
    def sendMsgToDst(self, msgExpr: Column) -> Pregel: ...
    def aggMsgs(self, aggExpr: Column) -> Pregel: ...
    def run(self) -> DataFrame: ...
    @staticmethod
    def msg() -> Column: ...
    @staticmethod
    def src(colName: str) -> Column: ...
    @staticmethod
    def dst(colName: str) -> Column: ...
    @staticmethod
    def edge(colName: str) -> Column: ...

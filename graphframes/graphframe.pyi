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

from graphframes._typing import (
    AlgorithmType as AlgorithmType,
    ExpressionOrColumn as ExpressionOrColumn,
)
from graphframes.lib import Pregel as Pregel
from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject
from pyspark import SparkContext
from pyspark.sql import DataFrame, SQLContext
from pyspark.storagelevel import StorageLevel
from typing import Any, List, Optional, Tuple

basestring = str

def _from_java_gf(jgf: JavaObject, sqlContext: SQLContext) -> GraphFrame: ...
def _java_api(jsc: SparkContext) -> JavaObject: ...

class GraphFrame:
    _vertices: DataFrame
    _edges: DataFrame
    _sqlContext: SQLContext
    _sc: SparkContext
    _jvm_gf_api: JavaObject
    ID: str
    SRC: str
    DST: str
    _ATTR: str
    _jvm_graph: JavaObject
    def __init__(self, v: DataFrame, e: DataFrame) -> None: ...
    @property
    def vertices(self) -> DataFrame: ...
    @property
    def edges(self) -> DataFrame: ...
    def __repr__(self) -> str: ...
    def cache(self) -> GraphFrame: ...
    def persist(self, storageLevel: StorageLevel = ...) -> GraphFrame: ...
    def unpersist(self, blocking: bool = ...) -> GraphFrame: ...
    @property
    def outDegrees(self) -> DataFrame: ...
    @property
    def inDegrees(self) -> DataFrame: ...
    @property
    def degrees(self) -> DataFrame: ...
    @property
    def triplets(self) -> DataFrame: ...
    @property
    def pregel(self) -> Pregel: ...
    def find(self, pattern: str) -> DataFrame: ...
    def filterVertices(self, condition: ExpressionOrColumn) -> GraphFrame: ...
    def filterEdges(self, condition: ExpressionOrColumn) -> GraphFrame: ...
    def dropIsolatedVertices(self) -> GraphFrame: ...
    def bfs(
        self,
        fromExpr: ExpressionOrColumn,
        toExpr: ExpressionOrColumn,
        edgeFilter: Optional[ExpressionOrColumn] = ...,
        maxPathLength: int = ...,
    ) -> DataFrame: ...
    def aggregateMessages(
        self,
        aggCol: ExpressionOrColumn,
        sendToSrc: Optional[ExpressionOrColumn] = ...,
        sendToDst: Optional[ExpressionOrColumn] = ...,
    ) -> DataFrame: ...
    def connectedComponents(
        self,
        algorithm: AlgorithmType = ...,
        checkpointInterval: int = ...,
        broadcastThreshold: int = ...,
    ) -> DataFrame: ...
    def labelPropagation(self, maxIter: int) -> DataFrame: ...
    def pageRank(
        self,
        resetProbability: float = ...,
        sourceId: Optional[Any] = ...,
        maxIter: Optional[int] = ...,
        tol: Optional[float] = ...,
    ) -> GraphFrame: ...
    def parallelPersonalizedPageRank(
        self,
        resetProbability: float = ...,
        sourceIds: Optional[List[Any]] = ...,
        maxIter: Optional[int] = ...,
    ) -> GraphFrame: ...
    def shortestPaths(self, landmarks: List[Any]) -> DataFrame: ...
    def stronglyConnectedComponents(self, maxIter: int) -> DataFrame: ...
    def svdPlusPlus(
        self,
        rank: int = ...,
        maxIter: int = ...,
        minValue: float = ...,
        maxValue: float = ...,
        gamma1: float = ...,
        gamma2: float = ...,
        gamma6: float = ...,
        gamma7: float = ...,
    ) -> Tuple[DataFrame, float]: ...
    def triangleCount(self) -> DataFrame: ...

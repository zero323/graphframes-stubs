from graphframes import GraphFrame
from typing import Optional

class BeliefPropagation:
    @classmethod
    def runBPwithGraphFrames(cls, g: GraphFrame, numIter: int) -> GraphFrame: ...
    @staticmethod
    def _colorGraph(g: GraphFrame) -> GraphFrame: ...
    @staticmethod
    def _sigmoid(x: Optional[float]) -> Optional[float]: ...

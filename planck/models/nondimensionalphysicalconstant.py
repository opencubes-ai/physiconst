from typing import Dict


# --------------------------------------------------------------------------- #
# Main Class                                                                  #
# --------------------------------------------------------------------------- #


class NonDimensionalPhysicalConstant(float):
    def __init__(
        self,
        symbol: str,
        name: str = None,
        value: float = None,
    ):
        float.__init__(value)
        self.symbol = symbol
        self.name = name

    def __new__(cls, symbol, name, value):
        return float.__new__(cls, value)

    def __repr__(self, *args, **kwargs):
        s = ""
        s += f"{self.name} [{self.symbol}]:\n"
        s += super().__repr__(*args, **kwargs)
        return s

    # def __repr__(self, *args, **kwargs):
    #     s = ""
    #     s += "{0:s} ({1:s}) : ".format(self.name, self.symbol)
    # #     s += str(self)
    #     s += "\n"
    #     return s

    @staticmethod
    def keys():
        return ["-"]

    def __getitem__(self, key):
        if key in ["", "-", "none", "None", None]:
            return self
        else:
            raise TypeError(f"Constant {self.symbol} has no units")

"""テスト用モジュール１
"""

from .package2 import package2

class package1():
    """test用クラス1
    """
    def __init__(self, message:str, num1:int, num2:int):
        """テストクラス１のコンストラクタ

        Args:
            message (str): 表示するメッセージ
            num1 (int): １つ目
            num2 (int): ２つ目
        """

        self._message = message
        self._num1 = num1
        self._num2 = num2

    def print_pac_msg(self):
        """メッセージ表示
        """
        print(self._message)
        print("add:", package2.add(self._num1, self._num2))
        print("mult:", package2.mult(self._num1, self._num2))
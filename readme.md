# wxテンプレート

wxPythonを手軽に使用するためのテンプレート。
完全に私用目的な上、wxPythonはド初心者なので期待はNG。

## 使い方

1. `ExampleModule.py`をコピー、好きなファイル名、クラス名にリネーム。
2. 作成したファイルの`self.layout`にレイアウトを、`self.bind`にイベントを入れる。
3. GetValueやSetValueメソッドでモジュール間で値を共有できる。
    * なおモジュール間でイベントの共有は出来ない。
        * いつの日か直したいなぁ。
4. `main.py`の`layout`に作ったクラスを入れる。
5. `main.py`を動かす。

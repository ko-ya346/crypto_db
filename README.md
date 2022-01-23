# 目的
- 仮想通貨bot運用のためのdbを作成
- SQL, DBの練習

# memo
## 1/23
### やったこと
- create tableクエリ書いた
- insertをpythonから実行する練習した
- pre-commit導入してgit commit時にlinter/formatter走るようにした

### 思ったこと
- csvでよくない？
    - SQLの練習なので。。。
- 何のデータを入れる？
    - ccxtのbf apiだとsince引数を使用できず、直前のohlcvデータしか取得できない
        - bitmexなら取得できた
    - そもそもccxtのohlcはどうやって算出してるの？
- tableからデータを呼び出してpythonで使用するためのスクリプト書く
- パラメータをベタ書きしてるのでなんとかしたい
    - yamlで管理
- SQL慣れてないので、頻出する操作をまとめたい（自分用）

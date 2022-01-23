from typing import Any

import MySQLdb


def connect_mysql(host: str, user: str, passwd: str, db=str):
    """
    mysqlサーバーに接続する
    """
    try:
        connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        return connection
    except MySQLdb._exceptions.OperationalError:
        print("Failed connection.")
        return


def insert_ohlcv():
    pass


if __name__ == "__main__":
    # configで管理
    params = dict(host="localhost", user="kouya346", passwd="52876398", db="bitflyer")
    connection = connect_mysql(**params)
    print(type(connection))

    cursor = connection.cursor()

    # テーブル削除
    cursor.execute("DROP TABLE IF EXISTS btc_jpy;")

    # テーブル作成用のクエリ読み込み
    # BTC/JPYベタ書きしてる
    with open("../sql/bf_btc_jpy.sql") as f:
        query = f.read()

    cursor.execute(query)

    # サンプルデータを挿入（ccxtのohlcvデータ）
    OHLCV = [1642917240000, 35400.0, 35399.0, 35360.5, 35360.5, 695400.0]
    timestmp, *ohlc, vol = OHLCV
    timestmp //= 1000
    ohlc = list(map(int, ohlc))
    vol = round(vol, 8)

    ohlcv_data = (timestmp, *ohlc, vol)
    query = f"INSERT into btc_jpy (timestamp_bigint, op, hi, lo, cl, vol) VALUES {(ohlcv_data)}"
    cursor.execute(query)
    print("Finished insert")

    # insertされたか確認
    for row in cursor:
        print(row)

    # 確定
    connection.commit()
    connection.close()

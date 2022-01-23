from typing import Any

import MySQLdb


def connect_mysql(host: str, user: str, passwd: str, db=str) -> Any:
    """
    mysqlサーバーに接続する
    """
    try:
        connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        return connection.cursor()
    except MySQLdb._exceptions.OperationalError:
        print("Failed connection.")
        return


def execute_sql(cursor, query: str):
    return


if __name__ == "__main__":
    params = dict(host="localhost", user="kouya346", passwd="52876398", db="bitflyer")
    connection = connect_mysql(**params)
    print(type(connection))

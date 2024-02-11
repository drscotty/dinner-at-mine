from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from data import DbType


_db_uid = "HeliumFillApp"
_db_pwd = "h3liumappread3r"
_database_connection_string = "sn1oxf05/HeliumDB"


def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None


def CreateDbEngine(db_type: DbType.DbType, conn : str = None, uid: str = None, pwd: str = None, sqlLiteName: str = "data"):
    """Created the database connection engine from the sqlalchemy create_engine routine.

    Args:
        db_type (DbType.DbType): Enumerator to define the database type
        sqlLiteName (str, optional): Name of the desired SqlLite database. Defaults to "data".

    Returns:
        Engine: the database connection engine from sqlalchemy
    """
    
    if uid == None: uid = _db_uid
    if pwd == None: pwd = _db_pwd
    if conn == None: conn = _database_connection_string
    
    if debugger_is_active():
        echo = True
    else:
        echo = False

    if db_type == DbType.DbType.SqlLite:
        engine = create_engine(f"sqlite:///data/{sqlLiteName}.db", echo=echo)
    else:
        engine = create_engine(f"mssql+pyodbc://{uid}:{pwd}@{conn}?driver=ODBC+Driver+17+for+SQL+Server", echo=echo)

    return engine


engine = CreateDbEngine(DbType.DbType.SqlMsServer)

Session = sessionmaker(bind=engine)
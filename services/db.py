import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

DB_CONN_SERVER = os.getenv("DB_CONN_SERVER")
DB_CONN_DB = os.getenv("DB_CONN_DB")
DB_CONN_USER = os.getenv("DB_CONN_USER")
DB_CONN_PW = os.getenv("DB_CONN_PW")
DB_CONN_SCHEMA=os.getenv("DB_CONN_SCHEMA")
DB_CONN_META=os.getenv("DB_CONN_META")

# print(DB_CONN_SERVER, DB_CONN_DB, DB_CONN_USER, DB_CONN_SCHEMA, DB_CONN_META)

cnxn = pyodbc.connect('Driver={SQL Server};'
                      f'Server={DB_CONN_SERVER};'
                      f'Database={DB_CONN_DB};'
                      'Trusted_Connection=no;'
                      f'UID={DB_CONN_USER};'
                      f'PWD={DB_CONN_PW}')
cursor = cnxn.cursor()

def select(table_name, display, condition=[], orderby=[], orderasc=True, top=None):
    values = []
    where = ''
    for c in condition:
        if type(c) is str:
            where += f' {c} ' if c not in ["(", ")"] else c
        elif type(c) is tuple:
            where += f"{c[0]} {c[1]} ?"
            values.append(c[2])
        
    query = f"""
        SELECT {"TOP " + str(top) if top else ""} {",".join(display)}
        FROM {DB_CONN_SCHEMA}.{table_name}
        {"WHERE" if where != "" else ""} {where}
        {"ORDER BY " + ", ".join(orderby) + (" ASC" if orderasc else " DESC") if len(orderby) > 0 else ""}
    """
    rows = cursor.execute(query, *values).fetchall()
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in rows]

def insert(table_name, columns, values):
    query = f"""
        INSERT INTO {DB_CONN_SCHEMA}.{table_name}
        ({", ".join(columns)})
        VALUES ({", ".join(["?" for _ in columns])})
    """
    cursor.execute(query, *values)
    cnxn.commit()

def update(table_name, condition, values, top=None):
    w_values = []
    where = ""
    for c in condition:
        if type(c) is str:
            where += f' {c} ' if c not in ["(", ")"] else c
        elif type(c) is tuple:
            where += f"{c[0]} {c[1]} ?"
            w_values.append(c[2])
    s_values = []
    set = []
    for v in values:
        set.append(f"{v[0]} = ?")
        s_values.append(v[1])
    s_values.extend(w_values)
    query = f"""
        UPDATE {"TOP (" + str(top) + ")" if top else ""} {DB_CONN_SCHEMA}.{table_name}
        SET {", ".join(set)}
        {"WHERE" if where != "" else ""} {where};
    """
    cursor.execute(query, *s_values)
    cnxn.commit()

def delete(table_name, condition, top=None):
    values = []
    where = ""
    for c in condition:
        if type(c) is str:
            where += f' {c} ' if c not in ["(", ")"] else c
        elif type(c) is tuple:
            where += f"{c[0]} {c[1]} ?"
            values.append(c[2])
    query = f"""
        DELETE {"TOP (" + str(top) + ")" if top else ""} FROM {DB_CONN_SCHEMA}.{table_name}
        {"WHERE" if where != "" else ""} {where}
    """
    cursor.execute(query, *values)
    cnxn.commit()

def create_table(table_name, columns):
    query = f"""
        CREATE TABLE {DB_CONN_SCHEMA}.{table_name}
        ({", ".join(columns)});
    """
    cursor.execute(query)
    cnxn.commit()

def table_add_column(table_name, column):
    query = f"""
        ALTER TABLE {DB_CONN_SCHEMA}.{table_name}
        ADD {column};
    """
    cursor.execute(query)
    cnxn.commit()

# def table_rename_column(table_name, oldcolumn, newcolumn):
#     query = f"""
#         ALTER TABLE {DB_CONN_SCHEMA}.{table_name}
#         ADD {column};
#     """
#     cursor.execute(query)
#     cnxn.commit()

def sql(query, values=(), returns=False):
    if returns:
        rows = cursor.execute(query, values).fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    else:
        cursor.execute(query, values)
        cnxn.commit()
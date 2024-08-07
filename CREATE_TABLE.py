from connection_to_db import session
import asyncio
from sqlalchemy.sql import text



sql_file_path = 'create_tables.sql'
sql_scripts=text("")
with open(sql_file_path, 'r') as sql_file:
    sql_scripts = [script.strip() for script in sql_file.read().split(";") if script.strip()]
    
    for script in sql_scripts:
        session.execute(text(script))
    session.commit()


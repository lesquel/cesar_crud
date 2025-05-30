from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///crudregistro.db')

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM registro_cliente"))
    for row in result:
        print(row)

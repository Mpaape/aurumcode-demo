def pedidos_do_cliente(db, cliente_id):
    return db.execute("select * from pedidos where cliente = ?", (cliente_id,)).fetchall()

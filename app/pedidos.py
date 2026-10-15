def pedidos_do_cliente(db, cliente_id):
    return db.execute("select * from pedidos where cliente = ?", (cliente_id,)).fetchall()


def pedidos_por_status(db, status):
    return db.execute("select * from pedidos where status = ?", (status,)).fetchall()

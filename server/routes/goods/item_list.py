from server.main_ import app, orm, c


@app.route('/goods/item_list', methods=['GET', ])
def _goods_item_list():
    store_id = c.session['store']
    if c.is_GET():
        pass
    elif c.is_POST():
        pass

    return c.display(store_id=store_id)


@app.route('/goods/item_list/<int:_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _goods_item_list_(_id):
    store_id = c.session['store']
    if c.is_GET():
        pass
    elif c.is_POST():
        pass

    return c.display()

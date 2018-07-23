from server.main_ import app, orm, c

thead = [
    {'tag': '#', 'name': 'no', 'width': 100, },
    {'tag': None, 'name': '분류명', 'width': None, },
]

form_types = [
    {'tag': None, 'name': '분류명', 'type': 'input', 'valid': None, },
]


def itemgroup_query(ss, store_id):
    return ss.query(orm.상품_분류) \
        .filter_by(s=store_id) \
        .order_by(ss.asc(orm.상품_분류.분류명)) \
        .filter_by(isdel=c.X)


@app.route('/goods/itemgroup', methods=['GET', ])
def _goods_itemgroup():
    store_id = c.session['store']

    if c.is_GET():
        if c.is_json():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                lst = c.for_json_l(itemgroup_query(ss, store_id).all())
                return c.jsonify(lst)
        return c.display(item=c.newitem_web(orm.상품_분류, c.session),
                         thead=thead,
                         form_types=form_types,
                         no=store_id)


@app.route('/goods/itemgroup/<int:_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _goods_itemgroup_(_id):
    store_id = c.session['store']

    if c.is_json():
        if c.is_GET():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_분류, no=_id)
                return c.jsonify(c.for_json(only))
        elif c.is_POST():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.newitem_web(orm.상품_분류, c.session)
                cnt = itemgroup_query(ss, store_id).count()
                only.번호 = cnt + 1
                for k, v in c.data_POST().items():
                    if hasattr(only, k) and k != 'no':
                        if getattr(only, k) != v:
                            setattr(only, k, v)
                ss.add(only)
                return 'added'
        elif c.is_PUT():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_분류, no=_id)
                if only.s == c.session['store']:
                    for k, v in c.data_POST().items():
                        if hasattr(only, k) and k != 'no':
                            if getattr(only, k) != v:
                                print(k, 'is changed')
                                setattr(only, k, v)
                    only.issync = None
                    return 'modified'
                else:
                    c.abort(403)
        elif c.is_DELETE():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_분류, no=_id)
                if only.s == c.session['store']:
                    only.isdel = c.O
                    l = itemgroup_query(ss, store_id).all()
                    for i in range(len(l)):
                        l[i].번호 = i + 1
                    only.issync = None
                    return 'deleted'
                else:
                    c.abort(403)
    c.abort(404)

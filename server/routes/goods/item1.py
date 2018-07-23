from server.main_ import app, orm, c

thead = [
    {'tag': '#', 'name': 'no', 'width': 50, },
    {'tag': None, 'name': '분류', 'width': 120, },
    {'tag': None, 'name': '품목명', 'width': None, },
    {'tag': None, 'name': '단가', 'width': 120, },
    {'tag': None, 'name': '부가세과세', 'width': 100, },
    {'tag': None, 'name': '부가세포함', 'width': 100, },
    {'tag': None, 'name': '시가여부', 'width': 100, },
]

form_types = [
    {'tag': None, 'name': '분류', 'type': 'select', 'valid': None, },
    {'tag': None, 'name': '품목명', 'type': 'input', 'valid': None, },
    {'tag': None, 'name': '설명', 'type': 'input', 'valid': None, },
    {'tag': None, 'name': '품목형태', 'type': 'input', 'valid': None, },
    {'tag': None, 'name': '단가', 'type': 'input', 'valid': 'integer', },
    {'tag': None, 'name': '부가세과세', 'type': 'checkbox', 'valid': None, },
    {'tag': None, 'name': '부가세포함', 'type': 'checkbox', 'valid': None, },
    {'tag': None, 'name': '시가여부', 'type': 'checkbox', 'valid': None, },
    # {'tag': None, 'name': '옵션코드', 'type': 'input', 'valid': None, },
    # {'tag': None, 'name': '프린터', 'type': 'input', 'valid': None, },
    {'tag': None, 'name': '바코드', 'type': 'input', 'valid': None, },
]


@app.route('/goods/item', methods=['GET', ])
def _goods_item():
    store_id = c.session['store']
    with orm.session_scope() as ss:  # type:c.typeof_Session
        gd = c.dict_itemgroup(orm, store_id)
        gl = list(gd.values())
        form_types[0]['l'] = gl
        # print(gd, gl)
        if c.is_GET():
            if c.is_json():
                l = c.for_json_l(
                    c.simple_query(ss, orm.상품_품목, s=store_id, order_by_asc='no'))
                for i in l:
                    i['분류'] = gd[i['분류no']]
                    i['idx'] = i['no']
                    i['enabled'] = True
                return c.jsonify(l)
            return c.display(item=c.newitem_web(orm.상품_품목, c.session),
                             thead=thead,
                             form_types=form_types,
                             no=store_id,
                             gl=gl)


@app.route('/goods/item/<int:_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _goods_item_(_id):
    store_id = c.session['store']
    gd = c.dict_itemgroup(orm, store_id)
    if c.is_json():
        if c.is_GET():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_품목, no=_id)
                only.분류 = gd[only.분류no]
                return c.jsonify(c.for_json(only))
        elif c.is_POST():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.newitem_web(orm.상품_품목, c.session)
                for k, v in c.data_POST().items():
                    if hasattr(only, k) and k != 'no':
                        if getattr(only, k) != v:
                            setattr(only, k, v)
                only.분류no = c.fs2i(c.data_POST()['분류'].split('|', 1)[0].strip())
                ss.add(only)
                return 'added'
        elif c.is_PUT():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_품목, no=_id)
                if only.s == c.session['store']:
                    for k, v in c.data_POST().items():
                        if hasattr(only, k) and k != 'no':
                            if getattr(only, k) != v:
                                print(k, 'is changed')
                                setattr(only, k, v)
                    only.분류no = c.fs2i(c.data_POST()['분류'].split('|', 1)[0].strip())
                    only.issync = None
                    return 'modified'
                else:
                    c.abort(403)
        elif c.is_DELETE():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.simple_query(ss, orm.상품_품목, no=_id)
                if only.s == c.session['store']:
                    only.isdel = c.O
                    only.issync = None
                    return 'deleted'
                else:
                    c.abort(403)
    c.abort(404)

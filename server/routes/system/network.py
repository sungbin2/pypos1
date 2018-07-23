from server.main_ import app, orm, c

thead = [
    {'tag': '#', 'name': 'idx', 'width': 100, },
    {'tag': None, 'name': '기기명', 'width': None, },
    {'tag': None, 'name': 'IP', 'width': 120, },
    {'tag': None, 'name': 'PORT', 'width': 100, },
    {'tag': None, 'name': 'DB', 'width': 70, },
    {'tag': None, 'name': '계산', 'width': 70, },
    {'tag': None, 'name': '주문', 'width': 70, },
    {'tag': None, 'name': '프린터', 'width': 70, },
]
form_types = [
    {'tag': None, 'name': '기기명', 'type': 'input', 'valid': None, },
    {'tag': None, 'name': 'IP', 'type': 'input', 'valid': 'ipv4', },
    {'tag': None, 'name': 'PORT', 'type': 'input', 'valid': 'integer[1024..65535]', },
    {'tag': None, 'name': 'DB', 'type': 'checkbox', 'valid': None, },
    {'tag': None, 'name': '계산', 'type': 'checkbox', 'valid': None, },
    {'tag': None, 'name': '주문', 'type': 'checkbox', 'valid': None, },
    {'tag': None, 'name': '프린터', 'type': 'checkbox', 'valid': None, },
]


@app.route('/system/network', methods=['GET', 'POST'])
def _system_network():
    store_id = c.session['store']
    only = c.get_settings(orm, store_id)

    if c.is_GET():
        if c.is_json():
            return c.jsonify(only.j['네트워크'])
        else:
            return c.display(thead=thead, form_types=form_types)
    elif c.is_POST():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            next_one = c.newitem_web(orm.settings, c.session)
            next_one.j = only.j.copy()
            for each in c.data_POST():
                next_one.j['네트워크'] = c.json.loads(each)
            ss.add(next_one)
            return 'modified'

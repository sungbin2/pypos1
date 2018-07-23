from lxml import etree
from server.main_ import app, orm, c


def get_config1(store_id):
    only = c.get_settings(orm, store_id)
    return only.j['설정']


@app.route('/system/config1', methods=['GET'])
def _system_config1():
    store_id = c.session['store']

    if c.is_GET():
        xml_path = c.os.path.join(c.os.path.dirname(__file__), '../../static/KBIZ_preferences.xml')
        f = open(xml_path, encoding='utf-8')
        tree = etree.parse(f)
        xml_root = tree.getroot()

        form_types = []

        for a in xml_root:
            form_types.append({'name': a.get('name'), 'type': 'divider'})
            for b in a:
                _c = {'tag': None,
                      'name': b.get('key') + c.SEP + b.get('name'),
                      'type': b.get('value'),
                      'valid': None}
                if b.get('value') == 'select':
                    _c['l'] = []
                    for d in b:
                        _c['l'].append(d.get('name'))
                form_types.append(_c)

        return c.display(xml=xml_root, form_types=form_types, item={"no": store_id}, store_id=store_id)


@app.route('/system/config1/<int:store_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _system_config1_(store_id):
    if c.is_json():
        if c.is_GET():
            d = {k + c.SEP + v['k']: v['v'] for k, v in get_config1(store_id).items()}
            return c.jsonify(d)
        elif c.is_PUT():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                only = c.get_settings(orm, store_id)
                next_one = c.newitem_web(orm.settings, c.session)
                next_one.j = only.j.copy()
                for k, v in c.data_POST().items():
                    if c.SEP in k and 'checkbox' not in k:
                        _n = k.split(c.SEP, 1)[0]
                        _k = k.split(c.SEP, 1)[1]
                        _v = v
                        next_one.j['설정'][_n] = {'k': _k, 'v': _v}

                ss.add(next_one)
            return 'modified'

    c.abort(404)

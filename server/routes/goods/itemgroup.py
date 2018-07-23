from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date


@app.route('/goods/itemgroup', methods=['GET', ])
def _goods_itemgroup():
    store_id = c.session['store']

    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/goods/itemgroup/<int:_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _goods_itemgroup_(_id):
    store_id = c.session['store']
    if c.is_GET():
        if True:  # c.is_json()
            l = []
            with orm.session_scope() as ss:  # type:c.typeof_Session
                q1 = ss.query(orm.상품_분류) \
                    .filter_by(s=c.session['store']) \
                    .filter_by(isdel='X') \
                    .all()
                for x in q1:
                    dummy = x.__dict__.copy()
                    del dummy['_sa_instance_state']
                    for k, v in dummy.items():
                        if v is None:
                            dummy[k] = ''
                        elif isinstance(v, date):
                            dummy[k] = v.isoformat()
                        elif isinstance(v, datetime):
                            dummy[k] = v.isoformat(' ')
                    l.append(dummy)
            return c.jsonify(l)
    elif c.is_PUT():
        with orm.session_scope() as ss:  # type:c.typeof_Session

            temp = []
            for i in c.data_POST():
                for j in c.json.loads(i):
                    temp.append(j)

            only = c.simple_query(ss, orm.상품_분류, s=c.session['store'])
            for i in temp:
                if '코드' not in i:
                    only1 = c.newitem_web(orm.상품_분류, c.session)
                    only1.분류명 = i['대분류']
                    ss.add(only1)

                elif i['코드'] != None:

                    for x in only:
                        if x.i == i['코드']:
                            x.분류명 = i['대분류']
                            x.isdel = i['isdel']

            return 'modified'


















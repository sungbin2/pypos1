from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date


@app.route('/goods/item', methods=['GET', ])
def _goods_item():
    store_id = c.session['store']

    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/goods/item/<int:_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _goods_item_(_id):
    store_id = c.session['store']
    if c.is_GET():
        if True:  # c.is_json()
            l = []
            with orm.session_scope() as ss:  # type:c.typeof_Session
                q1 = ss.query(orm.상품_품목) \
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
    elif c.is_POST():
        with orm.session_scope() as ss:  # type:c.typeof_Session


            if c.data_POST()['i'] == '신규':

                only = c.newitem_web(orm.상품_품목, c.session)
                for k, v in c.data_POST().items():
                    if hasattr(only, k) and k != 'i':
                        if getattr(only, k) != v:
                            setattr(only, k, v)

                ss.add(only)
                return 'modified'

            elif c.data_POST()['i'] != '신규':
                only = c.simple_query(ss, orm.상품_품목, s=c.session['store'])

                for x in only:

                    print(x.i, c.data_POST()['i'])
                    if int(x.i) == int(c.data_POST()['i']):
                        print(c.data_POST()['프린터j'])
                        for k, v in c.data_POST().items():
                            print(k,v)
                            if hasattr(x, k) and k != 'i':
                                if getattr(x, k) != v:
                                    print(k, 'is changed')
                                    setattr(x, k, v)
                        x.issync = None
                        return 'modified'

            temp = []
            # for i in c.data_POST():
            #     for j in c.json.loads(i):
            #         temp.append(j)

            # print(temp)

            # only = c.simple_query(ss, orm.상품_품목, s=c.session['store'])
            # for i in temp:
            #     if '코드' not in i:
            #         only1 = c.newitem_web(orm.상품_품목, c.session)
            #         only1.품목명 = i['명']
            #         ss.add(only1)
            #
            #     elif i['코드'] != None:
            #
            #         for x in only:
            #             if x.i == i['코드']:
            #                 x.품목명 = i['명']
            #                 x.isdel = i['isdel']

            return 'modified'






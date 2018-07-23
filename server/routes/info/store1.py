from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date
from flask import request


def _get_store1():
    with orm.session_scope() as ss:  # type:c.typeof_Session
        q1 = ss.query(orm.정보_가게) \
            .filter_by(id=c.session['store']) \
            .one()
        return c.OBJ_cp(q1)


@app.route('/info/store1', methods=['GET', 'POST'])
def _info_store1():
    if c.is_GET():
        return c.display()
    elif c.is_POST():

        user = request.form['content']
        print(user)

        return c.display()


@app.route('/info/store1/list', methods=['GET'])
def _info_store1_list():
    if c.is_GET():
        if True:  # c.is_json()
            l = []
            with orm.session_scope() as ss:  # type:c.typeof_Session
                q1 = ss.query(orm.공통_출력물관리) \
                    .filter_by(s=c.session['store']) \
                    .all()
                for x in q1:
                    dummy = x.__dict__.copy()
                    del dummy['_sa_instance_state']
                    for k, v in dummy.items():
                        if v is None:
                            dummy[k] = ''
                    l.append(dummy)
            return c.jsonify(l)


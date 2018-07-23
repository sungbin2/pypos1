from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date


@app.route('/info/staff1', methods=['GET', 'POST'])
def _info_staff1():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass


    return c.display()


@app.route('/info/staff1/list', methods=['GET'])
def _info_staff1_list():
    if c.is_GET():
        if True:  # c.is_json()
            l = []
            with orm.session_scope() as ss:  # type:c.typeof_Session
                q1 = ss.query(orm.정보_직원) \
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

from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date

def _get_member():
    with orm.session_scope() as ss:  # type:c.typeof_Session
        q1 = ss.query(orm.정보_가게) \
            .filter_by(id=c.session['store']) \
            .one()
        return c.OBJ_cp(q1)


@app.route('/member/member', methods=['GET', 'POST'])
def _member_member():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member/list', methods=['GET'])
def _member_member_list():
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



@app.route('/member/member1', methods=['GET', 'POST'])
def _member_member1():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member2', methods=['GET', 'POST'])
def _member_member2():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member3', methods=['GET', 'POST'])
def _member_member3():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member4', methods=['GET', 'POST'])
def _member_member4():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member5', methods=['GET', 'POST'])
def _member_member5():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member6', methods=['GET', 'POST'])
def _member_member6():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/member7', methods=['GET', 'POST'])
def _member_member7():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()
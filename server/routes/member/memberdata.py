from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date

def _get_memberdata():
    with orm.session_scope() as ss:  # type:c.typeof_Session
        q1 = ss.query(orm.정보_가게) \
            .filter_by(id=c.session['store']) \
            .one()
        return c.OBJ_cp(q1)


@app.route('/member/memberdata', methods=['GET', 'POST'])
def _member_memberdata():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata/list', methods=['GET'])
def _member_memberdata_list():
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



@app.route('/member/memberdata1', methods=['GET', 'POST'])
def _member_memberdata1():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata2', methods=['GET', 'POST'])
def _member_memberdata2():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata3', methods=['GET', 'POST'])
def _member_memberdata3():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata4', methods=['GET', 'POST'])
def _member_memberdata4():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata5', methods=['GET', 'POST'])
def _member_memberdata5():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata6', methods=['GET', 'POST'])
def _member_memberdata6():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata7', methods=['GET', 'POST'])
def _member_memberdata7():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata8', methods=['GET', 'POST'])
def _member_memberdata8():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/member/memberdata9', methods=['GET', 'POST'])
def _member_memberdata9():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()
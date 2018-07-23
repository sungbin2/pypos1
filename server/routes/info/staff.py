from server.main_ import app, orm, c
from dateutil import parser
from datetime import datetime, date

form_types = [
    {'k': 'id', 'type': 'input', 'alias': None},
    {'k': '가게명', 'type': 'input', 'alias': None},
    {'k': '대표자', 'type': 'input', 'alias': None},
    {'k': '사업자등록번호', 'type': 'input', 'alias': '사업자번호'},
    {'k': '우편번호', 'type': 'input', 'alias': None},
    {'k': '주소', 'type': 'input', 'alias': None},
    {'k': '상세주소', 'type': 'input', 'alias': None},
    {'k': '이메일', 'type': 'input', 'alias': None},
    {'k': '휴대폰', 'type': 'input', 'alias': None},
    {'k': '전화', 'type': 'input', 'alias': None},
    {'k': '팩스', 'type': 'input', 'alias': None},
    {'k': '가맹여부', 'type': 'radio', 'alias': None,
     'vl': ['단독점포', '직영점', '가맹점']},
    {'k': '업종', 'type': 'input', 'alias': None},
    {'k': '개점일', 'type': 'date', 'alias': None},
    {'k': '폐점일', 'type': 'date', 'alias': None},
]


def _get_staff():
    with orm.session_scope() as ss:  # type:c.typeof_Session
        q1 = ss.query(orm.정보_가게) \
            .filter_by(id=c.session['store']) \
            .one()
        return c.OBJ_cp(q1)


@app.route('/info/staff', methods=['GET', 'POST'])
def _info_staff():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass
    return c.display()


@app.route('/info/staff/list', methods=['GET'])
def _info_staff_list():
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

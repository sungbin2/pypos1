from server.main_ import app, orm, c
from dateutil import parser


def _get_store(store_id):
    with orm.session_scope() as ss:  # type:c.typeof_Session
        only = ss.query(orm.정보_가게) \
            .filter_by(no=store_id) \
            .one()

        return c.OBJ_cp(only)

def _get_account(store_id):
    with orm.session_scope() as ss:  # type:c.typeof_Session
        only = ss.query(orm.account) \
            .filter_by(s=store_id) \
            .one()

        return c.OBJ_cp(only)

@app.route('/info/storepwd')
def _info_storepwd_():
    return c.redirect(c.url_for('_info_storepwd', store_id=c.session['store']))


@app.route('/info/storepwd/<int:store_id>', methods=['GET', 'POST', 'PUT'])
def _info_storepwd(store_id):
    if c.is_GET():
        if c.is_json():
            return c.jsonify(_get_store(store_id).for_json())
        else:
            return c.display()


@app.route('/info/account')
def _info_account():
    return


@app.route('/info/account/<int:store_id>', methods=['GET', 'POST', 'PUT'])
def _info_account_(store_id):
    if c.is_GET():
        if c.is_json():
            return c.jsonify(_get_account(store_id).for_json())
        else:
            return c.display()
    elif c.is_POST() or c.is_PUT():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            only = ss.query(orm.account) \
                .filter_by(s=store_id) \
                .one()
            if only.패스워드 == c.pw_hash(c.data_POST('구패스워드')):
                only.패스워드 = c.pw_hash(c.data_POST('패스워드'))
            else:
                return 'diffrent'


        return 'modified'
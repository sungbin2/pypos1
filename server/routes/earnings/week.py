from server.main_ import app, orm, c



@app.route('/earnings/week', methods=['GET', ])
def _earnings_week():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week/<int:_id>', methods=['GET'])
def _earnings_week_(_id):
    store_id = c.session['store']
    cnt_weeks = {}

    cnt = 0
    if c.is_GET():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            lst = ss.query(orm.판매_품목) \
                .filter_by(isdel='X') \
                .filter(orm.판매_품목.d >= "2018-01-01") \
                .filter(orm.판매_품목.d <= "2018-12-31") \
                .all()

            for each in lst:
                d = each.d.strftime('%Y-%m-%d')
                if d not in cnt_weeks:
                    cnt_weeks[d] = {'영업일자': d,
                                   '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 }
                cnt_weeks[d]['총거래액'] += each.단가
                cnt_weeks[d]['총할인액'] += each.할인
                cnt_weeks[d]['실거래액'] += each.합계
                cnt_weeks[d]['세금'] += each.세
                cnt_weeks[d]['판매이익'] += (each.공급가 + each.면세)
                cnt_weeks[d]['영수건수'] += 1


        return c.jsonify(cnt_weeks)
    c.abort(404)


@app.route('/earnings/week1', methods=['GET', ])
def _earnings_week1():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

@app.route('/earnings/week2', methods=['GET', ])
def _earnings_week2():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week3', methods=['GET', ])
def _earnings_week3():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week4', methods=['GET', ])
def _earnings_week4():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week5', methods=['GET', ])
def _earnings_week5():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week6', methods=['GET', ])
def _earnings_week6():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week7', methods=['GET', ])
def _earnings_week7():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week8', methods=['GET', ])
def _earnings_week8():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/week9', methods=['GET', ])
def _earnings_week9():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

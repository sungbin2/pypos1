from server.main_ import app, orm, c



@app.route('/earnings/dayall/<int:_id>', methods=['GET'])
def _earnings_dayall_(_id):
    store_id = c.session['store']
    cnt_days = {}
    cnt_days['상품목록'] = {}
    cnt_days['상품분류'] = {}
    cnt_days['일자별'] = {}

    cnt = 0
    if c.is_GET():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            lst = ss.query(orm.판매_품목) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst:
                d = each.d.strftime('%Y-%m-%d')
                if d not in cnt_days['일자별']:
                    cnt_days['일자별'][d] = {'영업일자': d,
                                   '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 , '분류별' : {} ,'상품별' : {} , '수단별' : {}}
                cnt_days['일자별'][d]['총거래액'] += each.단가
                cnt_days['일자별'][d]['총할인액'] += each.할인
                cnt_days['일자별'][d]['실거래액'] += each.합계
                cnt_days['일자별'][d]['세금'] += each.세
                cnt_days['일자별'][d]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['영수건수'] += 1

                p = str(each.품목pi)

                if p not in cnt_days['일자별'][d]['분류별']:
                    cnt_days['일자별'][d]['분류별'][p] = {'총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수': 0}

                cnt_days['일자별'][d]['분류별'][p]['총거래액'] += each.단가
                cnt_days['일자별'][d]['분류별'][p]['총할인액'] += each.할인
                cnt_days['일자별'][d]['분류별'][p]['실거래액'] += each.합계
                cnt_days['일자별'][d]['분류별'][p]['세금'] += each.세
                cnt_days['일자별'][d]['분류별'][p]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['분류별'][p]['영수건수'] += 1

                s = each.품목i
                if s not in cnt_days['일자별'][d]['상품별']:
                    cnt_days['일자별'][d]['상품별'][s] = {'ppi': {}, '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수': 0}
                cnt_days['일자별'][d]['상품별'][s]['ppi'] = each.품목pi
                cnt_days['일자별'][d]['상품별'][s]['총거래액'] += each.단가
                cnt_days['일자별'][d]['상품별'][s]['총할인액'] += each.할인
                cnt_days['일자별'][d]['상품별'][s]['실거래액'] += each.합계
                cnt_days['일자별'][d]['상품별'][s]['세금'] += each.세
                cnt_days['일자별'][d]['상품별'][s]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['상품별'][s]['영수건수'] += 1

            lst1 = ss.query(orm.상품_품목) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst1:
                cnt_days['상품목록'].update({each.i: each.품목명})

            lst2 = ss.query(orm.상품_분류) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst2:
                cnt_days['상품분류'].update({each.i: each.분류명})


            lst1 = ss.query(orm.결제) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst1:
                d = each.d.strftime('%Y-%m-%d')

                cash = str(each.결제수단)

                if cash not in cnt_days['일자별'][d]['수단별']:
                    cnt_days['일자별'][d]['수단별'][cash] = {'판매i' : 0 , '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수': 0}
                cnt_days['일자별'][d]['수단별'][cash]['실거래액'] += each.합계
                cnt_days['일자별'][d]['수단별'][cash]['세금'] += each.세
                cnt_days['일자별'][d]['수단별'][cash]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['수단별'][cash]['영수건수'] += 1





        return c.jsonify(cnt_days)
    c.abort(404)


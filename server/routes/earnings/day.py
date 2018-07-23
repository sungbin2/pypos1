from server.main_ import app, orm, c



@app.route('/earnings/day', methods=['GET', ])
def _earnings_day():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/dayall', methods=['GET', ])
def _earnings_dayall():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/dayalldetail', methods=['GET', ])
def _earnings_dayalldetail():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/dayreceiptdetail', methods=['GET', ])
def _earnings_dayreceiptdetail():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day/<int:_id>&<dates>&<datee>', methods=['GET'])
def _earnings_day_(_id,dates,datee):
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
                .filter(orm.판매_품목.d >= dates) \
                .filter(orm.판매_품목.d <= datee) \
                .all()

            for each in lst:
                d = each.d.strftime('%Y-%m-%d')
                if d not in cnt_days['일자별']:
                    cnt_days['일자별'][d] = {'영업일자': d,
                                   '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '판매건수' : 0 ,'영수건수' : 0 , '분류별' : {} ,'상품별' : {} , '수단별' : {} ,'영수증별' : {} }
                cnt_days['일자별'][d]['총거래액'] += each.단가
                cnt_days['일자별'][d]['총할인액'] += each.할인
                cnt_days['일자별'][d]['실거래액'] += each.합계
                cnt_days['일자별'][d]['세금'] += each.세
                cnt_days['일자별'][d]['판매이익'] += (each.공급가 + each.면세)

                cnt_days['일자별'][d]['판매건수'] += 1

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


            lst3 = ss.query(orm.결제) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .filter(orm.결제.d >= dates) \
                .filter(orm.결제.d <= datee) \
                .all()



            for each in lst3:
                d = each.d.strftime('%Y-%m-%d')
                cashm = {'현금', '카드', '카드(임의)','포인트'}
                for each1 in cashm:
                    cnt_days['일자별'][d]['수단별'][each1] = {'판매i': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수': 0}

            for each in lst3:
                d = each.d.strftime('%Y-%m-%d')
                cash = each.결제수단


                # if cash not in cnt_days['일자별'][d]['수단별']:
                #     cnt_days['일자별'][d]['수단별'][cash] = {'판매i' : 0 , '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수': 0}
                cnt_days['일자별'][d]['수단별'][cash]['실거래액'] += each.합계
                cnt_days['일자별'][d]['수단별'][cash]['세금'] += each.세
                cnt_days['일자별'][d]['수단별'][cash]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['수단별'][cash]['영수건수'] += 1

            lst4 = ss.query(orm.판매) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .filter(orm.판매.d >= dates) \
                .filter(orm.판매.d <= datee) \
                .all()
            d=0
            d1=0
            d2=0
            d3=0

            for each in lst4:
                d = each.d.strftime('%Y-%m-%d')
                
                d1 = each.주문일시.strftime('%H:%M:%S')
                if each.결제일시:
                    d2 = each.결제일시.strftime('%H:%M:%S')
                if each.취소일시:
                    d3 = each.취소일시.strftime('%H:%M:%S')
                
                r = each.i
                if r not in cnt_days['일자별'][d]['영수증별']:
                    cnt_days['일자별'][d]['영수증별'][r] = { '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '주문일시': d1 , '결제일시': d2, '취소일시': d3 ,'테이블명': "" ,'상품' : {},'영수건수':0 }
                cnt_days['일자별'][d]['영수증별'][r]['총거래액'] = each.총금액
                cnt_days['일자별'][d]['영수증별'][r]['총할인액'] = each.총할인
                cnt_days['일자별'][d]['영수증별'][r]['실거래액'] = each.합계
                cnt_days['일자별'][d]['영수증별'][r]['세금'] = each.세
                cnt_days['일자별'][d]['영수증별'][r]['판매이익'] = (each.공급가 + each.면세)
                cnt_days['일자별'][d]['영수증별'][r]['테이블명'] = each.table_idx+1
                cnt_days['일자별'][d]['영수건수'] += 1

                for each2 in cashm:
                    cnt_days['일자별'][d]['영수증별'][r][each2] = 0

                for each1 in lst3:
                    if each1.판매i == r:
                        cash1 = each1.결제수단
                        cnt_days['일자별'][d]['영수증별'][r][cash1] += each1.합계

                for each3 in lst:
                    g = each3.품목i


                    if each3.판매i == r:
                        if g not in cnt_days['일자별'][d]['영수증별'][r]['상품']:
                            cnt_days['일자별'][d]['영수증별'][r]['상품'][g] = {  '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0,'영수건수' : 0 }

                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['총거래액'] += each3.단가
                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['총할인액'] += each3.할인
                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['실거래액'] += each3.합계
                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['세금'] += each3.세
                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['판매이익'] += (each3.공급가 + each3.면세)
                        cnt_days['일자별'][d]['영수증별'][r]['상품'][g]['영수건수'] += 1

            
        return c.jsonify(cnt_days)

    c.abort(404)


@app.route('/earnings/modal', methods=['GET', ])
def _earnings_modal():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

@app.route('/earnings/day1', methods=['GET', ])
def _earnings_day1():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

@app.route('/earnings/day2', methods=['GET', ])
def _earnings_day2():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day3', methods=['GET', ])
def _earnings_day3():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day4', methods=['GET', ])
def _earnings_day4():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day5', methods=['GET', ])
def _earnings_day5():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day6', methods=['GET', ])
def _earnings_day6():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day7', methods=['GET', ])
def _earnings_day7():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day8', methods=['GET', ])
def _earnings_day8():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day9', methods=['GET', ])
def _earnings_day9():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

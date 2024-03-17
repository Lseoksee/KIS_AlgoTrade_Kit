from pykis import *
from dotenv import dotenv_values

env_vars = dotenv_values('./test/info.env')

kis = PyKis(
    appkey=env_vars.get('appKey'),
    appsecret=env_vars.get('secretKey'),
    virtual_account=True,  # 가상 계좌 여부
)

# 계좌연결
account = kis.account(env_vars.get('bankAccount'))
# 잔고조회
balance = account.balance_all()
print(f'예수금: {balance.dnca_tot_amt:,}원 평가금: {balance.tot_evlu_amt:,} 손익: {balance.evlu_pfls_smtl_amt:,}원', flush=True)

stock = kis.market.stock('375500')
print(stock.mksc_shrn_iscd, stock.hts_kor_isnm)

# 매수주문


def customBuy():
    order = account.buy(
        # 종목 코드
        '000660',
        # 주문 수량
        qty=436,
        # 주문 단가
        unpr=89300,
    )

# 시장가매수주문


def marketBuy():
    order = account.buy(
        # 종목 코드
        '000660',
        # 주문 수량
        qty=436,
        # 주문 단가 (시장가 주문이므로 0)
        unpr=0,
        dvsn='시장가'
    )

# 매도주문


def customSell():
    order = account.sell(
        # 종목 코드
        '000660',
        # 주문 수량
        qty=436,
        # 주문 단가
        unpr=89300,
    )
# 시장가매도주문


def cancelSell():
    order = account.cancel(order)  # qty=None이면 전량


def cancelSell_num():
    order = account.cancel(KisStockOrderBase(
        # KRX주문조직번호
        '06010',
        # 주문번호
        '0001569157'
    ))

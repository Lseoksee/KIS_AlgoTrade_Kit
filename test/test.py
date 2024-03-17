from pykis import *
from dotenv import dotenv_values

env_vars = dotenv_values('info.env')

kis = PyKis(
    appkey=env_vars.get('appKey'),
    appsecret=env_vars.get('secretKey'),
    virtual_account=True,  # 가상 계좌 여부
)

# 계좌연결
account = kis.account(env_vars.get('secretKey'))
# 잔고조회
balance = account.balance_all()
print(f'예수금: {balance.dnca_tot_amt:,}원 평가금: {balance.tot_evlu_amt:,} 손익: {balance.evlu_pfls_smtl_amt:,}원', flush=True)

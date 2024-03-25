import sys
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

# 메시지 전송
sys.stdout.write('python worked done.\n')
sys.stdout.flush()

# Node.js로부터 메시지 받기
# for line in sys.stdin:
#    print('Node.js message :', line)
#   sys.stdout.flush()  # 버퍼 비우기

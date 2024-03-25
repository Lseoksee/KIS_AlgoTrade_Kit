from typing import Literal
import requests
import json
import Constant

class kisATkit:
    def __init__(self, type: Literal["실전", "모의"], appKey: str, appSecret: str, account: str, HTS_Id: str):
        """
        한국 투자증권 API 를 사용하기 위한 토큰 키 발급 및 기본정보를 입력합니다.\n
        토큰 재발급 처리는 만료 24분전에 자동으로 갱신되니 따로 처리하실 필요가 없습니다.

        Args:
            type ('실전', '모의'): 실전투자인지 모의 투자 인지
            appKey (str): 한국 투자증권에서 발급받은 appKey
            appSecret (str): 한국 투자증권에서 발급받은 appKey
            account (str):  계좌번호(뒤 2자리 포함 전체)
            HTS_Id (str): 한국투자증권 HTS ID
        """

        url = "/oauth2/tokenP"

        reqJson = {
            "grant_type": "client_credentials",
            "appkey": appKey,
            "appsecret": appSecret
        }

        req = requests.post(
            "{}{}".format(Constant.REAL_URL if type == "실전" else Constant.TEST_URL, url), json=reqJson)

        # 요청 오류시 예외 추가
        if (not req.ok):
            raise Exception(req.json())
        
        data = req.json()

        self.type = type
        self.appKey = appKey
        self.appSecret = appSecret
        self.account = account
        self.HTS_Id = HTS_Id
        self.accessToken = data["access_token"]
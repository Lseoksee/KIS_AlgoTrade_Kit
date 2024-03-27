from threading import Thread
from typing import Literal
import requests
import time
from kisATkit import Constant

class KisATkit:
    tokenUrl = "/oauth2/tokenP"
    
    def __init__(self, type: Literal["실전", "모의"], appKey: str, appSecret: str, account: str, HTS_Id: str):
        """
        한국 투자증권 API 를 사용하기 위한 토큰 키 발급 및 기본정보를 입력합니다.\n
        토큰 재발급 처리는 만료 27분전에 자동으로 갱신되니 따로 처리하실 필요가 없습니다.

        Args:
            type ('실전', '모의'): 실전투자인지 모의 투자 인지
            appKey (str): 한국 투자증권에서 발급받은 appKey
            appSecret (str): 한국 투자증권에서 발급받은 appKey
            account (str):  계좌번호(뒤 2자리 포함 전체)
            HTS_Id (str): 한국투자증권 HTS ID
        """

        reqJson = {
            "grant_type": "client_credentials",
            "appkey": appKey,
            "appsecret": appSecret
        }

        req = requests.post(
            "{}{}".format(Constant.REAL_URL if type == "실전" else Constant.TEST_URL, KisATkit.tokenUrl), json=reqJson)

        data = req.json()

        # 요청 오류시 예외 추가
        if (not req.ok):
            raise Exception(req.json())

        self.__type = type
        """모의투자, 실전 투자 여부"""
        self.__appKey = appKey
        """appKey"""
        self.__appSecret = appSecret
        """appSecret"""
        self.__account = account
        """계좌 번호"""
        self.__HTS_Id = HTS_Id
        """HTS 계정 아이디"""
        self.__tokenRes: dict = data
        """토큰 정보 딕셔너리"""

        # 토큰 관리 쓰레드 시작
        Thread(target=self.__refreshToken).start()
        time.sleep(1)

    # 토큰 재발급 함수
    def __refreshToken(self) -> None:
        while True:
            nextTime = self.__tokenRes["expires_in"] - 1000
            time.sleep(nextTime)
            url = KisATkit.tokenUrl

            reqJson = {
                "grant_type": "client_credentials",
                "appkey": self.__appKey,
                "appsecret": self.__appSecret
            }

            req = requests.post(
                "{}{}".format(Constant.REAL_URL if type == "실전" else Constant.TEST_URL, url), json=reqJson)

            data = req.json()

            # 요청 오류시 예외 추가
            if (not req.ok):
                raise Exception("토큰 재발급 실패: {}".format(data))

            self.__tokenRes = data

import sys
import os

#다른 폴더에 있는 모듈 불러오는 코드
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from kisATkit import KisATkit

# 한국투자증권 알고리즘 트레이딩용 라이브러리

한국투자증권 알고리즘 트레이딩 특화 라이브러리

## 개발 가이드

파이썬 버전: `3.12`

### 1. poetry 설치

> 참고 https://python-poetry.org/docs/#installing-with-the-official-installer

#### 리눅스

```
curl -sSL https://install.python-poetry.org | python3 -
```

#### pip (원도우등)

```
pip install poetry
```

`[유저디렉토리]\AppData\Roaming\Python\Python[버전]\Scripts` 에 환경변수 설정 해야 한다

### 2. poetry를 사용하여 패키지 설치 & 테스트

> 참고: [Poetry를-사용하여-가상환경-만들기](https://velog.io/@hj8853/Poetry%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0)

vs code에서 디버깅시 하단 인터프리터를 poetry거로 변경 후 디버깅 하면 된다

-   모든 패키지 종속성 설치

    ```
    poetry install
    ```

-   종속성에 패키지 추가

    ```
    poetry add [패키지]
    ```

-   현제 파일 실행
    ```
    poetry run python [파일경로]
    ```

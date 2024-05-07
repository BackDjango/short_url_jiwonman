# short_url_jiwonman

## 📎프로젝트 개요
- DRF로 간단한 단축 URL 챌린지
- 기능 단위에 초점을 맞춰 개발하고, 이슈 및 PR 생성
- 기한: 2024.05.07 ~ 2024.05.21 
    - 중간 점검: 14일 (1주차)
    - 최종 발표: 21일 (2주차)

## 👊 챌린지 진행 시 바라는 점
- 각자 가지고 있는 Initailize_Django 세팅 개선
- 나만의 단축 URL 간단 프로젝트를 통해 DRF 실력 향상
- 삽질일기 (블로그 포스팅 or 노션)

## ⚙ 구현 기능
- Auth
- 단축 URL
    - 생성
    - 삭제
    - 조회 (redirect)
    - 통계 (referer)
- 환경 변수 관리
    - 보안적 요소
- Logging 
- swagger
- black

## 🔎 구현 범위 상세 설명
- 긴 URL을 단축 URL로 변경
    - URL 생성 시 만료 옵션을 추가하면 해당 만료일시 이후의 요청에는 응답하지 않음 (삭제)
    - 만료 옵션이 있는 URL에 대해 재생성 요청을 하게 되는 경우 이전 옵션을 무시
    - 단축 URL 호출 시 긴 URL로 다이렉트
    - 만들어진 URL 뒤에 '+' 를 붙이면 통계 기능 제공 (API)
        - 일간 조회수 (최근 7일)
        - 전체 조회수
        - 전체 리퍼러 별 조회수
            - 만료 옵션이 있는 URL에 대해 재생성 요청을 하게 되는 경우 이전 옵션을 무시

## 📢 구현 조건
- 코드 컨벤션
    - PEP8
- Python 3.11
- Django 5.0.4
- djangorestframework 3.15.1
- CI (Jenkins or Github Action)
    - CI 에서는 빌드 및 모든 테스트가 통과 되어야 합니다. (컴파일 오류 확인)
    - CI 통과 후, Github Repository 통합
- CD (옵션 선택)
- ORM
- DB
    - 기본적으로 MySQL, RDBMS
    - 다른 DB 필요할 경우 추가
- 각 도메인(테이블)의 요소(필드)들은 자유
- 문서화 라이브러리 (swagger 등)
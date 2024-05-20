SPECTACULAR_SETTINGS = {
    "TITLE": "SHORT URL API Document",
    "DESCRIPTION": "SHORT URL API 문서입니다.",
    "CONTACT": {
        "name": "jiwonman",
        "url": "https://coddingjiwon.tistory.com",
        "email": "kusa1230@naver.com",
    },
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    "SWAGGER_UI_SETTINGS": {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  <- 여기 들어가면 어떤 옵션들이 더 있는지 알수있습니다.
        "dom_id": "#swagger-ui",  # required(default)
        "layout": "BaseLayout",  # required(default)
        "deepLinking": True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        "persistAuthorization": True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        "displayOperationId": True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        "filter": True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    # Optional: MUST contain "name", MAY contain URL
    "LICENSE": {
        "name": "MIT License",
        "url": "https://github.com/BackDjango/short_url_jiwonman/blob/master/LICENSE",
    },
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,  # OAS3 Meta정보 API를 비노출 처리합니다.
    # available SwaggerUI versions: https://github.com/swagger-api/swagger-ui/releases
    "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",  # default
}

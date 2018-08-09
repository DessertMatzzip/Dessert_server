DessertMatzzip_Server
===========

### API 문서 : [Google docs로 이동](https://docs.google.com/document/d/1K3fzN_OUAdnAGoy0OsK1ejsdH4eCdTpa25JWxrYZ6W8/edit)

# file structure

- dessertServer : django project

- login : django app for kakaotalk, facebook login

- screenshots : 진행상황을 표시하기 위한 이미지 저장 폴더

# 진행상황
## 2018.07.26
> - django REST Framework 설치 및 테스트 케이스 동작확인
> > ![스크린샷](./screenshots/2018-07-26.png)

## 2018.07.31
> - facebook login을 위한 API문서 생산
> > ![스크린샷](./screenshots/2018-07-31.png)

## 2018.08.02
> - 외부 ini파일을 통한 DB setting을 gitignore
> - django project models class --> DB 구축 테스트 확인
> > ![스크린샷](./screenshots/2018-08-02.png)

## 2018.08.09
> - 로그인 api 완성 (카카오톡, 페이스북 accesstoken->db확인)
> - accesstoken이 db에 있으면 signin_req / 없으면 signup_req 반환
> > ![스크린샷](./screenshots/2018-08-09.png)
-----------------

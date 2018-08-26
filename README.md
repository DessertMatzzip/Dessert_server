DessertMatzzip_Server

### API 문서 : [Google docs로 이동](https://docs.google.com/document/d/1K3fzN_OUAdnAGoy0OsK1ejsdH4eCdTpa25JWxrYZ6W8/edit)

-----------------

# file structure

- dessertServer : django project

- login : 회원 로그인을 위한 앱(페이스북, 카카오톡 연동로그인 + 자체로그인)

- join : 회원가입과 회원정보 수정을 위한 앱

- screenshots : 진행상황을 표시하기 위한 이미지 저장 폴더

-----------------

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
> - 로그인 api 문서 및 구현완료 (카카오톡, 페이스북 accesstoken->db확인)
> - accesstoken이 db에 있으면 signin_req / 없으면 signup_req 반환
> > ![스크린샷](./screenshots/2018-08-09.png)
> - 앱에서 카카오톡 로그인 url로 post 테스트 확인
> > ![스크린샷](./screenshots/2018-08-09-2.png)

## 2018.08.13
> - 회원가입 api 문서 작성중
> > ![스크린샷](./screenshots/2018-08-13.png)

## 2018.08.14
> - 회원가입, 회원정보수정 api 문서 완료
> - 회원가입, 정보수정을 위한 app 'join' 생성
> > ![스크린샷](./screenshots/2018-08-14.png)
> - app 'join'에서 app 'login'의 User table 접근 및 값 INSERT 확인
> > ![스크린샷](./screenshots/2018-08-14-2.png)

## 2018.08.17
> - join앱 내 소셜, 자체 회원가입 함수 구현
> - 회원정보 수정 함수 구현(DB갱신)
> > ![스크린샷](./screenshots/2018-08-17.png)

## 2018.08.18
> - 스토리보드 기반으로 기능 추려내기
> - 추려낸 기능 -> api 문서 작성

-----------------

# 미결사항
- 잘못된 매개변수(실패 시) : error occured 출력하는 것
- DB에 입력된 토큰을 소유하여도 signin 미출력
- get 출력
- 스토리보드 기능추려내기

-----------------

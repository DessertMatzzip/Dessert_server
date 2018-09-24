#  DssertMatzzip_Server
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

## 2018.08.27
> - 추려낸 기능 -> api문서 구현
> - 가게 데이터 파트, 랭킹파트, 소셜기능 파트 api문서 틀 구현 및 urls 경로 설정

## 2018.08.29
> - api문서에 기반하여 필요한 DB 테이블 구축 및 ERD 구성
> > ![스크린샷](./screenshots/2018-08-29.png)

## 2018.08.30
> - api 문서 구현중..
> - api 문서에 기반하여 서버 구축중..

## 2018.09.02~09.10
> - database model 필드 추가(스토어 리뷰, 유저 소개란)
> - api 문서 작성완료 (상단 구글독스 링크로 확인가능)
> > ![스크린샷](./screenshots/2018-09-10.png)

## 2018.09.21
> - 

-----------------

# 미결사항
- 잘못된 매개변수(실패 시) : error occured 출력하는 것(서비스구현 후 추가)

-----------------

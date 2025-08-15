from app.models.chat import User
from datetime import datetime

usersdb={
    "2171001": User(
  user_id= "2171001",
  name= "이학사",
  student_number=2171001,
  gender= "F",
  grade= 4,
  school= "이화여자대학교",
  income_level=5,
  major= "컴퓨터공학전공",
  id=1
    ),

   "2303029": User(
 user_id= "2303029",
 name="박장학",
 student_number= 2303029,
 gender= "F",
 grade= 2,
 school="이화여자대학교",
 income_level=2,
 major= "사학과",
 id=2
   ),

   "2501001": User (
  user_id="2501001",
  name="최식단",
  student_number= 2501001,
  gender= "F",
  grade= 1,
  school= "이화여자대학교",
  income_level= 6,
  major="경영학과",
  id=3
   )
}

#사용자 조회 함수
def get_user_by_id(user_id: str) :
    return usersdb.get(user_id)
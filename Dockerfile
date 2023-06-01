FROM openjdk:17-jdk
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]

# FROM : Docker Base Image (기반이 되는 이미지, <이미지 이름>:<태그> 형식으로 설정)
# ARG : 컨테이너 내에서 사용할 수 있는 변수를 지정할 수 있다.
# COPY : 위에 선언했던 JAR_FILE 변수를 컨테이너의 app.jar로 복사한다.
# ENTRYPOINT : 컨테이너가 시작되었을 때 스크립트 실행

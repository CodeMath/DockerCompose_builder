# docker-compose.yml builder App
[![Django CI & Pytest](https://github.com/CodeMath/DockerCompose_builder/actions/workflows/Pytest_build.yml/badge.svg?branch=main)](https://github.com/CodeMath/DockerCompose_builder/actions/workflows/Pytest_build.yml)
<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/CodeMath/DockerCompose_builder/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-99%25-brightgreen.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>base</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/CodeMath/DockerCompose_builder/blob/main/base/views.py">views.py</a></td><td>8</td><td>1</td><td>88%</td><td><a href="https://github.com/CodeMath/DockerCompose_builder/blob/main/base/views.py#L11">11</a></td></tr><tr><td colspan="5"><b>builder</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/CodeMath/DockerCompose_builder/blob/main/builder/factories.py">factories.py</a></td><td>34</td><td>1</td><td>97%</td><td><a href="https://github.com/CodeMath/DockerCompose_builder/blob/main/builder/factories.py#L114">114</a></td></tr><tr><td><b>TOTAL</b></td><td><b>152</b></td><td><b>2</b></td><td><b>99%</b></td><td>&nbsp;</td></tr></tbody></table></details><!-- Pytest Coverage Comment:End -->



> 도커 컴포즈(docker-compse.yml) 및 도커 파일(Dockerfile) 빌더
```
# python^3.9 && django==4.2.5
pip isntall -r requirements.txt
```

### 도커 컴포즈 작성을 CloudFormation 스타일로~

![preview](https://github.com/CodeMath/DockerCompose_builder/assets/12072529/81e17c76-1896-4587-95cd-42850383cf84)

물론 `CloudFormation` 보다는 쉽게 작성할 수 있도록 기본 코드를 제공을 통해 보다 빠르게 작성이 가능 하게 하는것이 목적이다.

개인적으로는 해당 `APP` 이미지를 클릭한 다음 기본 셋팅을 한 뒤, 세부 설정을 추가로 클릭 만으로 쉽게 셋팅 할 수 있게(?) 하는 것이 최종 목표이다.

물론 docker API 를 통해 실제 `PULL` 까지 지원해보려한다.

* * *

### 세부사항

* `CodeMirror`  사용
* `admin` 데이터 추가 시, `yaml` 코드 작성
```yaml
django:
  build:
    context: .
    dockerfile: Dockerfile
    command:
      - ["python", "manage.py", "runserver"]
    ports:
      - "8000:8000"
    expose:
      - "8000"
    restart: always
```
* 추후 [docker library](https://github.com/docker-library/docs) 에서 데이터 크롤링 예정

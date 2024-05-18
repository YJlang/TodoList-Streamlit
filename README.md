```markdown
# Weather Dashboard with Streamlit

이 프로젝트는 Streamlit을 사용하여 구현된 날씨 정보 대시보드 애플리케이션입니다. 한국의 주요 도시들의 현재 날씨와 예보를 지도에 표시하고, 사용자가 직관적인 인터페이스를 통해 정보를 확인할 수 있습니다.

## 주요 기능

- **현재 날씨 정보 표시**: 전국 주요 도시의 현재 날씨를 지도에 마커로 표시합니다. 각 마커에는 도시 이름, 날씨 상태, 온도가 팝업으로 표시됩니다.
- **날씨 예보 제공**: 주요 도시의 날씨 예보를 표 형태로 제공합니다.
- **실시간 시계**: 사이드바에 현재 날짜와 시간을 초 단위로 실시간으로 업데이트하여 표시합니다.

## 시작하기

이 섹션에서는 프로젝트를 로컬에서 실행하는 방법을 설명합니다.

### 전제 조건

프로젝트를 실행하기 위해 필요한 것들:

- Python 3.6 이상
- 필요한 Python 라이브러리: streamlit, pandas, folium, Pillow, requests, python-dotenv

### 설치 방법

1. 이 저장소를 클론하거나 다운로드합니다.
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```
2. 필요한 Python 패키지들을 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
3. Streamlit 애플리케이션을 실행합니다.
   ```bash
   streamlit run main.py
   ```

## 사용 방법

애플리케이션을 시작한 후, 웹 브라우저에서 [http://localhost:8501](http://localhost:8501)을 열어 프로젝트 대시보드를 볼 수 있습니다.

- 사이드바에서 현재 날씨, 예보, 소개 중 하나를 선택하여 해당 정보를 확인합니다.
- 현재 날씨 페이지에서는 지도 위의 마커를 클릭하여 도시의 날씨 상세 정보를 확인할 수 있습니다.
- 예보 페이지에서는 다가오는 날짜의 날씨 예보를 표로 확인할 수 있습니다.

## 구성 파일

- `main.py`: 애플리케이션의 메인 스크립트.
- `city_coordinates.csv`: 대시보드에 사용되는 도시의 위도와 경도 정보.
- `.env`: API 키와 같은 환경 변수를 설정하는 파일.
- `requirements.txt`: 필요한 Python 라이브러리 목록.

## 개발자 정보

- 이름: [윤준하]
- 이메일: [sean111400@naver.com]

## 프로젝트 진행 간 어려웠던 점

- streamlit cloud 연동 과정에서 requirement.txt에 사용됐던 라이브러리들을 알려줘야 했는데 헤맸다. 이 과정에서 streamlit의 작동 원리를 심도깊게 알게됐다.
- streamlit의 기능 중 사이드 바에 시간을 노출시키는 과정에서 한계가 있었다.(실시간 동적 확인 불가능)

## 라이선스

이 프로젝트는 MIT license 하에 제공됩니다.
```
# koreatech_chatbots_huggingface

## 프로젝트 개요

- FastAPI 기반의 다양한 예제 및 AI 챗봇, 번역, 요약, RAG 등 기능을 실습하는 프로젝트입니다.
- Hugging Face Transformers, Sentence Transformers, FastAPI, Jinja2 템플릿, PostgreSQL(pgvector) 등 다양한 라이브러리 활용.

---

## 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. FastAPI 서버 실행

예시(기본 예제 실행):

```bash
uvicorn app.exam1:app --reload --host 0.0.0.0 --port 8000
```

- 각 예제별로 `app.examN:app` 형식으로 실행 (`exam1.py`, `exam2.py`, ...)

### 3. 주요 예제 실행 예시

- **exam1.py**:  
  ```bash
  uvicorn app.exam1:app --reload
  ```
  - `/` 접속 시 "안녕? FastAPI!! ^^" 반환

- **exam2.py**:  
  ```bash
  uvicorn app.exam2:app --reload
  ```
  - `/test1`, `/test2`, `/test3`, `/test4` 등 다양한 응답 예시

- **exam7.py, exam8.py**:  
  - Jinja2 템플릿을 활용한 HTML 렌더링 예제

- **exam25.py**:  
  - 텍스트 파일 업로드 후 Hugging Face Summarization 모델로 요약 결과 반환
  - `/` 접속 후 파일 업로드

- **exam26.py**:  
  - 한-영 번역 API 제공 (Helsinki-NLP/opus-mt-ko-en)
  - `/translate` POST로 번역, `/`에서 번역 폼 제공

- **hotelrag.py**:  
  - RAG(Retrieval-Augmented Generation) 및 임베딩, 텍스트 생성 모델 로드 예제

---

## 폴더/파일 역할

- `app/` : FastAPI 예제 및 AI 기능 구현 파일
- `static/` : 정적 파일(css, 이미지 등)
- `templates/` : Jinja2 HTML 템플릿
- `requirements.txt` : 의존성 목록
- `README.md` : 프로젝트 설명

## codes 폴더 구성 및 역할

- **codes/data.txt**  
  - 호텔 서비스 안내, 정책, 고객 응대 등 실제 호텔 운영에 필요한 주요 문서 예시 데이터

- **codes/hf_exam.ipynb**  
  - Hugging Face 사전학습 모델 활용법, 파이프라인 실습, 감정분석/번역/요약 등 다양한 AI 실습 노트북

- **codes/exam1.html ~ exam5.html**  
  - Transformers.js, Hugging Face API를 활용한 웹 기반 AI 데모 예제  
    - `exam1.html`: 텍스트 분류(감정분석)  
    - `exam2.html`: 한영 번역  
    - `exam3.html`: 마스크 언어 모델(Masked LM)  
    - `exam4.html`: 이미지 업로드 기반 객체 탐지(Object Detection)  
    - `exam5.html`: 텍스트 요약(Summarization)  

- **codes/asset/**  
  - 웹 예제에서 사용하는 JS, CSS 등 정적 리소스  
    - `index.js`: 객체 탐지 등 JS 로직  
    - `styles4.css`, `styles5.css`: 각 예제별 스타일

- **codes/images/**  
  - 웹 예제에서 사용하는 이미지 리소스

- **codes/output/**  
  - 예제 실행 결과(생성 이미지 등) 저장 폴더

---

## 기타

- 일부 예제는 PostgreSQL, pgvector, 외부 모델 다운로드가 필요할 수 있습니다.
- 최신 torch(2.6+) 필요:  
  모델 로딩 오류 발생 시 `pip install --upgrade torch` 참고

---

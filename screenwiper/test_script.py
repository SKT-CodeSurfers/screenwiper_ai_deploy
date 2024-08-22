import requests

# 서버 URL
url = 'http://127.0.0.1:5001/analyze_image'

# 테스트 이미지 URL
image_url = 'https://screen-s3-bucket.s3.ap-northeast-2.amazonaws.com/1724350887204_test.png'

# 요청 보내기
response = requests.post(url, json={'imageUrl': image_url})

# 응답 처리
if response.status_code == 200:
    result = response.json()
    
    # 응답의 텍스트 결과와 날짜 추출
    text_results = result.get('summary', '')  # 'summary' 또는 'text_results'로 변경될 수 있음
    extracted_dates = result.get('list', [])  # 'list'는 카테고리 2의 경우…
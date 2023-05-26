import os
import openai

# GPT-3 API를 사용하여 질문에 대한 답변 받기
def get_gpt_answer(question):
    openai.api_key = os.getenv('GPT-KEY')

    # GPT-3 API 요청
    response = openai.Completion.create(
        engine='text-davinci-003',  # 사용할 GPT 엔진 선택
        prompt=question,
        max_tokens=1000,  # 생성된 답변의 최대 토큰 수
        n=1,  # 생성할 답변의 수
        stop=None,  # 생성을 중단할 토큰
        temperature=0.6  # 낮은 값일수록 보수적인 답변을 생성
    )

    # 답변 추출
    answer = response.choices[0].text.strip()

    return answer
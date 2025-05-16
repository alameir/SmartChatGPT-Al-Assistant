
# SmartChatGPT-AI-Assistant
import streamlit as st
import openai

# إعداد واجهة المستخدم
st.set_page_config(page_title="Smart ChatGPT Assistant", layout="wide")
st.title("🤖 Smart ChatGPT AI Assistant")

# إدخال مفتاح OpenAI
openai_api_key = st.text_input("أدخل مفتاح OpenAI API الخاص بك", type="password")

# اختيار نبرة الرد
tone = st.selectbox("اختر نبرة الرد:", ["رسمية", "ودية", "تقنية", "محايدة"])

# رسالة المستخدم
user_input = st.text_area("اكتب رسالتك للمساعد الذكي:")

# زر إرسال
if st.button("إرسال") and openai_api_key and user_input:
    # إعدادات النبرة
    tone_instructions = {
        "رسمية": "أجب بشكل رسمي واحترافي.",
        "ودية": "أجب بطريقة ودية ومريحة.",
        "تقنية": "أجب بمصطلحات تقنية دقيقة.",
        "محايدة": "أجب بطريقة محايدة ومباشرة."
    }

    # إعداد الطلب
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": tone_instructions[tone]},
                {"role": "user", "content": user_input}
            ],
            api_key=openai_api_key
        )
        reply = response['choices'][0]['message']['content']
        st.markdown(f"### رد المساعد:\n{reply}")
    except Exception as e:
        st.error(f"حدث خطأ: {str(e)}")

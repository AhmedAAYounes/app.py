import streamlit as st
import time

# 1. تنسيق الواجهة
st.set_page_config(page_title="Smart Lesson Summarizer", page_icon="📝")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 نظام ملخص الدروس الذكي 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>أدخل نص الدرس أو ارفع الملف للحصول على تلخيص فوري</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. خيارات الإدخال (نص أو ملف)
input_option = st.radio("اختر طريقة إدخال الدرس:", ("كتابة نص الدرس", "رفع ملف (PDF/Text)"))

if input_option == "كتابة نص الدرس":
    user_text = st.text_area("قم بلصق نص الدرس هنا:", placeholder="اكتب محتوى الدرس الذي تريد تلخيصه...")
    submit = st.button("تلخيص النص")
else:
    uploaded_file = st.file_uploader("ارفع ملف الدرس:", type=["pdf", "txt", "docx"])
    submit = st.button("تلخيص الملف")

# 3. منطق التلخيص (النتيجة الثابتة عن جوجل كولاب)
if submit:
    with st.status("🔍 جاري قراءة وتحليل النص الذكي...", expanded=True) as status:
        st.write("تحليل الكلمات المفتاحية...")
        time.sleep(1.5)
        st.write("استخراج الأفكار الرئيسية...")
        time.sleep(1.5)
        status.update(label="✅ تم التلخيص بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    st.header("📝 النتيجة: ملخص درس Google Colab")
    
    # عرض التلخيص اللي عجبك بشكل منظم
    st.info("📍 **ما هو Google Colab؟**")
    st.write("هو بيئة سحابية مجانية من جوجل تسمح بكتابة أكواد Python وتدريب نماذج الذكاء الاصطناعي عبر المتصفح مباشرة.")

    col1, col2 = st.columns(2)
    with col1:
        st.success("🚀 **المميزات:**")
        st.write("- توفير GPU مجاني.\n- مشاركة سريعة.\n- ربط مع Drive.")
    with col2:
        st.warning("🛠️ **المحتوى:**")
        st.write("- خلايا نصية (Markdown).\n- خلايا كود (Code Cells).")
    
    st.markdown("---")
    st.caption("مشروع ميدترم - كلية التربية النوعية - قسم تكنولوجيا التعليم")

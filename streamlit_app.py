import streamlit as st

st.set_page_config(page_title="دليل طبي - مساعد تشخيص ذكي", page_icon="🧠")

st.title("🧠 دليل طبي - مساعد تشخيص ذكي")
st.write("أدخل الأعراض وسأقوم بتحليلها مبدئيًا 👨‍⚕️")

symptoms = st.text_area("اكتب الأعراض بالتفصيل:")

if st.button("تحليل مبدئي"):
    st.write("تحليل مبدئي بناء على الأعراض:")
    if "حمى" in symptoms or "حرارة" in symptoms:
        st.warning("قد يكون هناك التهاب حاد. يُنصح بعمل تحاليل دم كاملة.")
    elif "صداع" in symptoms:
        st.info("الصداع قد يشير لعدة أسباب مثل التوتر أو الأنيميا أو مشاكل عصبية.")
    elif "ألم بطن" in symptoms or "مغص" in symptoms:
        st.warning("قد يكون هناك اضطراب بالجهاز الهضمي. راجع طبيب باطني.")
    elif "ضيق تنفس" in symptoms or "نهجان" in symptoms:
        st.warning("يُنصح بعمل تقييم للقلب والرئة.")
    else:
        st.write("الأعراض تحتاج تقييم طبي شامل من طبيب مختص.")

from transformers import pipeline
import streamlit as st
prompt="I have a problem with my iphone that needs to be resolved asap!!"
classifier = pipeline(model="facebook/bart-large-mnli")

prom=st.text_input("write")

if prom:
    s=classifier(
        prom,
        candidate_labels=["urgent", "not urgent", "phone", "tablet", "computer"],
    )
    print(s)
    st.write(s)

# s=classifier(
#         prompt,
#         candidate_labels=["urgent", "not urgent", "phone", "tablet", "computer"],
#     )
# print(s)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_normalyzer import normalize_text


def similarity_score(resume_text: str, job_text:str) -> float:
    resume_clean = normalize_text(resume_text)
    job_clean = normalize_text(job_text)



    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])


    score = cosine_similarity(vectors[0], vectors[1])[0][0]


    return round(score * 100, 2)

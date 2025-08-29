from PyPDF2 import PdfReader
import spacy
import string

nlp = spacy.load("en_core_web_sm")

TECH_TERMS = [
    "Python","Java","JavaScript","TypeScript","PHP","C#","Ruby","Go","Rust","Node.js",
    "Django","Flask","Spring","Express.js","React","Vue.js","Angular","Svelte",
    "MySQL","PostgreSQL","MongoDB","SQLite","Redis","OracleDB","Firebase",
    "Docker","Kubernetes","Jenkins","GitHub Actions","GitLab CI","CircleCI","TravisCI","CI/CD","AWS","Azure","GCP","Terraform",
    "Git","GitHub","GitLab","Bitbucket","SVN",
    "REST","GraphQL","API","Agile","Scrum","TDD","BDD","Unit Testing","Integration Testing","Webpack","Babel","npm","Yarn",
    "HTML","CSS","SASS","Bootstrap","Tailwind","Material UI","Figma","Adobe XD"
]

def normalize_text(text: str) -> str:
    doc = nlp(text)
    tokens = []
    for token in doc:
        # Preserve technical keywords as-is
        if token.text in TECH_TERMS:
            tokens.append(token.text.lower())
        # Keep your original lemmatization + stopword + punctuation removal
        elif not token.is_stop and token.text not in string.punctuation:
            tokens.append(token.lemma_.lower())
    return " ".join(tokens)




#print(page.extract_text())
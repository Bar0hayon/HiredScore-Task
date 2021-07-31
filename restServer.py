from flask import Flask
from matchingModel import MatchingModel
from dbWrapper import DBWrapper
import modelSerializer

model = modelSerializer.load_model("model.pkl")
app = Flask(__name__)
DB = DBWrapper(dbname="hiredscore", user="postgres")

@app.route("/bestmatch/<job_title>")
def get_best_match(job_title):
    candidates = DB.get_candidates()
    best_match = {'candidate_title': None, 'score': -1}
    for candidate in candidates:
        score = model.get_score((job_title, candidate))
        if score >= best_match['score']:
            best_match['candidate_title'] = candidate
            best_match['score'] = score
    if best_match['candidate_title']:
        return best_match['candidate_title']
    else:
        return "No match was found!"

@app.route("/score/job=<job_title>&candidate=<candidate_title>")
def get_matching_score(job_title, candidate_title):
    return f"{model.get_score((job_title, candidate_title))}"
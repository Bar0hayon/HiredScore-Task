class MatchingModel:
    def fit(self, X, y):
        pass

    def predict(self, X):
        return list(map(self.get_score, X))

    def get_score(self, candidate_and_job):
        candidate, job = candidate_and_job
        return int(candidate == job)
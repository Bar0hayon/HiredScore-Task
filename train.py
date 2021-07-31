from matchingModel import MatchingModel
import modelSerializer
import sys

def main(model_path):
    model = MatchingModel()
    model.fit(None, None)
    modelSerializer.save_model(model, model_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "model.pkl"
    main(path)
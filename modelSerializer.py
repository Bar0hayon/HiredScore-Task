import pickle

def save_model(model, model_path):
    model_file = open(model_path, 'wb')
    pickle.dump(model, model_file)
    model_file.close()

def load_model(model_path):
    model_file = open(model_path, 'rb')
    model = pickle.load(model_file)
    model_file.close()
    return model
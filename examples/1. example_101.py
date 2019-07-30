import datetime as dt
from rasa.nlu.model import Interpreter
from rasa.cli.utils import get_validated_path
from rasa.constants import DEFAULT_MODELS_PATH
from rasa.model import get_model, get_model_subdirectories

model = "models"
model = get_validated_path(model, "model", DEFAULT_MODELS_PATH)
model_path = get_model(model)
_, nlu_model = get_model_subdirectories(model_path)
interpreter = Interpreter.load(nlu_model)

message = "哈哈"
num_iter = 1000

start = dt.datetime.now()

for _ in range(num_iter):
    result = interpreter.parse(message)

print(result)
print("\n{0:4d} runs elapsed: {1}".format(num_iter, dt.datetime.now() - start))
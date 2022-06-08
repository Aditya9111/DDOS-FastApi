
# 1. Library imports
import uvicorn
from fastapi import FastAPI
from DDOS import DDOS
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("DDOS_stacked_classifier.pickle", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000


# @app.get('/')
# def index():
#     return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


@app.post('/predict')
def predict_ddos(data: DDOS):
    data = data.dict()
    Destination_Port = data['Destination_Port']
    Total_Length_of_Fwd_Packets = data['Total_Length_of_Fwd_Packets']
    Bwd_Packet_Length_Std = data['Bwd_Packet_Length_Std']
    Flow_IAT_Min = data['Flow_IAT_Min']
    Fwd_IAT_Total = data['Fwd_IAT_Total']
    Bwd_Packets = data['Bwd_Packets']
    Init_Win_bytes_forward = data['Init_Win_bytes_forward']
    Init_Win_bytes_backward = data['Init_Win_bytes_backward']

    prediction = classifier.predict(
        [[Destination_Port, Total_Length_of_Fwd_Packets, Bwd_Packet_Length_Std, Flow_IAT_Min, Fwd_IAT_Total, Bwd_Packets, Init_Win_bytes_forward, Init_Win_bytes_backward]])
    if(prediction == ['BENIGN']):
        prediction = "BENIGN"
    else:
        prediction = "DDOS"
    return {
        'prediction': prediction
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload

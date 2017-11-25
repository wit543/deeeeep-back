from flask import Flask, jsonify
from keras.models import load_model
model = load_model('rain1.model')

import numpy as np

num_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def predict(lat,lon):
  result = []
  if lat and lon:
    for month in [8,9]:
      for  i  in range(1,num_day_in_month[month]+1):
        for h in range(0,24):
          res = np.array([[[9,i,h,lat,lon]]])
          result.append(
            {
              "start":"2017-"+'{:02d}'.format(month)+"-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long),
              "end":"2017-"+'{:02d}'.format(month)+"-"+'{:02d}'.format(i+1)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long),
              "predict":res
            }
          )
  return result



app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_prediction():
    return jsonify(predict(request.args.get('lat'),request.args.get('long')))

if __name__ == '__main__':
    app.run(debug=True)
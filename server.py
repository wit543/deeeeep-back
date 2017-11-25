from flask import Flask, jsonify, request, abort
import tensorflow as tf
from keras.models import load_model
import sys
model = load_model('rain1.model')
graph = tf.get_default_graph()
import numpy as np
from flask_cors import CORS


if 'session' in locals() and session is not None:
    print('Close interactive session')
    session.close()

num_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def predict(lat,lon):
  result = []
  if lat and lon:
    for month in [8,9]:
      for  i  in range(1,num_day_in_month[month]+1):
        for h in range(0,24):
          with graph.as_default():
            res = np.array([[[month,i,h,lat,lon]]])
            print(res, file=sys.stderr)
            res_a = model.predict(res)
            print('{:0.1f}'.format(abs(res_a[0][0])), file=sys.stderr)
            result.append(
              {
                "start":"2017-"+'{:02d}'.format(month)+"-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00",
                "end":"2017-"+'{:02d}'.format(month)+"-"+'{:02d}'.format(i+1)+" "+'{:02d}'.format(h)+":00:00",
                "predict":'{:0.1f}'.format(abs(res_a[0][0]))
              }
            )
  return result



app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_prediction():
  if not request.args.get('lat') and not request.args.get('long'):
    abort(400)
  return jsonify(predict(float(request.args.get('lat')),float(request.args.get('long'))))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5050)
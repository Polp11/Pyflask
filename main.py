from flask import Flask , render_template
import io
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
  try:
    import matplotlib.pyplot as plt
    return 'fine pyplot'
      
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err
  
  y = [1,3]
  x = [0,2]
  plt.plot(x,y)
  #a=matplotlib.pyplot.plot(x,y)
  #return a
  try:
    return str(y)
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err

if __name__ == '__main__':
  app.debug = True
  app.run()

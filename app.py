import whatever-lib

def pre_a():

def post_a():

def preprocessing():
  pre_a()
  preprocessing lines

def model_loading():
  model loading lines

def inference():
  inference lines

def postprocessting():
  post_a()
  postprocessing lines

if __name__ == "__main__":
  preprocessing()
  model_loading()
  inference()
  postprocessing()

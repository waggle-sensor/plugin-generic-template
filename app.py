import whatever-lib

def pre_a():

def post_a():

def model_loading():
  model loading lines

def get_input():
  get input lines

def preprocessing():
  pre_a()
  preprocessing lines

def inference():
  inference lines

def postprocessting():
  post_a()
  postprocessing lines

if __name__ == "__main__":
  my_plugin = Plugin(app_name=”my_edge_app”)

  my_plugin.add_codeblock(model_loading)
  my_plugin.add_codeblock(get_input)
  my_plugin.add_codeblock(preprocessing)
  my_plugin.add_codeblock(inference)
  my_plugin.add_codeblock(postprocessing)

  my_plugin.run()

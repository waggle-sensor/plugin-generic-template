From waggle.plugin import Plugin
From waggle.data.vision import Camera

import libraries

def get_input():
    # get an image from given camera stream
    sample = Camera(args.stream).snapshot()
    # preprocessing the sample if needed
    normalized = normalize(sample.data, args.nomalization_factor)
    plugin.put(“image”, normalized)


def pre_a():

def post_a():

def func_argparse(args):
    …
    Plugin.args = args_result


def model_loading():
    model loading lines

def get_input():
    # get an image from given camera stream
    sample = Camera(args.stream).snapshot()
    # preprocessing the sample if needed
    normalized = normalize(sample.data, args.nomalization_factor)
    plugin.put(“image”, normalized)

def preprocessing():
    pre_a()
    preprocessing lines

def inference():
    # get sample from the previous code block
    image = plugin.get(“image”)
    model = plugin.get(“model”)
    # do inferencing
    output = model.infer(image)
    # cache the inference output
    plugin.put(“output”, output)


def postprocessting():
    # get inference result from the previous code block
    result = plugin.get(“output”)
    post_a(args)
    # postprocessing the output if needed
    top_classification = argmax(result)
    plugin.publish(“myresult”, top_classification)


if __name__ == "__main__":
    my_plugin = Plugin(app_name=”my_edge_app”)

    my_plugin.parse_args(func_argparse)

    my_plugin.add_codeblock(model_loading)
    my_plugin.add_codeblock(get_input)
    my_plugin.add_codeblock(preprocessing)
    my_plugin.add_codeblock(inference)
    my_plugin.add_codeblock(postprocessing)

    my_plugin.run()

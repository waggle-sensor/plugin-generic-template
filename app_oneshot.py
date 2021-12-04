From waggle.plugin import Plugin
From waggle.data.vision import Camera

import libraries

def pre_a(args):

def post_a(args):

def model_loading(args):
    model loading lines

def get_input(args):
    # get an image from given camera stream
    sample = Camera(args.stream).snapshot()
    # preprocessing the sample if needed
    normalized = normalize(sample.data, args.nomalization_factor)
    return normalized

def preprocessing(args):
    pre_a()
    preprocessing lines

def inference(args):
    # get sample from the previous code block
    image = plugin.get(“image”)
    model = plugin.get(“model”)
    # do inferencing
    output = model.infer(image)
    # cache the inference output
    return output


def postprocessting(args):
    # get inference result from the previous code block
    result = plugin.get(“output”)
    post_a(args)
    # postprocessing the output if needed
    top_classification = argmax(result)
    return top_classification


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(...)
    run(parser.parse_args())

    values = model_loading(args)
    values = get_input(args)
    values = preprocessing(args)
    values = inference(args)
    postprocessing(args)


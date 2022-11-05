import View, Model

def start():
    data = View.InputData()
    Model.set_math(data)
    Model.set_result(data)
    result = Model.get_result()
    View.outputResult(result)
from caffe2.python import workspace
from caffe2.python.onnx.backend import Caffe2Backend as c2
from onnx import ModelProto
import numpy as np
from caffe2.python import core,workspace,model_helper,brew,optimizer

#workspace.GlobalInit(["caffe2", "--caffe2_log_level=-2"])


class Model:
    def __init__(self):
        self.input_size = 100
        self.predictor = None

        self.item = np.zeros(self.input_size)
        self.item = self.item.reshape(1, -1).astype(np.int64)
        self.lstmnet_path = 'lstmnet.onnx'
        self.load_model()

    def load_model(self):
        try:
            predictor = self.create_caffe2_predictor(self.lstmnet_path)

        except Exception as e:
            print('Error while loading model: {}'.format(e))
            return

        self.predictor = predictor
        print('Model loaded!')


    @staticmethod
    def create_caffe2_predictor(onnx_file_path):
        with open(onnx_file_path, 'rb') as onnx_model:
            onnx_model_proto = ModelProto()
            onnx_model_proto.ParseFromString(onnx_model.read())
            init_net, predict_net = c2.onnx_graph_to_caffe2_net(onnx_model_proto)
            predictor = workspace.Predictor(init_net, predict_net)
        return predictor


    def predict(self):
        r = self.predictor.run({'0': self.item})

        return {'scores': [1]}

model = Model()

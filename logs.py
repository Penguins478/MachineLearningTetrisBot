from keras.callbacks import TensorBoard
# from tensorflow.summary import FileWriter
# from tensorflow.python.summary.writer.writer import FileWriter
# from tensorboardX import FileWriter


class CustomTensorBoard(TensorBoard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.writer = FileWriter(self.log_dir)

    def set_model(self, model):
        pass

    def log(self, step, **stats):
        # self._write_logs(stats, step)
        # just open a file and write the score each epoch
        print()

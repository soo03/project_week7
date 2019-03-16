import tensorflow as tf


class Second:

    def __init__(self):
        pass    # 아래 메소드에서 지정할 값이 공유되는 게 있으면 여기서 정의, 없으면 그대로 놔둠

    @staticmethod
    def execute():
        sess = tf.Session()
        saver = tf.train.import_meta_graph('saved/model-1000.meta')  # 아까 first파일 실행 후 생긴 메타파일 불러오기
        saver.restore(sess, tf.train.latest_checkpoint('./saved/'))
        graph = tf.get_default_graph()
        w1 = graph.get_tensor_by_name("w1:0")  # first파일에 만들어놓은 w1, w2 변수를 초기화함
        w2 = graph.get_tensor_by_name("w2:0")
        feed_dict = {w1: 13.0, w2: 17.0}        # 새로운 값을 줌
        op_to_restore = graph.get_tensor_by_name("op_to_restore:0") # first파일에 만들어놓은 op_to_restore 변수

        print(sess.run(op_to_restore, feed_dict))

        

    
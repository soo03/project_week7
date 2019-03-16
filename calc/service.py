import tensorflow as tf


class CalcService:

    def __init__(self):
        pass

    @staticmethod
    def calc(num1, num2, opcode):
        print("서비스 내부 {} {} {} = ".format(num1, num2, opcode))
        sess = tf.Session()
        saver = tf.train.import_meta_graph('calc/saved/model-1000.meta')  # 아까 first파일 실행 후 생긴 메타파일 불러오기
        saver.restore(sess, tf.train.latest_checkpoint('calc/saved/'))
        graph = tf.get_default_graph()
        w1 = graph.get_tensor_by_name("w1:0")  # first파일에 만들어놓은 w1, w2 변수를 초기화함
        w2 = graph.get_tensor_by_name("w2:0")
        feed_dict = {w1: float(num1), w2: float(num2)}  # 새로운 값을 줌.  실수값으로 넘어오게 함
        if opcode == 'multi':
            op_to_restore = graph.get_tensor_by_name("op_to_restore:0")
        # 일단은 곱셈만 실습해봄
        result = sess.run(op_to_restore, feed_dict)

        return int(result)  # 결과는 정수값(int)으로만 나오게 함


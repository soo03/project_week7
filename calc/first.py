import tensorflow as tf


class First:

    def __init__(self):
        pass

    @staticmethod
    def execute():    #staticmethod를 선언해놓으면 (self)를 지워도 됨
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        b1 = tf.Variable(2.0, dtype=tf.float32, name='bias')
        feed_dict = {'w1': 4.0, 'w2': 8.0}
        w3 = w1 + w2
        w4 = tf.multiply(w3, b1, name='op_to_restore')
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()  # 훈련이 끝난 지점에서 saver
        result = sess.run(w4, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print(" 결과 : {} ".format(result))

        saver.save(sess, './saved/model', global_step=1000)  # saved라는 디렉토리를 만들어놓았음. 그 안에 저장

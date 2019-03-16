import tensorflow as tf
import numpy as np
from cabbagePrice.model import CabbageModel

class CabbageTrainer:
    def __init__(self):
        pass

    @staticmethod  # 위의 init(self)와 관련없음(self인자가 공유되지 않으므로 staticmethod를 선언해야 함)
    def test(data):
        obj = CabbageModel(data)  # 테스트를 위한 모델에 데이터 주입
        # obj.create()               # 생성 # 한번 실행한 후에는 다시 실행되지 않게 주석으로 막음

        X = tf.placeholder(tf.float32, shape=[None, 4])  # 변수 4개
        Y = tf.placeholder(tf.float32, shape=[None, 1])  # 행은 None, 열(=배추가격)은 1개
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        # 가설 설정
        hypothesis = tf.matmul(X, W) + b

        model = tf.global_variables_initializer()  # 모델 초기화해서 불러오기
        avg_temp = float(input("평균 온도: "))   # 4가지 변인들
        min_temp = float(input("최저 온도: "))
        max_temp = float(input("최고 온도: "))
        rain_fall = float(input("강수량: "))
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(model)
            saver.restore(sess, "./saved/cabbage_model.ckpt")   # saver 다시 불러오기(restore)
            data = ((avg_temp, min_temp, max_temp, rain_fall),)  # 4가지 요인들과 그 외: ((요인들),)
            arr = np.array(data, dtype=np.float32)
            x_data = arr(0.4)
            dict = sess.run(hypothesis, feed_dict={X: x_data})
            print("예측되는 배추가격 {}원".format(dict[0]))
































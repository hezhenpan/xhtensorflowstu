# *_*coding:utf-8 *_*

import tensorflow as tf

a = tf.constant(2,name="a")

b = tf.constant(3,name="b")

x = tf.add(a,b,name="add")

r = tf.random_normal([2,3],mean=1.0,dtype=tf.float32,name="random")

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs',sess.graph)
    print(sess.run(r))




# *_*coding:utf-8 *_*

import tensorflow as tf

# a = tf.constant(2, name="a")
#
# b = tf.constant(3, name="b")
#
# x = tf.add(a, b, name="add")
#
# r = tf.random_normal([2, 3], mean=1.0, dtype=tf.float32, name="random")
#
# with tf.Session() as sess:
#     writer = tf.summary.FileWriter('./graphs', sess.graph)
#     print(sess.run(r))


# my_const = tf.constant([1.0, 2.0], name="my_const")

# print(tf.get_default_graph().as_graph_def())

# a = tf.Variable(2, name="scalar")
#
# b = tf.Variable([2, 3], name="vector")
#
# c = tf.Variable([[0, 1], [2, 3]], "matrix")
#
# w = tf.Variable(tf.zeros([784, 10]))
#
# init = tf.global_variables_initializer()

w = tf.Variable(tf.truncated_normal([700,10]))


with tf.Session() as sess:
    sess.run(w.initializer)
    print(w.eval())




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

# w = tf.Variable(10)
#
# sess1 = tf.Session()
# sess2 = tf.Session()
#
# sess1.run(w.initializer)
# sess2.run(w.initializer)
#
# print(sess1.run(w.assign_add(10)))
#
# print(sess2.run(w.assign_sub(32)))
#
# print(sess1.run(w.assign_add(100)))
# print(sess2.run(w.assign_add(154)))
#
# sess1.close()
# sess2.close()

a = tf.placeholder(tf.float32, shape=[3])

b = tf.constant([5, 5, 5], tf.float32)

c = a + b

import tensorflow as tf
import numpy as np

training_data=np.array([
		[1,2],
		[2,5],
		[4,2],
		[5,6],
		[1,4],
		[5,6],
		[3,4],
		[7,10]
	])

real_values=np.array([[1,0,0,1,0,0,1,0]]).T

x=tf.placeholder(tf.float32,[None,2])
w=tf.Variable(tf.zeros([2,2]))
b=tf.Variable(tf.zeros([2]))

predicted=tf.add(tf.matmul(x,w),b)

y__= tf.reciprocal(1 + tf.exp(-predicted))


y=tf.placeholder(tf.float32,[None,1])

#hyperparameters

learning_rate=0.01
training_epochs=20000
display_step=50
n_samples=real_values.size

#cost=tf.nn.sigmoid_cross_entropy_with_logits(predicted, y)
cost=tf.reduce_sum(tf.pow(y-y__,2))/(2*n_samples)
optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)


for i in range(training_epochs):
	sess.run(optimizer,feed_dict={x:training_data,y:real_values})
	if i%display_step==0:
		c=sess.run(cost,feed_dict={x:training_data,y:real_values})
		print("training ",'%04d'%i," cost=","{:.09f}".format(c))
print("\nOPTIMIZATION IS DONE NOW!!!!")


print("training cost=",sess.run(cost,feed_dict={x:training_data,y:real_values}),"\nW=",sess.run(w),"\nb=",sess.run(b))

z=sess.run(y__,feed_dict={x:training_data})
print(z)


sess.run(tf.nn.softmax([.1,.2]))
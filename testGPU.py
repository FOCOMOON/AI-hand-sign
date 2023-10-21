import tensorflow as tf

# ตรวจสอบว่า TensorFlow ใช้ GPU หรือไม่
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

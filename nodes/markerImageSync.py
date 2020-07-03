import message_filters
import rospy

from std_msgs.msg import Header
from sensor_msgs.msg import Image
from ar_pose.msg import ARMarker
#cassandra_ros/MarkerImage
from cassandra_ros.msg import MarkerImage

#shell> rostopic type /camera/image_rect
#sensor_msgs/Image
#shell> rostopic type /ar_pose_marker
#ar_pose/ARMarker

# This callback is used to merge partial marker and image data into
# a new type 'cassandra_ros.MarkerImage'
def callback(image, marker):
  rospy.loginfo("--> Image and Marker read.")
  # MarkerImage type is:
  #Header header
  #uint32 marker_id
  #geometry_msgs/Pose marker_pose
  #uint32 image_height
  #uint32 image_width
  #string image_encoding
  #uint8 image_is_bigendian
  #uint32 image_step
  #uint8[] image_data
  
  pub.publish(marker.header, marker.id, marker.pose.pose, 
              image.height, image.width, image.encoding, 
              image.is_bigendian, image.step, image.data)


if __name__ == "__main__":
  rospy.init_node('MarkerImageSync')
  
  image_sub = message_filters.Subscriber('/camera/image_rect', Image)
  marker_sub = message_filters.Subscriber('/ar_pose_marker', ARMarker)
  
  rospy.loginfo("# Initializing Publisher...\n")

  pub = rospy.Publisher('marker_out', MarkerImage, queue_size=100)
  rate = rospy.Rate(100) # 100hz
  
  rospy.loginfo("# Initializing TimeSynchronizer(image, marker)\n")
  ts = message_filters.TimeSynchronizer([image_sub, marker_sub], queue_size=100)
  ts.registerCallback(callback)
  rospy.spin()

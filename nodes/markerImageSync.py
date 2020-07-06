#!/usr/bin/env python
import message_filters
import rospy

from std_msgs.msg import Header
from sensor_msgs.msg import Image
from ar_pose.msg import ARMarker
from visualization_msgs.msg import Marker
#cassandra_ros/MarkerImage
from cassandra_ros.msg import MarkerImage

#shell> rostopic type /camera/image_rect
#sensor_msgs/Image
#shell> rostopic type /ar_pose_marker
#ar_pose/ARMarker

# This callback is used to merge partial marker and image data into
# a new type 'cassandra_ros.MarkerImage'
def callback(image, marker, rviz):
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
  
  pub_marker_image.publish(marker.header, marker.id, marker.pose.pose, 
                           image.height, image.width, image.encoding, 
                           image.is_bigendian, image.step, image.data)
  
  pub_marker.publish(rviz)
  pub_image.publish(image)


if __name__ == "__main__":
  rospy.init_node('MarkerImageSync')
  
  image_sub = message_filters.Subscriber('/camera/image_rect', Image)
  marker_sub = message_filters.Subscriber('/ar_pose_marker', ARMarker)
  rviz_sub = message_filters.Subscriber('/visualization_marker', Marker)
  
  rospy.loginfo("# Initializing Publisher...\n")

  pub_marker_image = rospy.Publisher('sync_marker_image', MarkerImage, queue_size=100)
  pub_marker = rospy.Publisher('sync_marker', Marker, queue_size=100)
  pub_image = rospy.Publisher('sync_image', Image, queue_size=100)
  
  rate = rospy.Rate(100) # 100hz
  
  rospy.loginfo("# Initializing TimeSynchronizer(image, marker)\n")
  ts = message_filters.TimeSynchronizer([image_sub, marker_sub, rviz_sub], queue_size=100)
  ts.registerCallback(callback)
  rospy.spin()

#!/usr/bin/env python

import rospy
from rosgraph_msgs.msg import Clock
from std_msgs.msg import String

rospy.init_node('cassandraBagClock', disable_rostime=True)
pub = rospy.Publisher('/clock', Clock, queue_size=10)
print "node initialized"

secs = 1590284291
usecs = 861526012

t = rospy.Time(secs, usecs)
r = rospy.Rate(1) # 10hz

while not rospy.is_shutdown():
    #t = rospy.Time.now()
    t = rospy.Time(secs, usecs)
    msg = Clock()
    msg.clock = t
    print t.to_sec()
    pub.publish(msg)
    r.sleep()
    secs = secs + 1

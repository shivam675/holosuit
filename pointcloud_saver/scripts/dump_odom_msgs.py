import rospy
from nav_msgs.msg import Odometry


# list_of_odom_msgs = []



def odom_callback(odom):
    # rospy.loginfo_once("Callback entered")
    time = odom.header.stamp
    x1 = odom.pose.pose.position.x
    y1 = odom.pose.pose.position.y
    z1 = odom.pose.pose.position.z
    l = [x1, y1, z1, time]
    # list_of_odom_msgs.append(l)
    
    with open('odom.txt', 'a') as f:
        f.write('%s\n' %l)
    f.close()




if __name__=="__main__":
    rospy.init_node("odom_sub", anonymous=True)
    odom_sub = rospy.Subscriber("/odom", Odometry, odom_callback, queue_size=30)
    while not rospy.is_shutdown():
        rospy.spin()
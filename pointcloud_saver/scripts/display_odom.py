import rospy
import sensor_msgs.point_cloud2 as pc2
import pcl
import message_filters
from nav_msgs.msg import Odometry

list_of_odom_msgs = []

def ros_to_pcl(ros_cloud, odom_msg):
    points_list = []
    for data in pc2.read_points(ros_cloud, skip_nans=True):
        points_list.append([data[0], data[1], data[2], data[3]])

    x1 = odom_msg.pose.pose.position.x
    y1 = odom_msg.pose.pose.position.x
    z1 = odom_msg.pose.pose.position.x

    points_list.append([x1, y1, z1, 1])

    pcl_data = pcl.PointCloud_PointXYZRGB()
    pcl_data.from_list(points_list)

    return pcl_data


def pc_odom_callback(pc_msg, odom_msg):
    list_of_odom_msgs.append([
        odom_msg.pose.pose.position.x, 
        odom_msg.pose.pose.position.y, 
        odom_msg.pose.pose.position.y])
    cloud = ros_to_pcl(pc_msg, odom_msg)
    




if __name__ == "__main__":
    rospy.init_node("point_cloud_sub", anonymous=True)
    rospy.loginfo("INITIALIZED....")
    # pc_sub = rospy.Subscriber("/points", pc2.PointCloud2, point_cloud_callback, queue_size=3)
    pc_sub = message_filters.Subscriber("/rtabmap/cloud_map", pc2.PointCloud2)
    odom_sub = message_filters.Subscriber("/odom", pc2.PointCloud2)

    ts = message_filters.TimeSynchronizer([pc_sub, odom_sub], 10)
    ts.registerCallback(pc_odom_callback)

    while not rospy.is_shutdown():
        rospy.spin()
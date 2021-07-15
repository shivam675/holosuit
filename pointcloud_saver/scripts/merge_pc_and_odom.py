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

def main(cloud):
    
    pass




if __name__ == "__main__":
    cloud = pcl.load_XYZRGB('400Kpoints.pcd')
    main(cloud)
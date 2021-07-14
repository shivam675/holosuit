#!/usr/bin/env python

import rospy
import sensor_msgs.point_cloud2 as pc2
import pcl
# import tf



def ros_to_pcl(ros_cloud):
    points_list = []
    for data in pc2.read_points(ros_cloud, skip_nans=True):
        points_list.append([data[0], data[1], data[2], data[3]])

    pcl_data = pcl.PointCloud_PointXYZRGB()
    pcl_data.from_list(points_list)

    return pcl_data


def point_cloud_callback(pcl_msg):
    cloud = ros_to_pcl(pcl_msg)
    # vox = cloud.make_voxel_grid_filter()
    # LEAF_SIZE = 0.006
    # vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)
    # cloud = vox.filter()
    pcl.save(cloud, "cloud.pcd")



if __name__ == "__main__":
    rospy.init_node("point_cloud_sub", anonymous=True)
    rospy.loginfo("INITIALIZED....")
    # pc_sub = rospy.Subscriber("/camera_intelrealsense/depth/point_cloud", pc2.PointCloud2, point_cloud_callback, queue_size=3)
    pc_sub_msg = rospy.wait_for_message("/points", pc2.PointCloud2, timeout=None)
    point_cloud_callback(pc_sub_msg)
    # while not rospy.is_shutdown():
    #     rospy.spin()
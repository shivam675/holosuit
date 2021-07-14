#!/bin/sh
# xterm  -e  ""
rosrun pointcloud_saver point_cloud_saver.py & # running node to save to pcd
sleep 5
echo Saving file in current directory
sleep 1
# xterm  -e ""
pcl_pcd2ply cloud.pcd output.ply
echo DONE!

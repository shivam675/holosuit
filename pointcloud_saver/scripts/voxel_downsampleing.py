import pcl

def main(LEAF_SIZE):    
    # Load Point Cloud file
    cloud = pcl.load_XYZRGB('400Kpoints.pcd')

    vox = cloud.make_voxel_grid_filter()
    vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)
    cloud = vox.filter()

    pcl.save(cloud, "downSampled.pcd")

if __name__=="__main__":
    main(LEAF_SIZE = 0.002)
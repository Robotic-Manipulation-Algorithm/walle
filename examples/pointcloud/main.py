import cv2
import os
import numpy as np

from walle.pointcloud import PointCloud


if __name__ == "__main__":
    data_dir = os.path.dirname(os.path.realpath(__file__))
    cam_intr = np.loadtxt(os.path.join(data_dir, "camera_intrinsics.txt"), delimiter=" ")
    cam_pose = np.loadtxt(os.path.join(data_dir, "camera_pose.txt"), delimiter=" ")
    depth_im = cv2.imread(os.path.join(data_dir, "depth.png"), -1).astype(float) / 10000
    color_im = cv2.cvtColor(cv2.imread(os.path.join(data_dir, "color.png")), cv2.COLOR_BGR2RGB)

    # create pointcloud from RGB-D and visualize
    pc = PointCloud(color_im, depth_im, cam_intr)
    pc.make_pointcloud(cam_pose, depth_trunc=1.7, trim=True)
    pc.view_point_cloud()

    # visualize normals
    pc_down = pc.downsample(voxel_size=0.01, inplace=False)
    pc_down.compute_normals()
    print("Press 9 to visualize normal heatmap.")
    pc_down.view_point_cloud()

    # create heightmap
    pc.make_heightmap(cam_pose, np.asarray([[0.15, 1.2], [-0.3, 0.4], [-5, 0]]), 0.002, -2)
    pc.view_height_map(figsize=None)

    print(pc.color_im.shape)
    print(pc.depth_im.shape)

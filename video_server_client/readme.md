## Sending video stream via socket

On server side (remote laptop) start:
```bash
python3 server.py
```

On client side (robot, embedded pc, Odroid):
```bash
python3 client.py LAPTOP_IP
```

## Using ROS

Another option is to transfer image data as ROS messages.
1. Set up ROS network on multiple machines: http://wiki.ros.org/ROS/Tutorials/MultipleMachines

2. Start [usb-cam-node](http://wiki.ros.org/usb_cam) on the robot:
```bash
roslaunch usb_cam usb_cam-test.launch
```

3. Check image messages recieved on the ground station:
```bash
rostopic list
```
You should see:
```bash
/rosout
/rosout_agg
/usb_cam/camera_info
/usb_cam/image_raw
/usb_cam/image_raw/compressed
/usb_cam/image_raw/compressed/parameter_descriptions
/usb_cam/image_raw/compressed/parameter_updates
/usb_cam/image_raw/compressedDepth
/usb_cam/image_raw/compressedDepth/parameter_descriptions
/usb_cam/image_raw/compressedDepth/parameter_updates
/usb_cam/image_raw/theora
/usb_cam/image_raw/theora/parameter_descriptions
/usb_cam/image_raw/theora/parameter_updates
```

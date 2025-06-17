<div align="center">
<img alt="" src="https://github.com/RasterScan/Floor-Plan-Digitalization/assets/100861353/9d11859f-ba5e-44cb-84d6-8067327b6ffe.png" width=200/>
</div>

# Floor-Plan-Recognition

It's the implementation to convert Raster to Vector on floor plan images.

## Before You Start
**Star us on GitHub, and be instantly notified for new release!**

![vlc-record-2024-04-04-20h47m49s-2024-04-04 20-46-42 mkv-](https://github.com/RasterScan/Floor-Plan-Recognition/assets/100861353/2ff494e2-12bb-4efb-8433-be096739037a)

## Installation
```bash
docker pull rasterscan/floor-plan-recognition:latest-cpu
docker run --name rasterscan-service -d -p 8888:8888 rasterscan/floor-plan-recognition:latest-cpu
```

The application will start on `http://localhost:8888` by default.

## Available Endpoints

- `/health` (GET): Health check endpoint
- `/get_machine_code` (GET): Get machine code to get lifetime license
- `/activate_machine` (POST): Activate the SDK
- `/plan_recognition` (POST): Recognize floor plan image file
- `/plan_recognition_on_base64` (POST): Recognize floor plan base64 image

## Update
- 2024/08/26. Room determination algorithm is added

## Original Paper
[Raster-to-Vector: Revisiting Floorplan Transformation](https://jiajunwu.com/papers/im2cad_iccv.pdf)

## Demo
https://huggingface.co/spaces/RasterScan/Automated-Floor-Plan-Digitalization

## API Portal
https://rapidapi.com/akashdev2016/api/floor-plan-digitalization

## Benifits
- It will reduce lots of manual work to design floor plan
- It will be more easier to create 3D floor plan automatically


Please reach out to me to get on-premise solution (Email: contact@rasterscan.com, WhatApp: +19382025720)



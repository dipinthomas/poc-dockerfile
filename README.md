# Docker Image

Like most people, I forget to document the process after doing a quick POC. Most of the time, the code used in the POC will be useful later on, so I created this repository to save all of my POC code and Docker files. 


# Folder Overview

## haproxy-with-ec2-metadata

A Haproxy docker image with pip package to fetch AWS EC2 metadata. The image accepts connection request on below three ports:

* 80 - Incoming request which will be forwarded to a backend service
* 5000 - Flask application which will fetch and return ec2-metadata when running on EKS.
* 9000 - HA proxy health & traffic stats 


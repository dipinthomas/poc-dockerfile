# Docker Image

Like most people after doing quick POC I forget to document the process, most of the time code used in POC will be helpful in later stage, hence this repository to save all my POC code and dockerfiles. 

# Folder Overview

## haproxy-with-ec2-metadata

A Haproxy docker image with pip package to fetch AWS EC2 metadata. The image accepts connection request on below three ports:

* 80 - Incoming request which will be forwarded to a backend service
* 5000 - Flask application which will fetch and return ec2-metadata when running on EKS.
* 9000 - HA proxy health & traffic stats 


#!/usr/bin/bash

# Navigate to the `opt` directory
cd /opt/

# Download Python 3.8.1 from the official repository
sudo wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz

# Verify the file is properly downloaded
sudo ls -l | grep Python

# Unpack the archive
sudo tar -xf Python-3.8.1.tar.xz

# Install the Linux packages necessary for Python 3.8.1 installation
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel

# Navigate to the directory with the Python 3.8.1
cd Python-3.8.1/

# Prepare the Python for installation
sudo ./configure --enable-optimizations

# Install Python 3.8.1
sudo make altinstall

# Check the version of the installed Python
python3.8 -V

# ape14
This repository contains sample solutions for the lab exercises contained in the Arista Programming Essentials (APE) 1.4 course.

All scripts and other files where made using "Student-06" so make sure that you make appropriate substitions for your student number in IP addresses, etc. 

Since git is not installed on the lab server you can't simply "git clone" this repository to the lab server, but if you want to install the scripts on the lab server for comparison or testing you can pull them down using the "pull.sh" script or just copy and paste the following code:
```
rm -rf ape14-samples
curl -L -o master.tar http://github.com/layer-zero/ape14/tarball/master/
tar xvf master.tar
mv layer-zero-ape14-* ape14-samples
rm master.tar
```

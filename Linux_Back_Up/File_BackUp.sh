# creating tar of some certain documents 
# flags - 
# c create a tar file
# f to give the op as a file rather posting on the standered op means the console 
# a is to compress the file as tar.gz 
# v is verbose like list all the files that will be compressed 

# One arguements are needed to be passed 
#echo "Enter the path " 
#echo "Number of args" >> test
#echo $# >> test   # total number of arg passed
#echo $1 
#Path = $1 

#clear 

echo "The directory conatins --------- >  " >> test 
ls $1 >> test 

# file name will be current date and time 
name=$(date +"%T")  

# Showing the path
#echo "Proceed with zipping at -->  $path [y/n] " >> test 
#ans='y' 
#echo $ans >> test 

#if [ 'y'  == 'y' ] 
#then 
#	clear 
	echo "<------ Starting to zip the filei ----> " >> test 	
	tar cavf file.tar.gz $1 >> test 

	echo "<---------File zipped Successfully------>" >> test 
	echo "#   .............Renaming the file . . . . . . .   #" >> test 

	# adding this line to store the file in time format 
	mv file.tar.gz $name.tar.gz 
	echo "File renamed Successfully" >> test 
#else 
#	exit 
#fi 

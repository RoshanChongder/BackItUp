# To extarct tar
# Flags used - 
# x To extact the content of the file 
# F to extarct to a file 
# z to decompress 
# v to verbose 

# It will take one arguements - 
# 1. File path of the tar file  

#echo "Enter the path of the file to extract "
#read path 

#clear 

echo "The selected file is  $path . . "
#ls $pah 

#echo "Continue ? [y/n] "
#read ans 

#if [ $ans == 'y' -o $ans == 'Y' ]
#then 
	echo "< -----------------  Starting to extract the zip file ------------- >  " >> test 
	tar xfzv $1 	
	echo "# ..........  File is unzipped successfully ......... #  " >> test 
#else 
#	exit 
#fi


 


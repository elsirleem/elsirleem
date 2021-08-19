#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lawal S.
# DATE CREATED:  08/08/2021                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #retrieves filenames from folder pet_images/
    filename_list  = listdir("pet_images/")
    #print 10 of the filenames from the folder pet_images/
    print("\nPrints 10 filenames from the folder pet_images/")
    for idx in range(0, 10, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))
     #in_files = listdir(image_dir)
     
    # this is to print 10 of the filenames from folder specified as image_dir/
    #print("\nPrints 10 filenames from folder specified as image_dir")
    #for idx in range (0, min(10, len(in_files)), 1):
      #  print("{:2d} file: {:>25}".format(idx + 1, in_files[idx]))
    
    # creating an empty dictionary results_dic
    results_dic = dict()
    
    # number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)
          
    # Add new key-value pairs to dictionary ONLY when key doesn't already exist. 
    # This dictionary's value is a list that contains only the pet image label
    
    filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    pet_labels = ["beagle", "boston terrier"]
    
    for idx in range (0, len(filenames), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
       if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [pet_labels[idx]]
       else:
        print("** Warning: Key=", filenames[idx], 
               "already exists in results_dic with value =", 
               results_dic[filenames[idx]])
            
    # Iterate through a dictionary printing all keys and their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet label=", results_dic[key][0])   

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

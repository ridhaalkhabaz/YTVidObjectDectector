# YTVidObjectDectector


## Contributors
* Ridha Alkhabaz (ridhama2@illinois.edu/ ridha.alkhabaz@gmail.com)
* German Bautista (gbauti5@illinois.edu) 



## Project overview
We want to detect objects in Youtube videos. Then, we want to detect the object when it appears. 


### Relevant Publications
* https://doi.org/10.32470/CCN.2018.1137-0
* https://arxiv.org/pdf/2004.10934.pdf
* https://ccneuro.org/2018/proceedings/1137.pdf
* https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhu_Towards_High_Performance_CVPR_2018_paper.pdf
* https://openaccess.thecvf.com/content_cvpr_2016/papers/Kang_Object_Detection_From_CVPR_2016_paper.pdf
* https://arxiv.org/pdf/1506.02640.pdf



## File structure:

* **Data**: Our data is from a youtube video that is located in the /videos folder. We use roboflow and some python scripts, like YTVidTFrame.py to create frames.
	* We could not upload the resulting data set because it is too big for git hub.   


* **Model** In YOLOv4_Training_and_Creating_Deploying.ipynb, we create and train our YOLOv4 model. In addition, we test it against multiple images. 
	* This takes at least 6 hours to run.
	* There you can use a link to youtube video to run videos.
	* The best weights are provided by linking a drive folder to google collab. 
	


## Results

We achieve higher accuracy of 93.75 % in our YOLO classifier. 

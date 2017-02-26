int main(int argc, char **argv){

 

 IplImage *pFrame = NULL, *srcImage=NULL;

 CvCapture *pCapture = NULL;

 //pCapture = cvCaptureFromFile("rtsp://admin:12345@192.168.7.45:554/h264/ch1/main/av_stream");
 pCapture = cvCreateFileCapture("rtsp://admin:default@10.1.10.173/h264");
 //pCapture = cvCreateCameraCapture(1);
 if(!pCapture){
  printf("Can not get the video stream from the camera!\n");
  return NULL;
 }

 //read the video by frame
 //while(1)
 while(1){
  //pFrame = cvQueryFrame(pCapture);
  if (srcImage==NULL)
  {
   pFrame = cvQueryFrame(pCapture);
   srcImage=cvCloneImage(pFrame);
   cvShowImage("123234",srcImage);
   //cout<<pFrame->width<<","<<pFrame->height<<endl;
   cvWaitKey(10);
   cvReleaseImage(&srcImage);
   srcImage=NULL;
  }

 }
 cvReleaseCapture(&pCapture);
 cvReleaseImage(&pFrame);


 return 0;
}

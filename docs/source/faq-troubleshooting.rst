7.FAQs And Troubleshooting
====================================

Where can I get the Take2 Proctoring API key and Secret key?
Please contact us at - ms@taketwotechnologies.com
I do not have an AWS account, can I access this plugin?
Yes, you can access the plugin. you can use the Take2 Proctoring API, which does not require an AWS account.
Why does the ‘Start Attempt’ modal  show a ‘No face detected’ warning?
Please allow ‘webcam access’ from your browser settings.
For chrome, enable ‘camera access’ from the video icon on the right side of the address bar. For safari, in the safari browser, go to preferences, and click 'allow' for your website to access the camera.
Where can I get the AWS API key and Secret key?
Please refer to the ‘Usage Accessibility’ section in the Plugin Documentation to generate AWS keys from your AWS account.
How can I add the AWS API key and Secret Key in Moodle™?
Go through the ‘Proctoring plugin configuration’ section in the Plugin Documentation.
As an admin, why am I getting the warning ‘Please complete AWS configuration to continue with the quiz?’
Check whether the ‘AWS access and Secret keys’ are set up in the ‘Moodle Proctoring’. Refer to the ‘Proctoring plugin configuration’ section in the Plugin Documentation.
As a student, Why am I getting the warning ‘The quiz is not properly configured. Please contact the site administrator.’
For a properly configured quiz, the plugin requires a mandatory ‘AWS or Take2 API key and Secret key’ to be set up in the ‘Moodle Proctoring.’
Where can I report an issue regarding this plugin?
Please raise your issue on:  https://github.com/taketwotech/moodle-quizaccess_quizproctoring/issues
Why am I unable to use this plugin on localhost?
Due to security reasons, cameras work only on https. 
You can go through the link: steps to allow the camera on the local host. 
How to fix this error on a moodle site hosted on Windows?
Error executing "DetectFaces" on "https://rekognition.us-east-1.amazonaws.com"; AWS HTTP error: cURL error 60: SSL certificate problem: unable to get local issuer certificate


Download and extract cacert.pem following the instructions at https://curl.se/docs/caextract.html
Save it on your filesystem somewhere (for example, XAMPP users might use C:\xampp\php\extras\ssl\cacert.pem)
In your php.ini, put this file location in the [curl] section (putting it in the [openssl] section is also a good idea): 
[curl]
curl.cainfo = "C:\xampp\php\extras\ssl\cacert.pem"
[openssl]
openssl.cafile = "C:\xampp\php\extras\ssl\cacert.pem"
Restart your web server (e.g. Apache) and PHP FPM server if applicable
   Why am I unable to see Proctoring Images and Proctoring Identity Buttons for any user?
Make sure you have Proctoring Images Show checkbox marked in Site administration -> Plugins -> Activity modules -> Quiz -> Moodle Proctoring.
Make sure you are allowed the user role permission named View the Proctoring Images and Proctoring Identity buttons.
Why only the main image is showing in the Proctoring Images button?
If the user did not get any warning during the quiz then the Proctoring Images button will display the main image only.
Why am I unable to see the Proctoring Identity button for any user?
Since the Photo ID field of the ‘Start Attempt’ modal has been made optional the Proctoring Identity button will not appear if the participant has not uploaded the photo ID. 
Is any data stored by Moodle Proctoring?
No, Moodle Proctoring does not store any data on our servers. All image data, including proctoring images and other relevant information, is stored locally on your own server. The plugin ensures that data remains within your infrastructure, and we do not have access to or store any of your data.


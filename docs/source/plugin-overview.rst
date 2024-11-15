1. Plugin Overview
================

Name
----
Moodle Proctoring plugin

Purpose
-------
Provides proctoring functionalities for online quizzes in Moodle, including:

* Webcam capture of user activity at set intervals
* Identity verification against captured images
* Warning alerts for potential cheating attempts

Features
--------

Real-time Human Proctoring
^^^^^^^^^^^^^^^^^^^^^^^^^^
The plugin allows for a human proctor to continuously monitor the student's activity during the quiz, including webcam feed and microphone audio.

Customizable Capture Intervals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Instructors can set the frequency at which the plugin captures images of the student's activity.

Identity Verification
^^^^^^^^^^^^^^^^^^^
The plugin compares the student's face to a pre-captured image, ensuring that the correct individual is taking the quiz.

Configurable Warning System
^^^^^^^^^^^^^^^^^^^^^^^^^^
Instructors can set the number of warnings issued to students for suspicious activity, such as:

* Leaving the camera view
* Switching tabs or windows
* Eyes not detected properly
* Face covered or obscured
* Two faces detected in the camera frame

Proctoring Report
----------------

Interface for Reviewing Captured Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Admins and Teachers can review all captured images and activity logs for each proctored quiz attempt within the Proctoring Report interface. This includes images flagged for warnings and any other captured data, allowing instructors to assess quiz integrity thoroughly.

Data Storage Options
^^^^^^^^^^^^^^^^^^
Admins and Teachers can select whether to store all images or only those triggered by warnings on a per-quiz basis.

Manual Deletion Options
^^^^^^^^^^^^^^^^^^^^^
Within the report interface, users can delete captured images manually, with a checkbox for permanent deletion (irreversible) or standard deletion (images stored until the next scheduled hard delete).

Automated Hard Delete
^^^^^^^^^^^^^^^^^^^
Images can be configured for automatic deletion at set intervals (1 month, 3 months, 6 months, or 1 year), managed by a cron job that regularly clears stored data beyond the selected retention period.

Permission Management
^^^^^^^^^^^^^^^^^^
Admins can restrict report access permissions, allowing only selected users (typically Teachers and Admins) to view and manage proctoring data in the report.

Target Audience
-------------

Administrators
^^^^^^^^^^^^^
Can modify permissions for all users and configure the plugin settings across the Moodle platform.

Instructors
^^^^^^^^^^
Can configure proctoring for their quizzes (if allowed by the administrator), monitor live activity, and review captured data.

Students
^^^^^^^
Automatically interact with the proctoring system during quizzes but don't need special permissions assigned.

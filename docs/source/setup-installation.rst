3. Setup and Installation
=========================

Pre-requisites:
---------------
- A Moodle platform (version 4.0 or later)
- A Moodle admin account with appropriate permissions

Steps:
------
**Install Moodle**  
If you haven't already, install Moodle on your server or hosting platform. Follow the official `Moodle installation instructions <https://docs.moodle.org/405/en/Installing_Moodle>`_.

**Download the Plugin**  
Download the Moodle Proctoring plugin from the Moodle Plugin Directory. You can find it by searching for "Moodle Proctoring plugin" or simply `click here to download it <https://moodle.org/plugins/quizaccess_quizproctoring>`_.

**Upload the Plugin**  
1. Log in to your Moodle site as an administrator.
2. Go to ``Site administration`` -> ``Plugins`` -> ``Install plugins``.
3. Upload the downloaded plugin file (usually a `.zip` file).

.. note::  
   While installing, refer to the basic `Moodle plugin installation guide <https://docs.moodle.org/405/en/Installing_plugins>`_ to ensure all recommended steps and requirements are met.

**Activate the Plugin**  
After the plugin is installed, activate it by going to ``Site administration`` -> ``Plugins`` -> ``Activity modules`` -> ``Quiz`` -> ``Proctoring quiz access rule``.

**Configure the Plugin**
-------------------------
1. **External Server Token and Secret Token (for Take2 Proctoring):**  
   If you're using the Take2 Proctoring API for identity verification, enter the provided token and secret key in the corresponding fields.

2. **Time Interval:**  
   Set the interval at which the plugin will capture images of the student's activity during the quiz.

3. **Proctoring Image Show:**  
   Enable this option to view captured images on the Review Attempts page of the quiz.

4. **Enable Proctoring for Quizzes:**  
   - Go to the ``Edit Settings`` of the quiz you want to proctor.
   - In the ``Extra restrictions on attempts`` section, select ``Yes`` to enable proctoring.
   - Set up the desired time interval and warnings threshold.

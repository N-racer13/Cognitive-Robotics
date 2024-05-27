Code developed by Nathan Van Damme, ID:210820414

to run the package:
1) unzip the cr_week8_test in your catkin workspace;
2) run in terminal:
	$ roscore
3) in a new terminal, navigate to the catkin_ws folder and build the catkin environment using: 
	$ catkin_make
4) run in terminal:
	$ roslaunch cr_week8_test human_robot_interaction.launch

In case of permission errors, navigate to the cr_week8_test folder in the terminal and make the nodes executable using:
	$ chmod +x scripts/<script_name>.py

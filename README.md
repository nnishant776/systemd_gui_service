# GUI Systemd Service Creator

A GUI application which helps to create a GNU/Linux **`systemd`** service file with common configuration options. Please note that this application will **NOT** provide all the options for the configuration. For more uncommon options, you may have to edit the required options yourself after the basic service file is generated. This is due to currently limited GUI of the applications which is planned to be upgraded and should consequently add more unit configuration options.

## Getting Started

To get this application you can follow one of the two listed methods below.

#### Installation using pre-built package
----
You can install this application by simply using the pre-built package present in `dist` folder of this repository. The package is the file with `.whl` extension. To install this package on your local system, follow below steps.

- Download the package file (.whl) in any directory of your choice 
- Open a terminal and navigate to the directory where you downloaded the package file.
- Run the following command

	```
	$ pip3 install <filename ending with .whl>
	```
	or alternatively
		
	```
	$ pip3 install *.whl
	```
	<br>
	
	**NOTE** : Above command will install this application as a non-privilieged user. If you have admin or `sudo` privilieges and want to install this application system-wide, use below commands.
	
	```
	$ sudo pip3 install <filename ending with .whl>
	```
	
	or alternatively
	
	```
	$ sudo pip3 install *.whl
	```
	

<br>

#### Installation by manual build
----

**Note**: This method is pointless unless you are planning to modify this application to your liking or develop it further. For users who simply want this application for general use, it would be better to use previous method.

To build and install this application on your local computer, you need to have `setuptools` and `wheel` packages installed on your system. To check if you have these packages installed, run below command on a terminal.

```
$ pip3 list | grep -iE "setuptools|wheel"
```

If you have these packages installed you should see some output on your terminal window, something similar to this

```
$ pip3 list | grep -iE "setuptools|wheel"
setuptools         47.1.1
wheel              0.34.2
```

If you don't see any output of the command, it means you don't have these packages installed. To install these packages, run below command.

```
$ pip3 install setuptools wheel
```

<br>
After the installation is done, you are ready to build the application. Follow below steps

- First, clone this repository in any directory of your choice. Use below command.

	```
	$ git clone https://github.com/nnishant776/systemd_gui_service.git
	```
	
- Then, run below command to build the package.

	```
	$ cd systemd_gui_service/
	$ python3 setup.py sdist bdist_wheel
	```
	
	This will create/update a folder named `dist` in the current directory (`systemd_gui_service`) and place a `.whl` package as a result of above build command.
	
- Then, to install the package, run the following command
	
	```
	$ pip3 install dist/*.whl
	```
	if you want to install this application system-wide, you need to have admin or `sudo` privileges. Then run the following command.
	
	```
	$ sudo pip3 install dist/*.whl
	```
	<br>

## Usage

After installation in the previous section, you will be able to find this application in your corresponding applications menu by the name **"Systemd Service Creator"**. You can also launch this program from terminal using following command

```
$ service_creator
```

The application will open with a blank page with usual wizard buttons. Clicking "Next" will take you through the configuration windows of different sections of the service as shown below

<p>
<img src="https://drive.google.com/uc?export=view&id=12uyvPa0iHK78EcFEVSb317QVH_GP3hiQ" height=480 /> 
<img src="https://drive.google.com/uc?export=view&id=18ozXFO35wLi_2PvB3Bt5HEYf5rIvoIi1" height=480 />
<img src="https://drive.google.com/uc?export=view&id=1ik7pyGzJ5eUhKdRjjVzO_Z8fgOCXwkpd" height=480 />
<img src="https://drive.google.com/uc?export=view&id=1vgn-WwflRTi339zi4ipvgOw8D2QooDD_" height=480 />
<img src="https://drive.google.com/uc?export=view&id=164b7OZiklz9MVkAWOFJ9EsCwpW-u0wYX" height=480 />
<img src="https://drive.google.com/uc?export=view&id=1602d6IOIyGec1IIVrRX4euBXbH0u0hwZ" height=480 />
<img src="https://drive.google.com/uc?export=view&id=1T7K-mNVmBz55gNZu8i_MAkoJkKD5Tc0I" height=480 />
<img src="https://drive.google.com/uc?export=view&id=1c2DNDJdXf4pNoRIoSEdhdB_40DpZqUkv" height=480 />
</p>

The application uses `wxPython` for GUI which has added advantage that it will look consistent with your desktop appearance.

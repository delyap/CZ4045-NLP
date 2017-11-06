import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

text = '''
How do I build a GCC 4.7 toolchain for cross-compiling?
On the RPi Advanced setup page, what does mkcard.txt do?
Which distributors are authorized to sell device units?
How can I use the GPIO pins as digital outputs?
Building Wireless Drivers for Edimax Wireless USB: EW-7811UN
Problems while booting
How do I install Arch Linux?
Necessary setup for a full computer
Is there a Linux From Scratch (LFS) ARM equivalent
Powering from a non-dedicated power source
Libraries for interfacing with the GPIO
How can I determine if a given touchscreen is compatible?
What is the simplest way to setup and run XBMC?
Are there any non-Linux operating systems available?
How can I control an RC servo?
What's the maximum SD card size that the Raspberry Pi will accept? Do larger cards give slower performance?
IPv6 connectivity
Can I use the GPU for calculations?
Why is my audio (sound) output not working?
How can I run Java software?
What type of television or monitor can I connect to?
Can I install Android?
Visual/audio status/activity indicators
Console unusable after running SDL app
How to set up swap space?
What happens if the power supply is 550 mA?
What are the overclocking capabilities?
What do I need to know when choosing a dedicated power supply?
Good lightweight web server framework?
How can I run the Pi on Solar Power?
How do I build a cluster?
Is there a JDK with a JIT compiler available?
Is it possible to run .NET code on the Pi using mono?
Is there a GPU accelerated Xorg server?
What's the maximum / minimum running temperature?
What comes in the box?
Can I use an airtight case?
What cameras can I connect to the CSI connector?
Can the Pi be potted in epoxy?
How can I enable the GUI on the Debian "Squeeze" Image?
Should all 'Linux-compatible' USB bluetooth/Wi-Fi devices work?
How do I enable Wake On LAN?
Is it safe to operate on any dry surface?
Can I install Ubuntu?
What's the quickest way to start playing a movie after attaching power?
Can I install webOS?
How can I reset to the factory settings?
If I plug my headphones into the audio jack, how do I control the volume?
How do I update software and firmware?
Emulation on a Linux PC
Is it possible to receive an electric shock by touching a Raspberry Pi while it's on?
How can I create a simple case?
Is it possible to mine Bitcoins?
Is it possible to use the GPIO to program a PIC?
How do I cross-compile the kernel on a Ubuntu host?
What kind of performance can I expect from using a Raspberry Pi as a webserver?
Is there a collection of teaching materials?
Building a waterproof case
Can the Raspberry Pi be used commercially?
Can I install Windows?
Can a simple cable convert HDMI output to VGA?
Simple Keyboard Configuration
What is the difference between Model A and Model B?
Is it possible to set up a Raspberry Pi as a wireless router?
Powering without using the micro USB
How can I determine when an SD card needs replacement?
Is it possible to immersively cool a device?
How to program a USB device with Debian/Python
What are the two long components on the board?
How can I keep system time?
Can I feed the device with a current rating that's higher than what's recommended?
Can I use Raspberry Pi as a USB peripheral device?
What kind of HDMI cable do I need?
Why do I have to `sudo`?
Will compiled binaries run on other Linux boxes?
Can I use the GPIO for pulse width modulation (PWM)?
How do I resize my debian partition?
Is it possible to control a SRAM module via the GPIO pins?
What is a typical boot time for the standard Debian distribution on a typical SD card?
How can I have multiple USB peripherals?
How does speed of QEMU emulation compare to a real Raspberry Pi board?
Is there anything I can do to improve boot speed?
Is it possible to dual boot from the SD card?
What cases are available?
How much power can be provided through USB?
What's the current draw and supply voltage tolerance?
Emulation on a Windows PC
How do I monitor and/or control the temperature of the SoC?
Can I attach a SATA controller?
Can I use PATA cables for GPIO?
Can I speed up web browsing on the Raspberry Pi?
Openelec/xbmc for Raspberry Pi No Addons Available
How do I install Google Chrome?
What could cause a failure to display anything on the HDMI output?
How do I install new software?
How do I connect/disconnect a flash drive from the command line?
Which Python IDEs/interactive shells are best suited to the Pi?
Can I use OpenCV?
Is there any workaround for Netflix compatibility?
How can I connect to a USB serial device?
What are the pros and cons of connecting to a VGA monitor?
How do I create a new user?
How can I resize my / (root) partition?
Where can I find the schematics and supporting design documents for the hardware?
How can I protect against intrusion and malware before connecting it to the internet (especially on a public IP address)?
How do I install packages from the AUR?
DSI video connector
Having launched X, can I shutdown without a mouse?
Why are there delays and input issues when using my wireless keyboard?
How can I install GStreamer gst-omx?
Definitive List Of Operating Systems
Using Raspberry Pi without a Linux OS?
Does the Raspberry Pi have Hardware Floating Point support?
How do I attach a GPS receiver?
GPIO-UART-to-Arduino communication
Which small displays have been confirmed to work?
How important is a case for the Pi? (And how to safely create my own?)
Can I run Concerto?
Is the BCM2835 (Broadcom SoC) proprietary to the Raspberry Pi organization?
To what extent can the device be used without a mouse?
Can't access shared libraries when running with sudo
Can the Raspberry Pi be used to construct a laptop?
Are there any expansion boards available for the GPIO?
How does memory-mapped I/O addressing work?
Can I program C within a nice IDE on desktop computer for the RPi
Can I switch mains devices on/off?
How to gain remote access without a Monitor or TV?
Can I break my Pi in a way that can't be fixed with a new SD card?
Why are certain resistors not populated on the device?
What are the dangers of connecting the Micro-USB through an adapter straight to the mains?
How can I solve sound drops over HDMI in Raspbmc?
How can I build a power switch?
How to get PulseAudio running?
Fixing issues with Powered USB Hub
How do I attach two monitors in a dual head configuration?
What password to use to log in after the first boot?
How do I use the Raspberry Pi as a Thin Client?
Is it possible to install VLC?
What is the optimum split of main versus GPU memory?
How can I control Lego motors?
How do I control the system LEDs using my software?
What SPI frequencies does Raspberry Pi support?
How can I use I2C to talk to sensors?
Is mame ARM compatible?
What advantage does the Pi-Face addon board bring to the Raspberry Pi?
Can I use a USB webcam?
How do I modify my Raspberry Pi to be powered over PoE?
Hooking up a Kinect?
How do I prevent the screen from going blank?
Boot from USB hard disk?
How do I load a module at boot time?
Is there an IDE I could use to edit code from a personal computer over the network in real time?
How can I use a bluetooth mouse and keyboard?
Why is the CPU sometimes referred to as BCM2708, sometimes BCM2835?
Connect Pi to an old laptop screen
Powering from my PC's USB 3.0 port
Is it possible to update, upgrade and install software before flashing an image?
I completely filled up my SD card - have I broken my Raspberry Pi?
Where is the rest of my sd card?
What do system LEDs signify?
Raspberry Pi fails to turn on
Non web-based Twitter Client?
Is it a good idea to mount /var in memory?
Can I power a USB SSD/HDD?
Audio over HDMI - hello_audio.bin works but not aplay
Why does python run relatively slowly?
Pi as a RFID Reader
Can I use a different filesystem type for the boot partition?
Adding a second Ethernet port
Can I use the Raspberry Pi as a second monitor?
How do I install an OS image onto an SD card?
How do I install Bluetooth for my mouse and keyboard?
How do I get the data from the serial port?
What qualities should I look for in a small, 7" or 10" monitor?
How do I get my bluetooth keyboard to pair automatically before I log in?
Running Headless - checking boot screen messages
Rebooting the system
Kernel panic immediately on a fresh debian SD card
How do I change the IP settings by mounting the SD card in another computer?
How to mount the EXT4 partition on the SD card from within VirtualBox
Using the Pi as a kiosk OR how to get VNC on Pi
Would E4rat or Ureadahead speed up the boot process from the SD Card?
Why does Raspbmc hang randomly?
Package browser to search for compiled software pre-install?
Can I install the Ruby Version Manager?
How can I control a 12V motor?
Has anyone got a Text to Speech engine installed?
How do I expand a raw disk image?
Why is `wget` hanging?
3d print host / arduino IDE setup/ 3d modeling
What is the power on state of the GPIOs?
Is my Raspi okay sitting on a magnet?
Why is my @ symbol not working?
How do I mount the .img files under Ubuntu?
Is Raspberry Pi resistant to nuclear radiation?
How can I setup a Wireless Access point or and Ad-hoc network?
How do I install node.js if my package manager doesn't include it?
Where can I find existing projects with instructions?
Can I use a DHT22 as a temperature sensor for my Pi?
How can the Raspberry Pi emulate a USB storage device?
How can I set the UART speed?
System time coming through SSH?
Using PCI or PCIe Devices
Why does my Raspberry Pi keep on rebooting?
How would I write a one-off boot script?
Are all of the devices the same?
Is the Raspberry Pi compatible with HDMI 1.4 specification with Ethernet?
What is the nominal GPIO Pin Output current?
Which locale should I select during the Raspbian setup?
Can I use Eye-Fi Wi-Fi SD card?
Is there a Skype replacement voice app?
Where is the GPIO header file ("linux/gpio.h")?
What are the different clock sources for the general-purpose clocks?
What file system format should I use on flash memory?
How to install lighttpd with php?
Outb in C to access GPIO
When will the Model A be released?
How to run Raspbian on VirtualBox?
Does Raspbian's repository have a browsable package list?
Boot from external USB stick / drive?
How to make raspbian load the i2c-dev module on boot up
Raspberry Pi won't Boot Just shows Black Screen
What to do about all the wall warts (AC/DC Adaptor bricks)?
How to measure temperature?
Can I install `libspotify` on Raspbian?
How to add custom loading screen?
What is Raspbian?
How do I determine the current MHz?
How to use a DS18B20 temperature sensor in my Pi?
Are there any emulators that run without X on the Raspberry Pi?
File config.txt with multiple lines is not working
Home cloud server with raspberryPI. What caveats I may get?
WiFi on Raspberry Pi & Raspbmc
What should be done to secure Raspberry Pi?
What is the highest performing hardware configuration?
ALSA volume ignored when beginning playback
Will router's USB port supply enough power for the Raspberry Pi?
Does anyone know of any kernel/driver programming tutorials?
Where is the kernel source for Raspbian's default 3.1.9+ kernel?
How do you protect the Raspberry Pi when you are carrying it about?
iOS on a Raspberry Pi
How can I connect an analog to digital converter (ADC)?
Boot without starting X-server
Where is the script for raspi-config stored in the FS on Raspbian?
Problems starting X
How do I install GDM on Raspbian?
How can I get Java Sound to work?
Easiest way to return to a known good state when overclocking
Recommended GUI toolkit for Python development on the Raspberry Pi
Is URxvt's slow rendering because of the limited RAM'?
How do I set up munin?
How free is Raspberry Pi?
How do I disable suspend mode?
Can anyone recommend a simple image viewer?
How accurate is Raspberry Pi's timekeeping?
How do I hard reset a Raspberry Pi?
Is it possible to run real time software?
Won't boot after removing and inserting the SD Card?
Why doesn't my external hard drive appear in /dev?
How to include RPi.GPIO in a python CGI script with lighttpd?
After writing an SD card image, is the remaining space usable?
How can I generate frequency / pulse signals?
Has anybody tried to Debug using JTAG/BDM?
How can I use an iMac as an external display?
What is the most practical OS to install long term?
How can I reformat my SD card to use it normally again?
How do you get wireless LAN working on Raspbmc?
Is there a way increase text size in Raspbian?
X11 forwarding with Xming over SSH?
What is the best way to access a DRM flash sites like Hulu or YouTube?
Live audio stream using FFMPEG
Raspberry Pi Drones? - Flying time?
Raspbmc stuck in reboot loop?
Custom Raspbian image fails to boot with "no init found"
How do I add 3G connectivity?
Why does my device shutdown when it goes to sleep?
How to exit omxplayer without command line?
Why does my wireless keyboard fail when I plug in my WiFi adaptor?
Is there a lightweight webserver that will serve dynamic content?
Is there a Linux image wich was compiled with -mfloat-abi=softfp?
What DLNA media server supports the most file formats?
How to attach an Arduino?
How do I access the distribution's name on the command line?
How can I change the bash screen resolution to custom values?
How can I record audio using a microphone?
Do I need to use a ribbon cable for GPIO?
Unable to obtain IP in AP mode
Why won't Flash Player on Chromium work?
Speed detector for amateur sports such as athletics or tennis
Can the Raspberry Pi be used as a media center?
How do I install Chrome OS?
Cannot rewrite Raspbian to SD
Raspberry Pi power source supply
How do I encrypt my Raspberry?
How is time kept on the Raspberry Pi?
How can I get and install Oracle's Java JVM for Raspbian?
How do I supply power through the GPIO?
No sound output in VLC
How can I compile Android applications?
If connected over HDMI will the 3.5mm audio jack socket work?
Ideal Handbrake x264 settings for encoding videos
continuous "mmc0: error -110 whilst initialising sd card" error at boot?
Are there any technical limitations when running hard-float binaries on a soft-float OS?
Re-using SSH keys?
Can I connect a 16x2 LCD screen to the 5V GPIO?
How do I read a button through the GPIO?
How can I connect a HD44780 based LCD?
Trouble powering pi from batteries
How can I change the RAM split?
How can I change the Raspberry Pi user password?
Why is my SD card slow?
How can I use a PC laptop or Mac Book to run a Raspberry Pi?
How to connect Raspberry to Grove Components?
Does the Raspberry run groovy?
Is it possible to control a small relay?
Does Raspberry Pi runs Minecraft and Netbeans 7.2?
Is there a good comparison chart for Raspberry Pi and similar enthusiast project boards?
Unable to grab image from usb Webcam
Can I use an Amazon Kindle Fire power supply?
X11 Connection Rejected Because of Wrong Authentication
External DVD drive won't open
Writing ARM Assembly code
please help -startx fails/hangs, finally returns error message "xauth: timeout in locking authority file /home/pi/.Xauthority "
How can my Raspberry PI start my TV?
How do I share my phone's WiFi internet connection with my Pi over bluetooth?
Starting ssh automatically at boot time
How long does it take to resize an SD card?
Problem with Python Games
Playing around with servers
Controlling the HDMI output via SSH
Empty desktop after typing "startx"
How to use Java to read/write data to/from the header pins?
Can I provide separate power to USB device?
Trying to get Edimax EW-7811UN wifi dongle working, but Pi reboots upon plugging it in
"packages have been kept back"
HDMI works in safe mode, but not much else
What are the software implication of changes in Model B, rev 2.0?
Would this touchscreen work with a Raspberry Pi?
Current state of I2C in Kernel and Kernel version in general
Custom operating system on the Raspberry Pi?
How can I identify from command line which board revision I have?
Can I use a One Wire File System through the GPIO?
Does the power supply need to be exactly 5 volts?
Why won't my Raspberry Pi overclock?
How can I visually identify which board revision I have?
Bluetooth Dongle not automatically Pairing with BlueSmirf
pre-compiled nodejs for raspberry pi?
What kernel parameters are available for fixing USB problems
Error in installing opencv on raspberry pi
Building Open CV fails on Raspbian on make at 61%
How to detect whether there is voltage between two points via GPIO?
Compiling for CPAN not possible on raspbian?
Play DivX 3 low motion too
How do I install MySQL on Occidentalis?
Can not capture video using OpenCv
Why does the Raspberry Pi need a MPEG-2 licence?
Button & 2700 Ohm Resistor?
CUPS Printer Stalls at "Sending Data to Printer"
How do you install a uncvideo driver for a Logitech C910?
Is it possible to upgrade occidentalis with latest wheezy upgrades
Is it possible to install Raspbmc without a wired internet connection?
Having trouble updating - how to fix problem with MergeList?
How to turn on a high current electrical device? (water heater)
Alternatives to Raspberry PI
Sudden development of "problem reading SD status register" error on boot. Cause?
Problems booting, any way to log this to a file?
Can Raspberry Pi reliably bit bang a 9600 baud serial and is there example code?
Can I make a full USB keyboard with Makey Makey + Raspberry Pi
Rpi running XBian. How to transfer files quickly over the network?
How to install Quake 3
Compiling Objective C with Clang
Interfacing with an RC receiver using PWM on the GPIOs
Where's my USB Disk / Memory Stick
Raspberry Pi Model B Revision 2, Max USB Output Power
chromedriver and selenium-webdriver -> unable to connect to chromedriver http://127.0.0.1:9515
Access the Raspberry Pi image on the SD card
Which CPU flags are suitable for gcc on Raspberry Pi?
Would systemd readahead be beneficial to a SD card?
Disable screen blanking in X-Windows on Raspbian
Using Raspberry Pi to control my AC via infrared
Filesystem corruption on the SD card
Enabling high resolution capture from web camera
Making a new image after changing a few parameter of Raspbian
How do I get the serial number?
Can I directly control a floppy drive from the Raspberry Pi's GPIO?
2012-09-18 version has no /etc/rc.conf?
The Manufacturing Cost Of Raspberry Pi
Cambridge University Raspberry Pi Operating system development Guide Questions
Breadboards is this possible?
sendEmail failure
How do I connect my printer to the serial GPIO pins?
Does Raspbian come with a remote desktop (RDP) client?
How do I measure the current power consumption?
What do I need to simulate traffic lights using LEDs?
Where are the WiFi config settings stored?
Do we need multiple versions of Python?
How do I reboot at a specific time?
Default shell for cron issue
Keyboard not detected
How do I force the Raspberry Pi to turn on HDMI?
Turning on and off a 3G (or any USB) port?
Is it OK to wash/submerge the Pi in water after Soldering
building kernel image (.img) including ramdisk
How to use Pi for standalone automation?
Wifi - bring wlan0 up on boot
Arch Linux downloaded file size is much bigger than actual amount downloaded?
SD card write speed seems to be 14 times slower than read speed
What is a accurate way to generate and decode IR signals?
How does a program check whether it's running on a 512MB RPi?
What are the min/max voltage/current values the gpio pins can handle?
Connect to USB via other means, not USB connector
Unable to start X after Cheese and VLC are installed
Is running a CGI server as root too dangerous?
PI Demo to prospective college students
Using Quickly to develop apps for Raspberry Pi?
What are the steps to get a Raspberry Pi issuing commands to an arduino-based 4-wheeled robotic rover?
How do I configure Raspbmc with a static IP address?
How do I compile GHC if it depends on itself?
Raspberry Pi not shown on the network
How to disable local terminal showing through when playing video
Female Breadboard Jumper Cables
Usb disk over network - performance
Run a script with a keypress
Checking sdcard for errors, unmount problem
Raspbmc network configuration file troubles
How can I protect software on the Pi for commercial use?
Trouble connecting my raspberry pi to to Arduino Mega 2650
Nano USB Wireless and HDMI to VGA
How to run Skype on Raspberry Pi
suspend for a fixed time interval
How do I set the memory split for 512MB model?
Wiring RGB LED's
Raspberry Pi stuck at splash screen
Alter dhclient to retry fetching IP address
Power RPi from same Powered USB hub as its Peripherals?
Accessing gpio pins using c program in raspberry pi
How do I install libxml on Raspbian?
Looking for a low-power, low-footprint WiFi solution
Controlling a Sprinkler Valve
What are S2 and S5 connectors for?
The assembly mscorlib.dll was not found or could not be loaded - what gives?
How to create an IMG file from USB but only using 2GB not full SD card size
Is there a way to get SoundPlayer to work or is there an alternative?
How can I stress test my Raspberry Pi
What are the capabilities of the GPIO pins?
How to enable transmission-daemon start at startup?
crosstool-ng build fails on ubuntu 12.04
Periodically losing connection to external hard drive
VLC Hardware acceleration
Why doesn't my Logitech K400 keyboard/mouse always respond in raspbmc?
Is it true that I should not use a Micro-SD card with a SD size adapter?
Errors with espeak
Raspbmc first boot without tv
Get High Quality Audio from HDMI
How can I deactivate the login password on my Raspberry Pi?
Connecting Raspberry Pi B to wireless network?
How do I wait for interrupts in different languages?
UART Output working on 57600 Baud but with 115200 only gibberish
Getting more than 26 GPIO pins
Are there any issues changing default username in Raspbian or Raspbmc?
Latest Raspbian 10.28.2012 perl issues
USB HID device only firing 1 event
How can i turn an GPIO to its alternate function?
Why isn't NTPd updating local time?
How to get more than one uart interface
Set up Pi, but nothing appears on monitor.
How can I zoom out the HDMI output in order to fit in areas of the screen that are being clipped?
What is the lowest power, most compatible, most compact usb wi-fi adaptor that works out of the box with the Raspberry Pi?
How to compile with qt for raspberry
Execute Python Scripts Via Web interface
How can I log into my Raspberry Pi Samba share from Windows?
Bad writing performance on Kingston sd card
X forwarding and GPU memory allocation
ArchLinux-SSH-First time boot
Guaranteed Power Supply
How do I increase the terminal font size?
Which chip to use to connect a Serial device to raspberry pi
I am unable to connect to a WPA2 Enterprise authenticated WiFi access point. What could be wrong?
How to change the umask?
Why do I not have a /boot/config.txt fle?
What's the Difference between Raspberry Pi and Arduino?
Powering Portable Rpi
How do I configure (hardware) the Pi as a NAS?
UART serial interrupt routine
Streaming live video to Raspberry Pi
Industrial applications
DS18b20 temperature sensor not listed
Porting Windows software
Problems with External Hard Drive - kernel: journal commit I/O error
How to install unrar-nonfree?
How to get better Audio quality from audio jack output
Is there an I2C Library
Running Headless - How do I create a boot sound?
How to play audio without being root (via sudo)?
pacman -Syu breaks Pi running Arch
USB microphone recording input and audio output
Does Someone Have a Recipe to Configure IPSEC/LT2P-PSK VPN for the Pi?
How can I install Debian from scratch?
Multiplexing 4-digit 7-segment display is flickering
Optimizing Apache, PHP and Mysql
Suitable monitors to use with Raspberry Pi?
Not getting enough volts - is the problem the power supply or the pi itself?
Strategies to deal with unpredictable power supply
I2C library for Mono/C#
What can cause libs to not be found on raspberry pi
Trouble with Wi-Fi connection
WatchDog Daemon not restarting PI after fork bomb
Where do Cron error message go?
Maximum amperage on power supply?
Oops I need runlevel 1
Can I temporarily remove the SD card while my device is turned on?
How to add ARM properly to the build target (Code::blocks)
Screen blank, does not boot
Raspberry Pi will not boot
Logitech c170 webcam not working
Custom recovery partition
Find the right device name of an SD card connected via a USB card reader
Raspberry Pi as a network monitoring device
Raspbmc + HDMI + AV receiver = screen changes resolutions
How can I change the frequency?
prevent pi from turning tv on
What to buy for my Pi to connect to my old laptop?
Replacing Raspberry PI HDMI Port
Samba login not working
Can I safely hook up my Raspbian device to the Internet?
SSH or Console in XBian1.0Alpha3
WLAN using Netgear WNA1000M fails - what am I doing wrong?
Start wireless network automatically on boot-up - how to?
Would this work OK with a Raspberry Pi instead of a monitor?
Transfer speed of download versus copying over the network
SSH to RPi without a network connection?
Touchscreen display from Chalk Electronics doesn't work
Auto-login with GUI disabled in Raspbian
What is the PREEMPT in the ssh message?
nanosleep won't sleep short time
Pi Model B quits working: Red PWR, pinprick green ACT LEDs
What kind of connector do I use for the Pi's GPIO pins?
Using 128bit integers in gcc
Configuring to read RTC at boot time
How to change the Raspberry Pi's hostname (in Raspbmc)?
What is breadboad? Is it a must for DYI projects?
How to listen to internet audio streams
What speed can I expect from the hardware-H264-encoding?
Pwr LED is solid red, OK LED flashes green once, no display
Using RasPi to send signal, for locking / unlocking alarm clock?
Raspberry Pi One Touch Audiobook *Updated*
can I use a disk larger than 320 GB with RPi?
How to use a USB 485 in the Pi
Infrared NodeJS
Running X11 without Window Manager?
Is it possible to connect an LED directly to the GPIO of the Pi?
Screen doesn't turn off
Record GPS tracks and convert to KML
Diagnosing dropped samples from a usb microphone
Can I use the Raspberry Pi to restrict web access?
Is it possible to restart a Raspberry Pi after OS shutdown?
How do I upgrade Raspbian?
Connecting blue LED (3.3V)
Can the USB ports be used to power the Raspberry Pi?
What Analog to Digital Converters Are Available For RPI?
How do I start the cron daemon automatically on Raspbmc?
Can I use ethernet to start Raspberry Pi for the first time
Will Raspberry Pi work with a USB Bluray player to play Bluray discs?
How can I boot directly into Google Chrome Web browser?
apt-get not installing software. Repositories are not updating
Why are Raspberry Pi's vi key bindings so quirky?
How can I make raspbmc remember my passphrase?
Which language should I use to provide dynamic web content.
How can dwc_otg.speed=1 be made to work
Install HTOP on Wheezy
Can the Raspberry Pi be used to send music to other devices on my network?
Video server for PS3
Wifi connection not working (using static IP)
Get GPS position and transfer them to server via GPRS
Is hard disk necessary for not over-using the sd?
How to automatically reconnect WiFi?
Running a Python script at startup
No video on HDMI?
Is Pi powerful enough for an oscilloscope project?
Setting up PBX using Astrisk and free PBX, with skype, PSTN (Talk Talk UK), and gsm gateway in the future.
Failed MySQL install (Raspbian)
Writing .img file to SD Card from a Mac
Raspberry Pi as sync device for automobile-based USB storage
Getting NPM installed on Raspberry Pi (Wheezy Image)
role of snd_bcm2835 on raspberry pi
Copy current SD image to larger SD card
How Viable is an RPI Laptop?
How to program pwm an arbitrary waveform to generate infrared stream
Is there any CLI alternative to xdiskusage?
Improper shutdown, now 3 flashes on boot
Black/white on composite TV
Upgrades possible on a Raspberry Pi
Unable to use apt-get: dpkg: unrecoverable fatal error ... is missing final newline
RPi rev 2 and USB powered harddrive
Forward mouse and keyboard input to X session
Is it possibly to have my pi play videos stored on my external hard drive?
How to get Pulseaudio working with Music Player Daemon?
How could I use a RasPi to control keg flow?
DNS resolution failure
How can I increase the size of the ram disk
Will a Raspberry Pi perform well with XBMC and many movies?
How to run a command with alias?
Cannot connect to internet - No DHCPOFFERS recieved
Not able to use VNC on my Raspberry Pi
Can I emulate x86 CPU to run Teamspeak 3 server?
How to install Deluge Client and Web UI
Can I use USB Dongle to connect Raspberry PI to internet?
External Hard Drive w/ Powered Hub will not mount
My USB mouse needs to be turned on when the pi boots - why?
How to prevent sd card capacity loss?
Get HTML5 videos to play in Chromium on Raspberry Pi
What are the kinds of (useful) things could I do on a raspberry PI?
Kernel panic, unable to mount root fs on unknown-block after restart
Can we put a Heatsink on the Raspberry Pi?
Can I get audio input through the GPIO
DIY External Powered USB hub not working
Raspbian Wheezy Audio
Could I turn a Pi into a DIY Chromebox?
Do I still need rpi-update if I am using the latest version of Raspbian?
Get CPU and GPU usage on Raspberry Pi
Why is a resistor needed for LEDs?
Raspberry Pi types in 'pi' but not the password 'raspberry' on login
Where does the Raspberry Pi get the time from?
What does rpi-update do?
Editing Serial Number
Can I safely connect a non-diode keyboard matrix to GPIO pins?
one power supply for raspberry pi and external HDD
Is it possible to extend the DSI connector?
How do I change/recover my password?
Streaming H264 with Logitech C920
How can I turn the lights off on my pi?
IRC/XMPP web-based chat client or BNC?
RaspPI/Debian Wheezy obtaining fixed IP address from DHCP server
Using a Transceiver with GPIO
underclocking to prevent overheating in the summer
External Hard-drive backing up using Time-Machine
Using USB as a slave
Powering Raspberry Pi and other USB devices through a single USB Hub
Raspberry Pi not booting at all with most images, but with some it does
i2c Group on Arch
How to run spotify on Raspberry Pi
TightVNC copy/paste between local OS and Raspberry Pi?
Why Isn't My Ethernet Working?
Remote Raspberry Pi 3D graphic using VirtualGL/TurboVNC?
RPi-compatible online backup service
Anyone have tutorials on how the Gertboard can be utilized? or demos?
Two problems with my pi (cron, and bootup w/o HDMI)
XBMC Rasberry Pi media center with harddrive?
184mb RAM after rpi-update
Can I use two raspberry pi to work together and faster?
Which GPIO pins are usable without any modifications?
Peripheral power from battery
How do I set up a windows NFS server to serve my media to RaspBMC [tutorial]
How to fix build error when building Linaro GCC crosscompiler crossstool-ng-1.17.0?
Installing Java but being blocked by Permission Denied
Could the raspberry pi be used for stimulus presentation in psychological experiments?
How can you update “Incredible PBX” for the Raspberry Pi without using the non-free, $20/year updater?
How to make a Raspberry Pi into a tablet?
What is a pull up resistor? What does it do? And why is it needed?
High Power USB Power Hub
SMSC95XX Ethernet Load Time
XBMC compile error under Raspbian
Can I use my Ubuntu desktop to cross-compile the GO language environment for my Pi?
Setting up a Ruby on Rails Server
transmission-remote localhost access does not work
Ethernet Suddenly does not work
Passwordless SSH isn't working
Make display go to sleep
Compile my RPi programs on my PC
Remote Desktop connection (RDP) to Raspbmc
Configuring the Raspberry Pi for Node.js
Benchmarking SD cards, read speed is identical
Cannot read input to SDA/SCL GPIO pins
Using several Raspberry Pi computers to create a household Internet of Things
Raspbmc only responds to bluetooth keyboard after restart
Raspberry Pi for real time video processing
Raspberry pi control GPIO with Haskell
Setting GPIO value on boot
Is it possible to view your network connection speed in RaspBMC?
Script Failed! : script.raspbmc.settings
How can I tell if I am using the hard-float or the soft-float version of Debian/Raspbian?
About 1 second from start is cut from each song played by XBMC
How to install the Java JDK on Raspberry Pi
Setting up Netgear N150 USB wifi adapter with RaspberryPi wheezy
Brand new Pi not displaying video
How can I keep my Raspbian "Wheezy" up to date?
Raspberry pi remote access active session
SSH "connection refused" on Raspberry pi - cannot find why
How to shut down RPi when running headless
Lost the start button on my pi?
Cloning SD card to different size SD card
XBMC settings sync on Raspbmc
How to stream Netflix on Raspbmc
What do I need to setup in order to push a video stream to the web
How to uninstall X Server and Desktop Manager when running as headless server?
Controlling many LEDs with few GPIO pins
ssh Over internet weird login
problem on sdcard
Is it possible to integrate RPi to a PC's GPIO?
RPi as a Sound Level Meter?
How can I share data between a network of Arduino and Raspberry Pi temperature monitoring stations?
How to install GNU C++ Development Tools on Raspberry Pi (using apt-get)
python audio bindings
Safe to power a raspberry pi from a 50W adapter
Pi stuck on wrong resolution
Addition to cron is not executed
How to use OpenGL (ES) through Python
How can I use a PQ Labs multitouch overlay with the Pi?
Special OS for a special device
How can I start rpcbind -i on startup?
Powered hubs, backfeeding and safety
How can I build MongoDB?
Keeping System Time Without Network
Model B without soldered connectors?
How to configure Django/Apache on Raspbian?
Control Hardware PWM frequency
Program that autosaves music position on shutdown?
Lightspark can't be installed
Options for mounting a hard drive to lessen the chance of data loss?
Need help with (ambitious?) project
Pi for Google+ Hangouts
Can I run Selenium webdriver using Firefox as the browser?
Resize image file before writing to SD card
Networks drops, and freezes
WD Passport disconnects and remounts itself
Install very basic linux
Xbian with BerryBoot
Electronics manual for noobs
Why won't my raspberry pi boot after reformatting the SD?
Webcam disconnects after a few hours of running motion
Is it possible to run Raspberry Pi's HDMI output to a USB port on another computer to see the video?
Make fsck run without intervention after non-clean shutdown
Using an old laptop keyboard with Raspberry Pi
Game platforms emulators on Xbmc/Openelec
pwr light is red
Raspbian source code
Light Controller System Help - What should I use in my build to individually control multiple lights?
How much energy does the raspberry pi consume in a day?
What application (and options) should I use to get terminal access to my Raspberry Pi over a USB/serial cable on Linux?
Cannot Expand FileSystem
Connect raspberry pi to my computer via serial port
Anyone knows how to link Raspberry pi to Kinect camera?
Unaccellerated DVD playing
Having problems with RPi and DHCP
cannot login anymore
How can I run a MONO application/program on boot?
Where is the bottleneck of web browse speed on raspberry pi?
trying to build file with gcc getting several errors
Falls off network ("Destination host unreachable")
Detect that a python program is running on the pi
Running on read-only SD card
I shut my Pi down last night - now it doesn't finish booting
Lack of 'Raspi-config'
Multiple keyboard and input languages
Can't get Raspbmc to browse samba shared folders
How do I run a background service written in MONO?
Is there some kinda serial number available from OS level?
How do I prevent Motion from using up the entire SD card?
Hidden Wi-Fi won't connect
How to check for keyboard input, while waiting for switch input?
Can I read the amount of light?
Would you recommend a Raspberry Pi as a remote file backup device?
Static DNS with DHCP on Raspbian
Is hardware deinterlace possible?
javac: command not found - after installing Java
GPIO input connected to garage door button
Create a Windows readable/writable FAT32 partition
Gyro questions numbers not staying steady at stand still
Custom firmware on Raspberry Pi?
Is it better to use NFS or SMB to serve files on a LAN using the Raspi?
Java IDE for Raspberry Pi
Controlling a 12V RGB LED strip with the GPIO
Gert Board voltage on J7 is nearly 4 volts, is this a problem?
Raspberry pi maximum relays that I can connect
Installing dependancies
How can I get my Pi to check/read email to trigger an event?
How can I improve boot time on raspbian?
Does Arch come with a GUI preinstalled?
Performance difference Raspbian versus Gentoo
Hadoop on the Pi
Permissions on /dev entries
How long can a RaspberryPi run for on 4 or more AA batteries?
PIR Sensor with RPi
Can't get an IP for wlan0
Problem installing Net::SDP
Is XBMC an operating system?
Expected User Limit of IRC Server on Pi 512 MB?
How to map Caps Lock key to something useful?
How can I disable raspbmc's firewall for SSH access?
How to detect objects with minimal weight?
Raspmbc send CEC commands without CEC adapter?
Bluetooth connection
Can't update /etc/rc.local
I can not get my WiFi connection to work
mmc0: Timeout waiting for hardware interrupt trigger watchdog
WiFi connection gets dropped quite often with Edimax EW-7711UTn
OpenELEC as Printserver
How do I change the editor used by visudo?
What's the right way to run a python script as a daemon (service) in raspbian (or debian)?
Circuit to safely power-down Pi
Motor Shield Needed or not?
Webcam issue apparently not related to usb system
Why do I have to refresh the network interface to get shared ethernet working?
Can I use RasPi as a thin client to access LOB applications on Windows Terminal Server?
Relay and GPIO Question
Battery pack for model B RPI, Thoughts?
Segmentation fault
How can I cut power coming out of the Pi's USB ports?
How to get tomcat running on Raspberry Pi with ArchLinux?
How to automagically have yaourt / makepkg add the armv6h platform to PKGBUILD?
Answering machine with Raspberry Pi
Can a Raspberry Pi be used to create a backup of itself?
OMXPLAYER black screen after video for 1 second
Raspberry Pi disconnects from network
Return to xbmc from console
motion doesn't work without HDMI display plugged in
Usb driver development in raspberry pi
Using two screens at the same time
Copy existing Raspbian installation to smaller SD card
Trying (and failing!) to boot a Pi for the first time
JAVA GUI application on Raspberry Pi with touch screen
Time and date in Raspbian vs. OpenELEC (one works, one not)
USB Sound card found, but no output
Why is my Pi running at 700MHz all the time?
How to open a terminal at startup?
How do I configure a USB WiFi Dongle from the command line?
Redirect audio to another AirPlay device
Does Raspbian come with Perl?
why raspbmc constantly writes (or reads) from external disk?
Cannot find debian mirror while installing Raspbian
External power for USB HDD
How can I mass-provision a lot of RPi's at once?
Raspberry Pi Video Output
Why does my Pi become unreachable from other computers but is still connected to the internet?
Electrical characteristics of GPIO
I2C: Raspberri pi as a Slave
How would I use right click on a single click mouse
How to compile C files in terminal
How to Remap the Raspbian “Wheezy” Keyboard
Wifi - No Adaptors listed in WPA_GUI
How to unzip Minecraft PI edition through terminal
Why are my changes to cmdline.txt ignored?
How to overclock the Raspberry Pi with Kali Linux?
top/htop not showing CPU usage of kernel processes
Power USB hub and Raspberry Pi with the same PSU
U-BOOT and tftp (network) crashes or blocks during uImage download
How do I set up a storage device that is only "on" when used?
Connecting to network through Ralink Wi-Pi adapter
Why am I getting far slower internet on my Raspberry Pi when compared to my Mac and Windows Computer
How to wall mount the Pi and its monitor?
Wifi Dongle - Cannot ping beyond intranet, works with Ethernet!
What is the point of the spikes on the Raspberry Pi?
OpenCL / GPGPU programming coming soon?
stopping RaspPi / raspbmc from auto changing source on tv
Keyboard, mouse & wifi dongle, but only two USB ports
Capacitor C6 dislodged
lsusb command outputs "Illegal Instruction" (part of making sakis3g work)
How to get the Raspberry Pi's IP address for SSH
Can the original StarCraft be played on LAN with a Raspberry Pi?
Bluetooth Dongle and Macbook Keyboard
Update transmission
Video blinks in and out
How to use SSH out of home network
dconf-gsettings-backend:armhf' contains empty filename
Raspberry Pi Raspbian Web Kiosk Virtual Keyboard Solution
Installed pyusb, still: 'ImportError: no module named core'
Commands to "simulate" removing and re-inserting a USB peripheral?
Pi powerd OBD-II Computer
Can SSH be accessed over a VPN such as Hamachi
Installing node with nave
Mopidy and sound quality
Is there any way to hide my email when deciding to become a dev on the raspberry pi store?
Why does opening startx disconnect my ssh session?
How to make shairport play nicely with mpd?
Raspberry Pi LED confusion
How does apt-get work?
Wheezy: How do I create a .zip on the Pi?
Preventing an ntfs partition from ever mounting
Should I buy a Raspberry Pi?
CUPS is too slow, how can I make it faster?
Raspberry Pi boot stops right after the rainbow splash screen
List of IDE's for the Raspberry Pi
Raspberry pi with webcam, motion, and FTP
Can I drive a Solid State Relay directly from GPIO?
Safe way to shut of Pi without keyboard, access to command line ,etc
Fix broken plastic on SD Reader
how to disable raspberry pi power management?
Raspberry Pi Inaccessible Screen Area Problem
Location of berryboot's config.txt
How can I determine which OS image I am running?
Get PI's temperature using C
Auto-refresh for Midori
What is the Path and Name of a runtime executable?
What is the difference between the POP3 and IMAP email protocols?
Will not boot, black screen only
Can I run Mac OS X on the Raspberry Pi?
Could you write directly on an external hdd drive with owncloud reading the files?
QEMU Virtual Machine - Win 98 Disk Error
Open multiple "Terminals" without GUI (startx)
Get a static network IP on Raspbian
Can I have Google Now running on Android in a Raspberry Pi?
Thermal Management in Raspberry Pi Clusters
Is my Raspberry Pi permanently damaging SD cards?
How to supply redundant power to a Raspberry Pi from two PC usb ports?
CEC wake up command
Raspbmc: How can I open the terminal?
Battery Supply Question
cannot resolve hostname error
How to successfully emulate RPI on OSX?
Easiest way to control a pis power supply via usb
Troubleshooting TP-link WN725N wifi dongle problem
Playing audio files with Python
Display a test pattern by writing the Frame Buffer and then clear it
Building a case for a server
Control robot over WiFi
Does dust accumulation on raspberry pi causes heating problem
Raspberry Pi Live Boot or Read Only Distro?
Console cable to iPhone / iPad
ssh not working
Deluge have no init scripts?
Level of Hackability of raspberry pi
How to change user pi sudo permissions; how to add other accounts with different permissions?
MMA8452 I2C module
Create a Raspberry Pi webserver with a domain name
Voice recognition
Static local IP/gateway config on startup issues
Can the raspberry boot to an LVM root partition?
How do I power down my Pi if I'm ssh'ed in?
Image of a 16Gb card containing unpartitioned space at the end: Truncating possible?
SSH Permission Denied, Please try again
Pi not starting up, no light
What should I take into account when trying to decide between an Arduino Uno or a Raspberry Pi for my application?
What SSH server does the Raspberry Pi use?
Using Raspbmc as an OS
How can I reset network settings without a network connection?
Setting up Bluetooth dongle
How do I make my raspberry pi webserver public?
How can I stop Raspbmc from removing my directories at reboot?
How to utilize Raspberry PI in daily life task?
Network Security Toolkit on a Raspberry Pi
Using the Raspberry Pi as a router?
Setting up the Raspberry as a data logger
What commands do I use to make Bluetooth discoverable on RPi running Raspbian
Raspbmc boot failure on fresh install
Varying power output using RPI
Raspbmc - how to set up keyboard layout *after* first SSH login?
How to set my Raspberry Pi to boot into the GUI?
Raspbmc - can the command-line be accessed from within the GUI?
How do I start to to play videos automatically while boot?
Big Endian distribution for the Raspberry Pi
Advice on RPi taking high res pictures at timed intervals
USB to USB cable connecting PC to Raspberry Pi
Running "sudo dpkg --configure -a" fails
Raspberry Pi USB power from 5V S-ATA from inside 3.5" HDD Enclosure
Auto-start X application from read-only file system
What is the difference between CEA and DMT?
raspberry pi and Scream out loud - 110dBA fixed tone Siren
Raspberry Pi apt-get update/upgrade on Raspbian hangs?
Time a GPIO input
Controlling PI's GPIO over Wifi (WebIOPi alternatives)
Unable to connect to Raspberry Pi over the network
Python Synth with Raspberry
PHP to execute Python scripts for GPIO
Forcing HDMI Audio Breaks Resolution?
Is it possible to power the RPi by re-assembling the ethernet port?
SSH and rsa authentication on mpich2
How to restore the original iptables configuration?
What is the mmcqd process?
Is it possible to host Discourse on a Raspberry PI
How does Pi keep track of time interval?
NAS with a cluster of some raspberry pi
Is it possible to detect input voltage using only software?
USB Hard drive mounting as Read-Only
How to printscreen on Raspberry Pi?
Why does raspbian use ext4 for it's rootfs with journaling enabled?
What is the "AP" on the Raspberry Pi, from the FAQ?
Remote Desktop With xrdp
How can I stream H.264 video from the Raspberry Pi camera module via a web server?
Random GPIO values when ribbon cable is connected
Configure the port knocking server (knockd)?
Creating boot script for webcam
Ethernet light doesn't go on
Running Plex server on Raspbian OS
Which key types the "|" symbol?
How is memory split by CMA?
PI as a VPN router for local machines
Recover files from broken sd card (no boot)
Is it possible to install update for raspbian onto and SD card via my Mac and install it on the rpi later
Which platform is best for project? Raspberry vs Arduino?
Controlling 400 LEDs from a raspberry pi
How to get a good overview over used space?
How can I use usbip-host?
SSH not working when connecting from local network, but working when connecting from external ip
Cheapest way to controlling multiple power sockets (lights) through Wi-Fi
Camera Module Turn LED Off
How can I tell if my Raspberry Pi supports H.264 hardware acceleration?
Has anyone manage to drive a HD44780 LCD using a 74HC595 shift register?
Can berryboot detect an already-existing OS on a USB drive?
Unable to get static IP address to work with wlan0 (WiFi)
munin-node plugins : VCHI initialization failed
Raspberry Pi to iPhone Audio Streaming
Raspberry Pi doesn't boot
code stops after few hours and raspberry py freezes. (pymodbus + rs485 + raspberry pi) python code
Raspberry pi and shift register
Bash Script with GPIO fails - what am I doing wrong?
Accessing a USB drive after start up with Python
Setting a static eth0 ip
i2cdetect doesn't catch ANY address. How can I tell if I2C working correctly?
Raspberry Pi not reachable via its hostname in LAN
On Raspbmc, play 1080p video full screen on 1080p TV
GPGPU simple example
Display Powersaving Options (Pi powered on display USB)
Prevent libsane.so.1 from being overwritten during update
Use SSD as RAM?
Raspberry pi HDMI Output multiple screens
Thermostat using wireless relay
No output on HDMI display, but it works on Video
What happens when we connect the 5V GPIO output with the Ground, why does it restart?
Raspberry PI and fingerprint scanner
Apt-get fails because of libqtcore and libqtdbus4
Home Automation in an apartment
Play video using XBMC in raspbmc displays OpenGLSpectrum instead of video
Playing various movie file types on Pi
Suitable power supply for DC power through GPIO
How does the RF/FM GPIO transmitter hack work?
How to configure serial port settings of /dev/ttyAMA0?
Safely Logging Data on Raspberry Pi
Power light but very dim act. No display or network output?
Sending Commands from PC to Raspberry Pi via USB
Are there any tiny screen I could use to make a wearable RPi?
RF Module input is random
How to get an SPI Analog-to-Digital (MCP3204) working with the GPIO?
NOOBS won't start
Raspberry Pi and realtime audio effects / digital signal processing?
What is the best OS for XBMC on Raspberry Pi?
SSH from Android to rPI using USB?
Setting up an IP Camera on raspberry pi
What can I do on a Pi with an Infrared sensor but no Arduino?
How to add unlimited Crypto-Strength to Java jdk8 for ARM?
Is the USB-Port generally faulty with the RP?
Can the Raspberry Pi overheat in a small space?
Powering the raspberry Pi from USB + microUSB, is it safe?
Linux machine broadcasting its own network while connecting to a different network
Using android phone's sensors on raspberry pi
How can I harden Raspbian to boot unattended after unexpected shutdown?
Log says I can't allocate memory, but I have more than half of my memory free
How can I check for internet connection before running /etc/rc.local script
HDMI Video to TV shuts turns off and right back on every few minutes
Is is possible to remotely SSH into a RPI from iphone/ipad (using iSSH) when outside a wifi network?
Can I use this bridge with Raspberry Pi to drive 2 servos and a stepper motor?
Raspberry Pi constantly faulting
Is it normal to read a connection between pins 2 and 4 of a GPIO breakout board?
Internet always cuts out
Powering a PI from 12V
Raspbmc - install missing man pages?
Is there a dashboard for Raspberry Pi?
Default content of /etc/dhcp/dhclient.conf from Raspbian
How do I restart Raspberry Pi from a remote system?
Play 2 sounds simultaneous HDMI + analog
How to output digital value to multiple GPIO pins as one port?
Connecting to an LCD via I2C
WiFi configuration on Arch Linux ARM
Can executable code be run from the SD card without a bootloader?
Are there any sites dedicated to developing expansions for the GPIO port?
Will a 2.1 Amp MicroUSB charger be OK for the RPi?
Internet access via 1 of 2 Network interfaces
How is internet bandwidth allocated in a customized router using Raspberry Pi?
How to set up a wireless AD HOC network if there are no other networks are available
Starting Python Program with Screen Automatically
Start and run a Python script at boot and use Cron to make sure its still alive
Setting the time on the raspberry PI - one day out - what gives?
SNES usb controller adapter - some input not recognized
Use of ZRam module in Raspberry Pi Kernel
Does anyone know of any Accelerometers that are easy to use in Python
Which database to use with node.js and raspberry pi?
How can I lower the usage of CPU for this Python program?
How can I stream music from a different machine?
How to play my music on my RPI outside my local network
Will Terminating an SSH Connection Also Terminate any Program running?
Use the Raspberry Pi as a Git server
Relay working at 3.3V for RPi?
Wayland/Weston freezes
NOOBS recovery password
controlling two motors with an L293D
Effect on ping response when using Raspberry Pi as firewall (lag, jitter)
Can RPi be used to stream internet TV shows from web pages?
OMXplayer pexpect loop screen blacks out
Keyboard incompatible with Raspbian
Can I compile R-Pi programs (Qt) on R-Pi itself?
How to share desktop's connection with Raspberry Pi?
unable to login in raspberry.. please help me out
UART sends but not receives but works if tx-rx are bridged
Stuck in a rebooting loop
Emulating "Baking Pi"
Network monitor by Process
Why is my disk space suddenly full?
Run startup application as a specific user
Wireless surround sound using Raspberry Pi?
Raspberry Pi as an Email Server
Reading common food thermometer probes
Is there a pre-built LAMP server image for the Raspberry Pi?
How to get the exact clock speed at the raspberry pi is running?
Unable to setup bluetooth dongle
AirPlay on Raspberry Pi
Problem with connecting to Raspberry pi after setting a shutdown
Raspberry Pi HDMI no signal
How to correctly install the python RPi.GPIO library
Detecting TV power on/off without CEC
Trying to image SD card not working: Read-only file system
How to force NTPD to update date/time after boot?
SSH is unreachable for the second time
My server hostname doesn't work?
I cannot connect to the internet via ethernet (Bell Canada Fibe Modem)
btrfs root filesystem on raspbian
Wifi connection lost after about 12 hours
A good sensor for a Bed Occupied detector?
Using motion to save single images
Running script in motion
replacement for SD card
how can I host a web page on Raspberry pi using Ad-Hoc network?
External hard drive power down?
fswebcam not displaying images properly
How to make an image (.img) from what's on the SD card (but as compact as the original one)?
How to install last Scipy version on Raspberry Pi
SSH - connection timeout when connecting
Blank screen after installing Raspbian
How to connect Raspberry Pi to my monitor?
Install software on raspberry pi offline
Network interface settings on startup
What software library is avaliable for RPI camera module?
Can I make my Pi shutdown safely in the event of a power outage?
Can I use a 5V battery as a UPS?
Raspberry Pi Remote SSH Connection
uTOLED-20-G2 display compatibility
How do I connect the Raspberry Pi to a TV with limited input options?
Keyboard works in NOOBS but not Raspbian
ir filter on the camera
How to mount Time Capsule from Raspberry Pi
Choosing Python v2.7 instead of v3.2
GPIO input and output levels
Required SD card capacity
Controlling 240 volt power supply (via Relay) with Raspberry Pi
Problems with changing mac-address of Raspberry Pi
Parts on a Raspberry PI
Unable to reliably connect Pi HDMI to Motorola Atrix Lapdock
Use same power adapter for RPi and USB Hub (For bundling)
Resetting usb device from terminal
Use smaller space when i have expand it?
Why is the hostname Raspberry when I search my network?
Arch Linux ARM doesn't boot to desktop
Max MB/s down from BT Sync?
Disabling USB ports
What is so special about Pi?
Is it possible to install and configure a Raspberry Pi without a wired keyboard or mouse?
One-way file-transfer from PC to Raspberry Pi
How to install it?
Meaning of cmd param in write_i2c_block_data
What BIOS does Raspberry Pi use?
How can I ensure all data sent from an Arduino is received by a Raspberry Pi?
How to stop program running on startup?
Disable LAN9512
SSH with Putty to RPi: Network error: Connection timed out
Can Python control normal Minecraft, or only the RasPi Edition?
How do I check the MD5 for a file I downloaded on Raspberry Pi?
Battery powered Raspberry Pi
Why does my SPI-using program in C give varying results?
Networking : DHCP/static : connection to LAN but not to internet
GPIO Interrupt debounce
peerguardian / moblock installation on raspbmc
Enable monitor mode in RTL8188CUS realtek wifi USB dongle
Arm timer in kernel module with precision less than microsecond
Can you transfer data through the microUSB?
SSH Not working for additional users
What is the MTBF of the Raspberry Pi Model B?
Record raw PCM from microphone
Stream PC screen to Raspberry Pi
Sharing internet through ethernet port?
isc-dhcp-server install and run problem
Resize file system on OpenELEC
Lighting a LED slowly with GPIO
Controlling process priority/Stepper motor missing steps
Write an OS for Raspberry Pi in C
SDL 1.2 for use with C++ on Raspbian?
How do I download the Python libraries without a direct internet connection on my Pi?
Can RasPi run GNU Radio and OpenBTS?
Unable to access my Pi nginx server from outside
Raspberry PI freezes
Can I install Git on Raspbian?
Homebrew Power Supply for Raspberry Pi
Apache fails on startup
How do I get the uLCD-43PT-PI touchscreen working?
How do I display the temperature from the internal sensor on a HTML page?
Raspberry Terminal and SSH not working
How can my Raspberry Pi turn on/off my Samsung TV
Android 2.2 won't start
Boot off Ext4 Memory Cards
How to trigger GPIO event using an active infrared sensor
Raspbmc UI flickering, virtually unusable
Which available operating systems for the Pi come with OpenOffice and paint programs?
Will I need to enable expand-rootfs if I use NOOBS?
Execute script on start-up
When does the OS kill an application?
Ping a website and have an output turn on if online/offline?
Rpi power timer
I think I've deleted the default pi user
External Wifi not properly connecting to AP
Can I power Raspberry Pi using the mini USB to USB cable connected to a computer?
How do I run a python program as a process in the background?
Raspberry Pi Air gap
How to Encrypt External Hard Drive so It Can be accessible only from XBMC on Raspberry PI
Pi have to ping other host first then other host can see pi
Kernel module assembly output
Auto-login into LXDE and auto-start video-player (omxplayer)
1080p Pygame Output?
Will iOS, jailbroken or not, work on RP Model B?
Adding 5V fan to GPIO 2 and 6
Does Raspbian come out of the box with some GPIO C library?
Connect PCI boards to RPi board
RPi Accepted Waveforms from power source
Power USB Hub from "Mains to USB" adapter
Finding cards optimized for random read/write
Setting up WiFi and Ethernet
What tools can I use for a Basic C++ Interface on Raspberry Pi running Rasbian
Use cellphone screen as monitor
Multiple temperature sensors with a Raspberry Pi
SSH session closses on TAB key
Overclocking via command line
Javac with Oracle Embedded SE on Raspberry
How do I find out if my Pi's warranty is voided?
How do I display images without starting X11?
Enabling audible terminal bell/beep on wheezy
Logging using SSH key for password less login is not working in Raspbmc
What software can I use on my pi to take a screenshot?
Memory Problem; I can make new files and install new software but can't download
Watching YouTube videos in command line failed
how to stop /etc/profile.d/ from loading on startup
Copy files from OSX to/from Pi
Stream linux sound output to Raspberry Pi
Raspbmc with usb audio
Default kernel preemption vs real time patch?
Preparing SD card for use on the Pi
Software PWM as kernelspace module?
What type of motor and speaker would be suitable for a DIY: Making a Pi-powered baby mobile?
Learning Linux driver development with Raspberry Pi
JavaFX Jar doesnt run properly
How to drive a high voltage (30V) signal from Raspberry Pi?
Forcing resolution on display :0 when HDMI is not connected
Hosting my own domain on Colo Raspberry Pi (Soc)
Cannot mkdir unless sudo is used
How to break a 5v circuit using raspberry pi
How do I get tshark to see my wireless USB dongle?
Watchdog timer waking-up Pi after shutdown
Confused about GPIO
Is there a way to make a regular GPIO pin into a Tx UART pin?
While using startx I get the response 'Error locking authority file'
RaspBMC plays some avi files but not others
How to change the default governor?
Floating values from GPIO pin
Raspberry Pi Posts (successfully I think) then nothing but a cursor
held broken packages
Toggling a GPIO pin set as output
Raspberry Pi as surveillance cam?
How to change focus on Raspberry Pi camera?
Ethernet not working on newest version of Raspbian installed with NOOBS
Boot raspberry without SD card slot?
How to make the Pi an acces point
Wifi works, ssh can connect, but cannot connect out to the internet, cannot ping internal machines
RGB LED resistance calculations
I would like to play 3 different video clips selected by 3 different hard-wired buttons
Will the GPIO return data that is accurate out to .001 seconds?
Why is the 'file transfer' button greyed out on TightVNC
Boost Site Speed - Raspberry Pi node.js server
Unsoldering elements from from rpi -> can't get solder to melt. Any tips?
Is there any reason to use multiple ground pins on the P1 header?
Does my RPi uses video RAM for tunneling X over ssh?
USB WiFi adapter being detected but no connection
RPi extremely slow download speed
How to install a Lisp compiler?
1080p Raspberry Pi on Debian/Raspbian/XBMC
Software for displaying animated gifs?
How do I setup swap on Raspbmc?
Using Raspberry Pi as VoIP phone with USB sound device
Lightweight and/or legacy distro for FOTRAN hackery?
Creating an HDMI Pass-Through Connection
How to set up "kiosk" mode in Raspbian?
Maximum, demonstrated SD card durability
Highest current raspberry pi can take from usb
eGalax touchscreen
Tutorial Guidance - Writing Web Apps for my RPi
Share Internet Connection from Windows 7 to RPi
Raspberry Pi and BMP085 (I²C)
xcalib not working on Raspberry Pi
How to use Android mobile as Remote control for wifi enabled raspberry pi car , without using any access point/wifi router
What's the difference between `wpa-roam` and `wpa-conf` in the /etc/network/interfaces file?
USB is not working properly (playback and record are too loud?)
How do I reset a USB device using a script?
How to make Raspberry Pi suspend to RAM?
Using Transistors and the GPIO, can someone please check my math?
How to Wake the Raspbery Pi Display Without Disabling The Screensaver
Harddrive detected as 13fd:160e Initio Corporation instead of 1058:1010 Western Digital
RetroPie not detecting my ROMs even after tweaking settings in ~/.emulationstation/es_settings.cfg
How can I reset a USB device using command line utilities?
How to encode DVDs using the Raspberry Pi
What is the maximum current the GPIO pins can output?
apt-get installation doesn't work on Raspberry Pi
Which would be faster? Computing 2000 MD5 hashes on the fly or cache them on SD?
How to install LXDE on raspbmc?
Wire Raspberry Pi to 7'' TFT LCD?
Tether Android Phone to Raspberry Pi (for MMS/SMS)
What is the Raspberry Pi?
Best source for raspberry pi sensors and accesories
Larger Touch Screen Displays
How do I simulate mouse right click from Keyboard?
Stopping (orphaned?) Minecraft server properly
How can I monitor power usage via the CLI?
how do I enable JPEG support with PIL?
"cannot open display" with PuTTY
How to display a graph from temperature, humidity readings?
how can a movable Rpi(B) can follow another movable Rpi(A)
ITEAD PN532 NFC Module with Raspberry PI
How to connect to wireless network using Belkin N300
I accidently deleted my taskbar - how do I get it back?
HDD without external power is working. Is this dangerous?
Roadmap to leverage RPi to do signal processing from 4 inductive loops and data transmission in an outdoor environment
Latest NOOBS goes into panic after rainbow splash
Reading values from XBee Pro S1 via Putty
Why won't dnsmasq's DHCP server work when using hostapd?
Can't get rPi to boot with Raspbian and/or NOOBS
How to known if an ARM library (.so) is compatible with the raspberry PI
How do I automate removal and re-enabling overscan as I move the pi between HDMI and TV?
nmap variance between releases
USB-LAN adapter over USB hub
GPIO: Why wire button to ground rather than +3.3v?
autostarting program with rc.local, stuck on startup
What is the best way to increase digital I/O lines on Pi?
Make a portable device based on Raspberry Pi
How to access the RPi root ext4 file system by inserting SD card into a different computer?
Automatically start python program at start-up
Routing http traffic to different http adresses depending on request url
Issues playing back wav files with pygame
How to setup openHAB to work with a RaZberry ZWave binding?
Long (30 to 50 foot) USB power only cable
How to install GNUradio on raspberry pi?
How many volts does the Raspberry Pi supply out to the GPIO?
Are there any good Raspberry Pi distributions that load completely into RAM?
How many volts can you safely connect to the Pi?
tightvncserver - show the same screen on hdmi and vncclient
Streaming games from PC to RP
Difference between Ubuntu Server and Raspberry Pi
Microphone for a project
How to regulate current when peripherals or servos draw a large current?
Is the Raspberry choice for SD Card a irresponsibly one, or there are optons to make it serious?
Raspberry Pi/"Arduino" communication
USB to USB mimicking Ethernet?
Control WS2801 with Raspberry Pi
How fast is GPIO+DMA? Multi I2S input
How do I program a serial EEPROM IC using a raspberry Pi?
How to build/install usbip?
I have a 16 GB SD card that is now only 55 MB. How do I get 15.945 GB back?
Using NOOBS, no keyboard
Static IP Failing for wlan0
Trying to execute 'a.out' returns "-bash: a.out: command not found."
Using the Raspberry PI as a Replacement for Desktop Browser
Struggling to setup Dynamode wifi USB on OpenElec
Connecting Raspberry Pi to another device via USB port
Disable DTR on ttyUSB0
Update Webpage from server event
After reboot, my RPi is one hour off -- How to adjust for Daylight Savings problems?
5 Ghz Hostapd device for RPI
How do I run a single line of code (with sudo) on boot up?
some config help: lighttpd and fastcgi stuck on running the same python script
What is the best container to put h264 into and how do I do it?
Analog input to the PI
Enclosing the Raspberry Pi in a Plushie
Raspberry Pi setup
Remote communication with home server
What is an easy way to electromagnetically shield a Pi?
Do I overclock my RPi without voiding my warranty using RASpi-Config?
PWM input in Raspberry Pi
How can I automatically update the hwclock with NTP when I have internet connection
"Cant open display" error message
PulseAudio sink stuttering
Can I launch a script remotely with ssh and leave it running
LCD with RTC and GPS
Raspbian: mount: / is busy (tried to remount sd card as read only)
/dev/ttyUSB0 missing after restoring from backup
INIT: Id "1" respawning too fast: disabled for 5 minutes
External power of raspberry pi without going through GPIO
Turns off when touching test points
Subtitles embedding on video files, without re-encoding needed
Howto transfer internet-stream to raspbmc?
Camera gets stuck on
i2c data understanding
Raspberry (HDMI) to monitor(VGA) Does a cable work?
Raspberry PI usbmount, dmesg: “READ CAPACITY failed” & “Asking for cache data failed”
How to wirelessly transmit data in between Raspberry Pis?
Connecting to a school network
How to Stream Media from Raspberry Pi to iphone/ipad/android?
Unable to use SSH to access Pi over local network
Linux - Windows 8 - Samba - Can see dir and contents but not create
redirect console output from PI to my PC/laptop
How do I tell which version arm cpu on my Pi?
Perl Script doesn't update file
Can't connect to rpi with either minicom or gnu screen when connecting with console cable
Is there an accurate 3D CAD model of the version B board?
Connecting to wifi
Raspberry pi cannot read from GPIO using pi4J
Pyaudio - Recording sound on Pi - getting errors
Pinning down why the Pi won't boot
Unable to share internet connection with correct settings
How can I obtain an IP address from my RPi access point?
Mini usb power cable and ethernet connection
How to add usb webcam and WiFi to RPi model A without ruinning power consumption?
OpenELEC plays only the audio but not video for certain avi files
connecting a USB to Serial TTL PL2303HX to Raspberry Pi
Basic wifi connectivity through raspbmc
Raspbmc does not seem to do anything
Networking problems without keyboard attached
Use multiple SD cards in RAID 0?
What's the RPi camera board called (internally)?
Cannot connect to RasPi by SSH with WiFi interface only
Raspberry shutsdown after boot
Changing to XFCE from LXDE
Controlling a headless torrent server via transmission
Is there a way to perform a full system encryption of Raspbian?
RISC OS assembly help
Unable to run RaspiStill from PHP
Installing Hamachi
Connect RPi to Ad Hoc network
What gaming servers can I run on the Raspberry Pi?
Problems compiling kernel on Raspberry Pi
WPUT is uploading pictures captured by Motion over FTP, but JPGs are blank?
Autologin and autorun script only once for a user
How can I install version of screen with vertical split in Arch linux?
Is there any way to send files to raspberry faster?
How can I get my hardware to generate interrupts?
Emulated_Keyboard
Is there a way to Stop/Pause an actively recording/on raspi camera?
Raspberry pi SD card issue
dhclient keeps sending DHCPDISCOVER requests. why?
sudoers file changed?
Wifi Dongle heating problem
Helping the Raspberry Pi to work on a weak USB power supply
Synchronizing video on multiple raspis
Is there any use to water cool a raspberry pi?
Screen blanking in X-Windows on Raspbian
How to disable mouse cursor on LXDE?
What is the OpenELEC/XBMC equivalent of ctrl-alt-del?
Change wlan0 Mac Address RTL8188CUS Device
Difference between 3.6.11 and 3.6.11+?
NTFS-3g HDD 0770 and 0777 permissions Owncloud
Upgrade from Python 2.7 to 3.3,x
Can't access NTP server with a static IP address
How do I install libfaac-dev on Raspi?
Prepare SD card for Wifi on Headless Pi
cgps: GPS timeout error with BU-353 USB GPS Receiver
Incorrect time until I restart the ntp server (multiple times)
Getting files from dropbox
servoblaster device file is sometimes too slow
Simple Universal Plug and Play ( uPNP ) to find Raspberry Pi on Network
How can I use more GPIO ports on the Raspberry Pi?
Method to stream Raspbmc media to laptop
How do I get .sub/.srt files to be displayed in the Video file explorer? (XBMC)
Is there a way of making raspi-config verbose?
Multiple Callbacks from GPIO interrupt
How would I get more USB ports on an RPI
How to check what process is slowing down my RPi
Transition between two images on Raspberry Pi using Hardware Acceleration
Youtube video playback fails on XBMC
Enable camera without Raspi-config
How to prevent Raspberry Pi memory allocation failure?
No HDMI output when HDMI cable is connected after power supply
use ssh to control tty1
Wake console screen with SSH
Speech processing on the Raspberry Pi
NFS Server: Not starting: portmapper is not running
Can hot (un)plugging a SCART cable corrupt an SD card?
How to get Motion working "On the fly"
Remote desktop connection to Raspberry Pi without specifying a port
Raspberry Pi Reboot Cycle After SD Clone - Card works on old Pi but not new ones
SSH into Raspberry Pi times out, but pinging works
issues with installation of software packages
VNCViewer fonts
How to use the DS2482 kernel module
Where is kernel.img?
RasPi Camera Board and Motion
mount: special device /dev/sda1 does not exists
Write current IP adress eth0 to a file
Making text very readable without X server on a 3.5 inch backup camera monitor
Raspberry Pi wifi wlan0
I need help setting up a Raspberry dash cam
battery power for RPI and IR LED bank?
MiniDLNA issue - not indexing files
Google Flat Earth needed for RPi
PHP + PYTHON + LIGHTTPD + Raspberry Pi GPIO to control the Robotic Arm
noIR Camera not working
How can I stream a video from a camera over a network in the most effective way?
How to connect Raspberry Pi to a Western Digital MyBookLive NAS and create a link to it on the desktop?
Ethernet drop out
Streaming live from the picam
I2C devices not detected
refresh chromium browser by shell script with xdotool via PHP
Green LED blinks 4 times, did I brick my Pi?
Virtual UART ports
How do I boot directly to a VNC or RDP session on a Raspberry Pi?
Error 500 for access to webserver page
apt-get update gives me errors with mirrordirector.raspbian.org
Mono C# SPI interface
How to Install NginX + Flask + Webmin to my Raspberry pi?
Can I use Robotic Operating System (ROS) with Raspberry Pi?
Does the firmware update corrupt the filesystem?
Pygame screen resolution
Exchanging Data and Instructions Between Two Raspberry Pi Via Wifi
How to automatically reboot if external hard drive not mounted?
How to setup multiple WiFi networks?
How to connect 20 DS18B20 temperature sensors to RPi?
How to wire a stepper motor?
5V sensor to Raspberry PI
Power TV on/off
How can I connect my Pi directly to my PC and share the internet connection?
Node Js, Pi Face and piface-node
Make RPi keep an semi-accurate time after power loss
Mapping SD card on networked raspberry pi from linux
Camera module works on one but not on another
Bidirectional M2M communication via ethernet (WAN) with raspberry pi
DHCPDISCOVER is using wrong netmask, how to set the right one?
What is the best way to capture still time-lapse from logitech C920 on raspberry pi
Power issues when connected to tv via usb
Make a read-only OS image from working installation
Building dependency tree using apt-get is slow
Monitoring LVM disks for failures
RTL8188CUS extremely slow!
SD card died - How to set up root on a HDD?
Battery Power Requirements
Why APT can't locate GNURADIO package even though it apparently exists in repository?
Using Pi to stream all audio output from my pc to my stereo
Local webserver accessible with external IP within network but not from outside
can take picture with PI camera
Issue with rc.local on boot
Raspberry Pi LED current limit
CGI and sudoers
Owncloud on the raspberry pi
Play videos with OMXPlayer while downloading them
NOOBS shows black screen unless I switch to to another video setting and then back to HDMI
Would it be possible to use both a Razberry Z-Wave and a RaspBee simultaneously?
Use Raspberry Pi to stream videos on a TV
no wlan0 after apt-get upgrade
Raspberry Pi Mobile Phone Control
How can I run gparted over ssh?
Is using a powered hub with the Pi safe
hdd mount for server
HTTP header for raspbian
PiFM not working for me
I want to start my Pi without logging in
Raspberry hostname.local unable to resolve in MacBook Pro with Maverik
How to use SOCKS proxy for Raspbmc
How to tell how much memory is left on the SD card?
Raspberry Pi for Machine Learning
How to make a change to the routing table persist?
How can I start X11 only for a single application?
wpa-roam can only be used with the manual inet method
pc>ssh>pi problem
set system clock to value received from GPS
Setting up Raspbian and WiFi on a private network
Can you make a high-power NAS from a Raspberry Pi?
Power requirements when overclocking a Pi to Turbo mode
12V device to a Raspberry Pi
Power Management System for Raspberry Pi
Stop raspberry pi from turning on when plugged in
Software for running virtual hosts on the Raspberry Pi
Raspberry Pi kernel configuration for USB mouse and keyboard
Communicating between two Raspberry Pi
How to use JFFS2 or UBIFS to avoid data corruption and increase life of the SD card?
Black screen with X cursor when running VNC on boot
Is Raspberry Pi powerful enough for a VDR with a USB HDD and USB DVB-C stick?
Pi won't show anything on VGA screen
launching chromium browser via terminal throws errors
running npm install throws permission error
Install Raspbian OS on SD Card for Raspberry Pi
Create Standalone SD Card from a NOOBS installation
Stream videos wirelessly from PC to Pi to TV?
Unable to see public IP when running ifconfig or ip address commands
Under what user is apache being run?
4 USB camera framerate and resolution
My new raspberry pi ethernet is dead
Where is my RPi losing power?
Only write to directory when USB is mounted
fat32 vs ext2 USB-HDD filesystem efficiency
Will I need to do soldering to be able to work with components using the arduino?
How to use ARM software in Raspberry?
What could cause the ext4 root file system to become unusable after a reboot or panic?
Hard to get raspberry out of case
Powering 4 x 12-15v motors with Raspberry Pi (quadcopter)
Why does my Pi lose io after a while?
Bluetooth device is not available?
Programming on Raspberry Pi device?
Slow connection with raspberry when "/" is on external hard drive
HDMI-CEC pass through reciever?
How to communicate between Raspberry Pis using WiFi?
How to turn my Raspberry Pi into a small game console?
I need a USB keyboard, mouse and wi-fi adapter to work on my RPI *under 200mA*
RPi doesnt work after formatting SD card
Unable to setup WiFi on Arch Linux and Realtek rtl8192cu
Water irrigation system for Raspberry Pi
Is it possible to stream H.264 with RTSP on Raspberry Pi?
Do I have to connect a resistor to my DHT22 humidity sensor?
Having trouble reading (MQ 4) sensor digital value
How to open up terminal (gui) at startup and execute a command?
What speed of SD card is better?
Triggering a solenoid off GPIO
Maximum number of USB devices supported
Halting inevitably leads to reboot
Show IO value on webpage in realtime
Execute C program from web server
Scratch GPIO Shows Limited 'Sensor Value' Options
Not able to detect interrupt on GPIO 2
Can 3.3v GPIO pin be used for buttons that don't need power?
Which framework is best to communicate with Internet?
Why does USB port enumeration change?
Raspberry Pi network camera
Can we order custom made Raspberry PI?
Where is the archive.key for backports.debian.org?
How to protect RPi camera from ESD?
Raspbian server version
How to make Pi an AP with 2 WiFi adapters?
Are there any major differences when programming of the Pi and for normal Linux
How do I protect Raspberry Pi Webcam over internet
Connecting a Pi to a Projector via RS232
NAS & Torrenting
Connected to the internet, but can't download data
Performance drops after a few seconds
How do I get a GUI program to run before the login screen?
How can I install GCC 4.8 on the Raspberry Pi?
Will Raspberry Pi with OwnCloud and RAID setup be fast enough?
new text rendered over older text in pygame
Shutdown properly when power-supply can't supply anymore
How to set time at a specific time each day
How I transfer files from laptop to raspberry via ethernet cable?
open a win32diskimager-imported file on Windows
What permissions does Motion require to write to specific directory?
Is it possible to install a larger RAM chip on the Raspberry Pi?
Unable to set static IP
How do I create command line menu in Debian with a Raspberry Pi?
How can I connect by raspberry using the tethering USB of my (android) phone
Booting from an external USB drive
How to set up ssmtp and send emails?
Restrict remote access to Pi from ONE computer
Issue with owncloud and btsync
WPA_GUI can't load wpa_supplicant
Youtube TV Client
SSH into Raspberry Pi without knowing IP address
Play music from laptop through XBMC on TV?
Control XBMC remotely using keyboard and mouse?
Why is Web consuming all of my Raspberry Pi's CPU?
Raspberry pi hangs on ssh, but gives feedback from a telnet terminal
Unable to mount Win95 FAT32 (LBA) boot partition of freshly imaged external hard drive on host machine, to make Pi boot from USB
Open Chromium on start?
Power Supply With UBEC
Is auto upload possible?
Changing the static IP of a Pi headless
Driving Bi-Color LEDs
Boot into the GUI after changing default user
How do I stream movies to openELEC via LAN?
Read files from external disk through command line after login?
Using Raspberry Pi as video test pattern generator
Looking for a pi-compatible thermometer for brewing
Which is the highest version of libc6 available for Raspbian?
Trying to launch GUI thru Cygwin ssh: FATAL: module g2d_23 not found
Do HDMI to VGA cables work with Raspberry Pi?
Raspberry PI, PHP, MPG123 playing music via 3.5mm jack - No sound via PHP?
Impact of Uptime over the lifetime of a RPi
Write Device driver for Raspberry Pi?
Will RPi suffer from the Y2K38 bug?
Run a GUI without the desktop
Advice on RPi as backup server
How to restore Image of SD card from a larger SD card to smaller one
Safest way to connect Raspberry Pi to Arduino Uno R3
More free raspberry Pi alternatives?
Good TV tuner and remote for HTPC
Need OS advice!
Couldn't start vnc in raspbian
How to enable Airplay on raspbmc via SSH?
How to connect DS1307 5V Real time clock (RTC) to 3.3V?
Will I be able to use the Pi to detect counterfeit money using UV and IR sensors?
Can't figure how to identify WiFi adapter
Trouble connecting to wireless network two rooms away
How to turn off auto-login
Error when trying to control GPIO in python
aux output with hdmi as video
DVK511 w/ LCD1602 - No text appearing on the LCD
cloning SD card to another SD Card
where can i get maestro from riscos?
Have webcam sever going but cannot reach it from outside the network even with port forwarding set up
Will a Model B 512MB Pi run a Minecraft Bukkit Server
Relative benefits of standard vs NoIR module cameras for Raspberry Pi
Booting Raspbian onto a Laptop
SSH for Raspberry Pi using a PC
Audio Output on RaspPI
Read a file from inside the raspberry pi's SD card
How to build custom OS for Raspberry pi from scratch?
GPIO pins alternate high and low
Change default username
using both internal eth and a usb wifi dongle
How to get back to NOOBS?
How can I install emacs without local (Pi-based) network access?
Power a Pi from a hard drive enclosure?
The D-Link DWA-131 Wi-Fi adapter is not working on Raspberry Pi
Best USB sound card for signal elaboration
Automatically run a program as root for GPIO?
Powering Pi and 3.5" HDD from one PSU
"Encountered a section with no Package: header" error?
ADC for ultrasonic frequency recording?
Why does a time delay suddenly fix my code?
Set RAM split based on HDMI status on boot
OS that would not corrupt SD card when abruptly shut down?
How to debug no Internet connection?
SD card seating issue?
Raspberry Pi wake up on GPIO
SSH outside LAN?
Set up Edimax EW-7811UN WiFi dongle?
How do I send data from the Raspberry Pi to the PC
Setup raspbian to respond to .local
Pre-install device drivers
Run .sh file after LXDE enviroment is completely loaded
System for determining occupied seats
Static IP on Arch Linux
Why is 14 (board numbering system) listed as a GPIO pin, and not 13?
Connect a GPU into Raspberry pi
Web-based relay control
How do I change the Desktop wallpaper from the cli
Raspberry Pi restarts after connecting 2TB WD My Passport
List of supported software versions?
Configuring Rpi as a Privoxy-protected Access Point
Installing Raspbian from NOOBS?
WiFi USB adapter for monitoring on the cheap
Executing a jar file when Raspberry boots up
Start Raspbmc via Logitech Unifying receiver
Updating kernel/firmware to specific version
Booting Raspberry Pi for the first time!
How to control a Traxxas XL-5 ESC directly from the GPIO?
How to start working with Raspberry Pi?
Samba on Raspberry Pi ->USB reset
Ethernet Connection
Packet sniffing with channel hopping using scapy
Can Raspberry Pi Model B be used as JEE applications web server?
First time RPI user, Raspberrian installer won't boot, red light only
Why are the buttons that I am using with my Pi inverted?
Read positioning data from 4 laser mice
Simple web interface to execute C++ program
Pipe output from several commands into 1 line
How to disable emails from Crontab?
Apache2 webserver running python script
Additional USB ports for a consumer product?
Estimated run time off of 9V
Creating halt/wake button?
Brand new pi, black screen on first attempt
Use internet on raspberry pi via laptop
What is the cheapest and long distance (20-30 m) way for communicating Raspberry Pi and attiny (or any other microcontroller)?
How to generate a PWM signal with Visual Basic?
Wiring a home to power Raspberry Pis
How can I automatically mount USB hard drives (regression)?
Raspberry Pi wont boot until ethernet cable is connected
Is a super computer built from many RPis really practical or just a novelty?
Add Wireless Adapter to RaspberryPi
Is it a feasible idea to use a Raspberry Pi as a wireless router?
Data loss (and/or corrupted) over serial USB connection to Arduino
Get IP with no internet
how to disable keyboard/mouse input?
Can I use an ATX power supply to power a graphics card, the USB3380EVB and a Pi?
transmitter for raspberry pi
Absolute RaspPI Beginner what do i need to realize this project?
Deleting NOOBS from SD card and only keep Raspbian
Can I transform GPIO pins into a CAN bus
Connecting multiple ds18b20 digital temperature sensors to different GPIO ports
How can I use my Raspberry Pi for motion detection and SMS?
Controlling a relay with GPIO
insserv: warning: script 'mathkernel' missing LSB tags and overrides
Where does my secondary IP come from?
Can I upgrade the single USB port on a Model A to two ports, like the Model B?
Raspberry pi as a second monitor for Windows
To Access the gpios from webpage by executing python code
Capacitive, Small Screen?
What streaming solution for the Picam has the smallest lag?
What kind of SD card is recommended?
Where is the HTTPD.CONF file?
Locking down Raspbian to only allow limited features
32 gigabytes memory card to 8 megabytes
DrRacket seg fault
Using init.d script to start my python program on startup
Is there any lightweight webkit browsers that isn't slow?
Raspberry pi network over usb
Server and client between PC and Raspberry Pi
Raspberry Pi - Controller for a light system
How to mount a Raspbian SD card on a Mac?
Connecting an LCD display to the Raspberry Pi
Can I use the composite video connecor to send video INTO the Raspberry PI?
How to force rescan of USB serial devices?
Oracle Java could not find or load main class
Reading barcode with Raspberry Camera and zbar
How can I edit a Raspbian SD card image to use a static IP address within Windows?
7 Segment display too dim with BCD to 7-segment latch/decoder/driver
Connected to the Internet, but can't ssh or ping
Use RPi as a LIN Master to control slave nodes
What web servers can I install on the Raspberry Pi?
Connecting a micro pump to Raspberry Pi
512MB suddenly not recognizing USB or ethernet
Speeding up translations in arrays
Raspberry Pi to email when power outage occurs
Robust power supply, powerdown and industry housing
How to communicate with Pi through a tablet/phone (Android) in a no-internet environment
How to get Wi-Fi to connect on boot?
Not able to connect to the network on Raspberry Pi
Raspbian - With Wifi Dongle connected with internet, but no ssh
Alternative ways of attaching power to a RPi
Can I use video and HDMI output at the same time?
nat in the iptables is not recognized
RPi will not start; No green flashes; Reflashed SD; 5v 1.9A power
Not working: EDUP EP-N8508GS on Raspbian (Wheezy 2014-01-07) with wpa_gui
Using rsync to backup Pi
mix power and data for usb HDD
SSH connection fails with fresh install of XBian and XBMC
What is the most optimum memory split for streaming pi's as security monitors which you will only ssh into?
What to know about powered USB hub?
Remote Access with VNC outside local network
Is it correct to put startup operations in /etc/xdg/openbox/autostart?
RF transceiver and XBee module, both need UART?
Send Python script data to Webserver using push button
Anonymous File Upload
Create new user and enable autologon Startx/LXDE
Stuck on Raspi-Config
Will customizing USB pinout help with backfeeding issue?
Edit root files from SD card?
install Raspbian from .img on windows
What is the devtmpfs filesystem and how to shrink it?
I can't connect to my Raspberry Pi until I curl to the connecting device
How to crypt a specific folder in raspbian?
Best way to store temperature data offline
How do I get simple lighting inside a case for my Raspberry Pi?
How to run a script (Node.js) at startup
Any program for sending characters to RPi web server?
gpxlogger/gpspipe clean file close
Automatic boot and shutdown
Serial Input for the Pi
Deluge permission denied for directory in external hard drive
Any ideas on how to increase the range of an IR transmitter?
Pi Performance: tcpdump vs wireshark
How to keep the the mini USB power secure?
How to override config.txt settings during boot?
TV remote no longer working
Can a raspberry pi accept input data if the input voltage is 42 mv when is required is 3.3v?
auto brightness bypass whilst using Motion
Not able to connect my netgear WNA1100 wifi adapter to my raspberry pi
Clone SD card via SSH over network
USB webcam showing green screen
No-ip redirects to router config page instead of lighttpd server
How would Raspberry Pi perform as a router/firewall?
Pi GPIO - momentary open switch for shutdown - python help needed for time delay
My Windows share will not mount during boot
raspberry pi hangs after 2-3 days of continous use
how to know how much battery power in remaining?
Cannot SSH to Raspberry Pi via WiFi only
Solving “RTNETLINK answers: File exists” when running ifup
Is there any way to get redshift to work?
Are there any `armv6j_hardfp` binary repositories for Gentoo?
Raspberry Pi communication over USB
Could Motion and the PI learn their environments over a few weeks (eg ignore normal movement)
LED strip has R-G-B instead of DI and CI
Using one Raspi to control long (>100ft) of 5V LED strip
Capturing serial number of 2 USB RFID Reader in python (PI+2 RFID (Mifire RFID))
Find Raspberry PI address on local network
Internet Connection Sharing
Hello world script doesn't work
Watch YouTube in Browser with Raspbian
script runs at terminal - but not in cron
Raspberry pi not booting!
How to create an EGL window on HDMI monitor output through SSH?
Trying to connect a Raspberry Pi and Water Pump with one power source
How to have remote desktop on Macbook with Raspberry Pi?
Use Raspberry Pi to control PC's power switch
Minecraft Pi Permissions
How to cross compile large projects?
Installing VNC server in raspberry pi
Camera problems: green tint and long delays after snapshot
Raspberry motion getting killed every morning and evening
Raspberry Pi OpenVPN Client Speed Bottleneck
School network and raspberry pi
C and C++ Library and where is it located actually?
Java JDK 8, use with .jar how to?
Mount NFS directory at boot
The way to catch system clock interrupt in Python?
How does python GPIO bouncetime parameter work?
do I require a potentiometer
Cannot delete files from Samba share
Adafruit I2C Library Problem?
executing Linux commands inside a python script on my PI
Use PyDrive to upload files to Google Drive folder
Script works from command line, but not when called automatically by PI
NAS on Rpi vs ASUS RT-n16
How to power up raspberry pi with batteries?
Presenting a webpage from raspberry pi
RPi can't get IP address
How can I enable the camera without using raspi-config?
Get USB address
Disable i2c in Raspberry Pi
Converting AAC to MP3
How to change DS18B20 reading resolution?
Auto-reboot on hang
Can't read/write to GPIO as non-root after export
Can't find the files that fill up my Rasbian SD Card
Connection Pi -> Arduino through nRF24l01, problem with integers
How to have wifi connected raspberry pi control an arduino?
Expand file system on USB on Raspberry Pi
Connect to Pi via network switch
WiFi AccessPoint bridged to LAN transparently
Is it possible to set the desired DPI of an image created using raspistill?
Raspberry Pi apt-get update error
Is Pi a good Development/Post-Production Server
Most Secure way to Attach Wires to Header?
Light HTTP server to upload,browse and execute files
Use Raspberry Pi only in local network
vcgencmd measure_temp doesn't always work
Audio in Java application won't stop when told
Send camera image to cloud for more open streaming?
What is the Best Way to Label your DS18B20 water proof temperature probes?
Control 18 LEDs individually? (17 GPIO pins)
communication between two raspberry pi
UART/Serial communication w/ mono
How to connect more than 1 am2315 temp rh sensor to respberrypi
Android screen cast/mirroring to Raspberry Pi?
record audio from rtl_sdr using usb dongle
Trying to image SD card with wheesy-raspbian - dd command fails with "No such file or directory"
Filezilla won't access pi via SFTP (Times out)
beta epiphany-browser (Web Browser), comand line auto start?
can't make module "mod_dingaling" for freeswitch
can't assign IP to my rpi
How to use 2 x MCP23017?
GPIO pins are always HIGH
control motion via cron
apt-get upgrade fails because of some dependency loop
Update Raspbian O
Using FSR with Raspberry Pi
HDMI input to composite out
Sending live data readings from Raspberry Pi to laptop
I2C with zener protection isn't working
Git automatically pull, commit and push?
Can I have same static IP for wlan0 AND eth0?
Camera blinks but doesn't record
Deluge crashes at raspberry pi after while
L.E.D controlled by IF STATEMENT from variable
Accessing the command line on the Raspberry Pi outside
Making Raspberry Pi Bluetooth slave
How do I mount the correct drive everytime the Raspberry Pi reboots?
Transistor or optoisolator when dealing with the GPIO pins and an external power source?
Graphic output sensor data
Build XBMC on wheezy raspbian
HDMI not functioning
reopen program when it is crashed
Check a program/script is active and running properly
Does "/dev/null" writes data to SD Card before discarding?
Language query(Python?)
Samba Server not running
SSH Login prompting for SUDO password - RaspBMC
Running NOOBS on a used SD card
My first breadboard / led
How do I restart a python program on my pi when it crashes?
allow apache to run sudo scripts
Connecting to a raspberry pi simultaneously from more than one desktop PC
Is it possible to physically upgrade either model's USB ports from USB 2.0 to USB 3.0?
How to improve boot time for Raspberry Pi?
No audio on Xbian connected to an AV receiver via HDMI
How the remove the Raspberry Pi Version message after login
use ssd as main drive
SSH not working on OpenElec Frodo
Is it safe to buy Pi at Ebay from China?
HDMI output not functioning
trigger cron job from web application
I want Raspbian and Retropie; how do I get both?
Is that possible to transfer file from Raspberry PI to PC through LAN?
Need help to get NzbDrone to autostart
Connect to raspi over ethernet with no known IP
external ip address
Raspberry Pi not sending Multicast UDP
Raspberry Pi Screensaver As Signage
Why does the Raspberry Pi's GPU control the first stages of the boot process?
Can I use the Raspberry Pi as a Mini-PC?
Output terminal to HDMI?
Battery packs without "blip"
Has the Rasberry Pi website taken on a new theme?
How to install PiTFT and use to the GPIO for other usage (like serial console)
E-mail client to automatically handle attachments
Edge Detection using usb webcam
USB external sound card and Minimodem Software
samba net command on Debian Wheezy
Back up switch or circuit
What servo motor and mechanism to move the whole Raspi, its camera and case?
How do I maximize a headless Pi to run node.js?
How to develop for Mikroe's click boards with free software only?
How to install usb wifi on rpi
How can you use face recognition on raspberry pi as a login to the pi?
How to send multiple sensor data from arduino to the raspberry pi, and from there to google docs
How can I communicate Raspberry Pi and Arduino (in both ways) using a 10-15m distance wires?
Will the RaspberryPi Operate Correctly in a refridgerated, 60*F (15*C) Temperatures?
my raspberry pi freezes while face tracking using openCV and servoblaster
How to install opencv and eclipse on a raspberry pi
What is the simplest way to securely access my Raspi from internet?
How do I discover the IP address of my headless RPi?
How do I put UNIX on the Pi?
Raspberry Pi and Arduino Storing Data
How to bring out Status LEDs to be available on enclosure
What GPIO pins are required to Power RPi?
Baremetal Forth for Raspberry Pi?
Can I clone my entire Raspberry Pi for deployment onto another Raspberry Pi?
Transferring data from Arduino to RPi, Missing data
RPI can't connect to internet
Network storage on SD-Card
Raspberry PI camera module
Debian Release Upgrade
Wifi drops on raspberry PI
I get WiFi timouts with the rt2800usb driver
Why "Server refused our key" when trying a SSH connection with Putty
Can I develop Android apps on my Raspberry Pi?
Control GPIO from outside home network
access services over internet not working(anymore)
My sd-card crashed after a reboot, how can I fix it?
/etc/network/interfaces file keeps changing itself - breaking wifi connectivity
Installing Raspbian from NOOBS without display
How to get the temperatur of 2 sensors in java, using an extension board?
Using 'Network Manager' for Wireless & VPN Management
Used-to-be-working Pi does not boot, shows no lights, gets pretty hot
Auto-Execute a program on power up
Using the Raspberry Pi Cam at 110 degrees Celsius
Raspberry Pi as NAS
Installing Python 3.4 on Raspberry Pi
How to get remaining memory in SD Card?
More Software PWM
add user, and set user privileges, setting file permissions block certain commands?
Safest way to power a hungry Wifi adapter and the Pi from a single 5V source
How to interface raspberry pi and plc?
echo: write error: Operation not permitted
How to get the state of a GPIO pin bash
How do I connect Raspberry Pi to my TV?
bridge eth0 static wlan0 static wlan1 dhcp
How do I shrink the screen with composite out?
folder permissions changeing and i don't know why
Does Atlassian JIRA run well on the Raspberry Pi?
Can I play Day Z on My Raspberry Pi?
OpenCL w/ Broadcom GPU?
Can I power my pi with an 800 ma/h battery?
Set IP of Raspberry PI device automatically
WIFI USB adapter not detected
Raspberry Pi used as a cheap serial-to-WLAN converter
Docker on Raspbian?
Connect to unsecured wireless network
Is there any point to a 2.0A (or greater) power supply, given the 1.1A polyfuse?
How to backup only select partitions of an SD card?
Image Recognition Raspberry Pi
Logic converter for relay module or extra resistors and transistors?
Cannot Connect to Apache Server, No Errors Generated
How to install python3-matplotlib on RasPi?
Create a Terminal Menu GUI in C
Does LIRC support 'Everything at Once' remotes?
Detect if iphone/Android nearby?
How do I setup automount of any (mountable) USB drive in Raspbian?
Run bash script on startup
What programming languages does the Raspberry Pi support?
Displaying binary files in the Terminal completely messes up the Terminal
dd entire SD card to new one
Cloning Pi Image
Is Wolfram Mathematica compatible with all the operating system images?
WS2801 LED's only glow white
Will my Pi will be fine if I use those el cheapo chinese power adapters?
Is it safe to transfer files onto the computer from the Raspberry pi sd card, and then put it back later?
Why don't I need time:sleep() for talking with a 10MHz chip?
GPS for Raspberry Pi, which product is better in terms of technical specification and compatibility with Raspbian?
PiFM not transmitting on some frequencies
Boot to Login Screen Raspberry
Default login in Raspberry is not working, how to go back to config screen?
Email notifications for low free space
Multiple PIR Sensors
Raspberry Pi SSH login slow
How to add start up and shutdown script?
Raspbian fresh install SSH default IP
Corrupt image fix
Reading from serial port [loop]
Reading data from external device
Raspberry Pi GPIO input help
How to "scroll up" and view previous console output?
Raspbian is very sluggish. Almost unusable
How to know when to pull the power from SSH
2FA on RPi and trusted computers
Effects of overclocking
NTPd is not updating time
Using a Pi as an EEPROM programmer
soft-float debian wheezy and debian wheezy
Working with Raspberry Pi having only a laptop and a table (no extra monitor)
RaspBMC - what is the .xbmc-current folder and why is this being used rather than .xbmc
Is it possible to install old versions of Raspbmc?
Pi Camera - how to create a flash?
Writing an XBMC addon: how do I add a torrent to my home PC over LAN from RaspBMC?
Raspberry Pi image with a flash filesystem
How to do a minimal size backup after expand_rootfs under Windows?
Why has Raspbian enabled swap by default if that is bad?
Can I use openCV with Java SE embedded wrapper for Raspberry Pi?
When do I need accurate time via NTP?
Controlling a servo and playing sounds
SD Image won't fit on SD Card
Install tightvnc in arch linux raspberry pi
Raspberry pi GPIO extension
Problems recording while playing audio
Sample program for RaspiCam API not compiling
How to identify the USB to Serial wire mismatched?
Assembly code on Raspberry Pi
Looking for 3G USB Dongle (with low-power consumption )
Does Raspbian come installed with PyOpengl?
What packages are pre-installed on the current Raspbian image?
Using Python Shell (Idle or Idle 3) I get Run time error and suggestion that I "Try running from Root"
Least delay for audio processing
A ping between to raspbian fails
How do I install snort on RPi?
How to stream video and audio from a Raspberry Pi?
DHT11 module compilation error
Raspbian kernel source compilation configuration
Cheap COTS transceivers that work with Raspberry Pi?
RFID system that integrates with Raspberry Pi Model B?
Display IP Address on Character Based LCD
Pi4J i2c error: Error writing to /dev/i2c-1 at address 0x21. Got -20001
Raspberry Pi to Arduino protocol
Unable to write to GPIO pins using gpio command line utility
Access Archlinux Remotely
Can I directly connect to my Pi wirelessly without a router?
RS-485 and Raspberry Pi
Automatic start of python script after just plugging the power supply
Raspberry Pi and Arduino communicate over RF?
How insert a command line command in python script?
Connect keypad in Raspberry
RFID reader for Raspi
RF transmitter and multiple receivers to led on/off control
Can I use any GPRS Arduino shield with a Raspberry Pi?
NXP Explore NFC using libnfc on Raspberry Pi
Using OpenCV with RasPiCam and python
How do I install pandas on Raspberry Pi?
ServoBlaster problem (auto rotate)
What is the best way to help my Raspberry Pi manage itself unattended?
Raspberry Pi and the USB to TTL Serial Cable on Mac
Relays are isolated or can they cause any harm to my Pi or connected electronic device?
Run Raspbian "Wheezy" in QEMU on Windows
2.8" TFT Touchscreen with pygame script from console
Reboot via cronjob does not work, it just shuts down without booting up again
Raspi+Arduino+RS485
How can I increase USB voltage on multiple Pi's?
How to connect my RaspBerry Pi directly to my PC using ethernet cable? Don't work
More control of serial?
Are there any GPIO pins guaranteed to stay low during startup?
Starting an application when a certain port on the IP address is accessed
Big ask: could anyone give me a tutorial to compile entangle 0.6.0?
LED lights on pin 1 but it fails on other pins
Connecting a PS/2 mouse to Python
CCTV housing that fits the Raspberry PI
Best Media centre setup?
Can I perform a total backup of my system on an image file?
Using Watchdog to reboot in case of overheat
Can I control this ESC/Brushless Motor with a Raspberry Pi and/or Arduino
How do I display an image file (PNG) in a simple window?
Trace raspberry pi booting process
No signal on TV and Computer Monitor
Raspberry pi reboots when usb wifi (Edimax EW-7811UN) is plugged without usb extension cable
Raspberry Pi's analog audio output in watts
"Home Server" + XBMC
How long does a pi last with an 8 gb sd card?
How can I use my Raspberry Pi camera to detect motion and then email me a photo?
Can not read SD Card anymore
Trouble with rpi-source (hello world kernel module)
install MATLAB directly on raspberrypi
Is the RPi enough to host a web application with pictures and videos?
WiFI connection keeps disconnecting
Shared Windows Folder
Connection for 6 raspberry pi camera modules?
Should the Pi automatically connect to an ethernet connection with a default Raspbian install?
Syntax error near unexpected token 'GPIO.BCM'
Having a Cook server send signals to Pi
Raspberry Pi with boots up with Rainbow screen
How do I improve Raspberry Pi Boot Up Time?
How can I install the latest version of Chromium?
Powering Pi with a 5V regulated power supply
How to install RetroPie using/alongside NOOBS?
PyInstaller fails
Powering an amp and a Pi from a single 12V lead?
USB to Serial converter / connect to pi?
Are there any alternatives to the Pi Camera?
how to turn on and off an led with only a tactile button
Raspbian wifi connection problems
How to fix boot section / firmware and keep user files
The 'ACT' LED is not blinking and the CPU is overheating.
Forcing one of two wifi dongles
RPi remote access over internet
Debugging headless install
How can I permanently fix /dev/vchiq permission errors?
Sending and receiving SMS via a huawei 3g Dongle E220
SSH into Raspberry Pi times out, ping can't reach host
pylirc returns none all the time
How do you wire 2 stepper motors to a Raspberry pi with a ULN2803?
Is there a console-only (no GUI included) distro under 1 gb?
Booting up a headless Raspberry Pi using Mac OS X
Raspberry Pi arkOS terminal Password not known
Power external hard drive though USB -- safe to use USB charger?
What type of SD cards can handle a high volume of read/write?
Multiple Inputs through GPIO
Streaming from the camera only when required?
RedHat distro on RPI?
If I were to set my RPI up as a webserver, what security issues to my home network should I be aware of?
Can't Access TTY: Job Control Turned Off
What bug tracker can we use on a Raspberry Pi?
ssh into pi from Mac over direct ethernet connection
Need to initialize serial connection with screen
How can I download packages to windows so that they can be installed in raspberry?
Connect to OLED Display Module
Is there a way to automatically activate a script when a USB device connects?
local and global variables in bare metal programming
Red LED only staying on momentarily during bootup?
Error when trying to install XRDP from Putty
Music, stored on the Pi, played over HDMI with visualisation, controlled from mobile phone
show data online
Raspberry PI Audio Input
Do I need female to male jumper wire because I have a jumper cable
Can't WRITE out a text when running Python Shell
Android commincate to Raspberry Pi through otg
Connecting multiple light sensors to one port
Transmit music to multiple iPhones
Connecting RTC DS1037, Pin 5 already occupied
Picamera as streaming server
USB card as my default Audio Device
Using incrontab to read GPIO's
Raspberry Pi Speaker
Rpi as usb stick
Raspberry Pi Compute Module schematics
Best method to test if the Pi is stable after overclocking
RPi GPIO as a high-speed square wave generator
Raspberry Pi is unstable on a single projector, appears to be HDMI related?
Pi in "meshed" wireless network
How long does the RPi last on a battery?
Problems with Pifm legality
Setting camera module to /dev/video0 to scan QR Codes using zbar
How to use flash storage as blackout-proof volatile memory?
Raspberry PI connect with Analog Devices ADIS16227
Weird SSH problem
How to run python script on pi without logging in everytime
IndexError DS18B20 Temperature sensor
Mac OSX CyberDuck Upload Failed
Using Raspberry Pi as print server
How to check whether a Webserver is Installed in Pi or not?
Bypass in-browser authentication to connect to internet
android device as USB Mass Storage
Raspberry Raid 0 gains
A Shortcut For Checking Temps?
How to create a REST services using Node.JS in Raspberry PI?
Plant watering installation
Java Eclipse configuration for raspberry-pi
How to get a specific kernel version for Raspberry Pi Linux?
Access external HD formatted as Mac OSX Extended (Journaled) from Windows PC
WiringPi vs default Raspbian RPi.GPIO module
Raspberry pi wont boot, red light shows
How to write an IP change notifier script in Xbian?
Fast os for Raspberry Pi
Turning on HDMI programmatically doesn't work
take images in a short time using the Raspberry Pi camera module
Disabling rainbow splash screen does not work
My pi with berryboot with vnc enabled wont work
Whenever I connect a usb device, it shuts down and won't boot for 3 minutes
How to remove the first line on the MOTD screen?
sending live data reading from raspberry pi to internet
playing wav files with pygame bad quality with noise
Raspberry unbootable after unexpected shutdown
Home Automation, Mechanical Relays and Physical Switches
Raspberry Pi to Arduino (Leonardo) avoiding latency
Powering a 3-12V water pump on raspberry pi
Airplay Mirroring XBMC addon
One Wire Temperature auto setup while booting
Can I transfer programs to my RPi via a USB stick from Windows?
WLAN or LAN, where is the bottleneck?
Will a script keep running even if I SSH in separately?
Arduino Serial Port via Raspberry Pi SSH
Move 16GB SD NOOBS Raspbian to 64GB Micro SD for a new B+
Is there any GUI mode for omxplayer?
Executing remote binaries over network
Why does sudo not work in this case?
Powering a RPI with its circuit from one wallsocket
QEMU Raspbian on OS X
Remove Maynard and cgroups
Raspbian GUI Headless
How to get in the raspbmc console if exit and esc does not work?
Is it fine to use an ASUS Memo Pad power supply on a B+ RPi?
SSH slow to ask for password
'Safe' temperatures for use
ssh: connect to host ... port 22: Connection refused
How can I get Raspivid to skip h264 encoding? (getting rid of 5 second latency streaming video)
Disabling DHCP Server
Mount NFS Folder share on RPi from a synology NAS
dhcpd after reboot (Arch Linux)
USB modem not switching from mass storage to modem mode
Mult-head micro-usb cable
Preventing SD card corruption in the event of power failure
PI4J: Multi-threading when listening to Pin Interrupt events
Error on displaying mySQL records in my REST API
Raspberry Pi w/ 2 ethernet ports
PIC Microcontroller to Raspberry Pi Communication
Wi-Fi dongle not working
Using a Generic Switching Power Supply
Can I automate raspi-config partition resize?
Why do people use powered USB hubs?
Using the UV4L driver to stream video from the raspberry pi camera to android phone
Sound card for raspberry pi?
What's the difference between the Model B and B+?
Official MongoDB Repo for ARM Processor for Debian base
Colored screen when booting raspbian from noobs
Shutdown, reboot not working
What power supply should be used for the B+ model?
What hardware do I need to turn Raspberry Pi into a TV remote controller?
Can I use my Raspberry Pi as an AirPlay receiver?
Play video from ssh to TV
ImportError No module named thread
Is the Raspberry Pi suitable for use as a commercial WiFi Router?
Using battery pack as a UPS
how to access local GPIO from remote Django/apache server
Raspi periodically unreachable via SSH
How to debug avahi-daemon? Hostname not coming through
Is PiGlow compatible with model B+, and will both fit inside a Pibow?
RF24 communication with Arduino
Maximum current from usb (model b+)
Hot plugging the GPIO cable
wlan connection not working
Pi as a USB client
Power on from idle with gpio3, undocumented?
Smallest interval that RPi can record
Why are system logs not rotating?
7.2V battery with Raspberry Pi
Pi Headless: How to confirm that the Pi is shut down
Disabling IRQ #32
Viewing Pictures from the RPi on my computer
Using Raspberry Pi as a router connected to an access point device
using the temperature command in a bash script to affect gpio
Raspberry Pi network can't be accessed outside of network
Using Qt5 on PiTFT
Accessing a SSH shell session between Rpi and computer from another computer
Noob question- PI wont boot
Is it possible to format RPi SD card remotely?
HDMI out not working
Raspbmc slow networking issues
Raspberry pi as a tmc server
Powering a 24V 1A device
raspbian wheezy: Package 'i2c-tools' has no installation candidate
Locale errors when installing packages
Raspbian/OctoPi File Recover
Can I use GPIO to close a circuit on a RC sender PCB?
USB bandwidth for the RPi model B+
Stereo camera frame synchronization/genlock (video or still image)
Kit for beginners
pymodbus rtu RS-485 communication
Fullscreen browser for Raspberry Pi
raspberry Pi and robots in one toolkit
Raspberry Pi Camera Module, Time Lapse Photography
Is there a way to get a list of what has been installed from a specific repository?
Web Client for Raspbian MiniDLNA
"Easy" Headless File Transfer
Raspberry Pi wireless AP problems (static IP address)
How can I save my SD card without to make a too big image file?
Can't get Raspberry Pi's IP address (Headless Method) Unix/OSX
How to use usb ports on raspberry pi?
How to make Raspberry shutdown when I unplug the ethernet cable
How to fully control Raspberry Pi over Wi-Fi?
Connecting a garage door opener remote directly to Raspberry Pi
how to install libtbb-dev in raspberry-pi
Can a Pi back itself up?
EmulationStation hot key buttons not registering
Connecting two cameras into a PI
I've locked myself out of SSH and my pi while trying to set up public keys
Reducing 24V to 5V for RPi PSU
Does the Raspberry Pi need a cooling system?
can someone explain lambda functions?
What does T mean in file permissions?
From raspi to laptop python3 vb.net/c#
Write to USB stick on specific USB port
Using other camera modules to build custom webcams
Want to stream just captured audio using VLC media player as HTTP or RTSP
Unresponsive USB on a Raspi Model A
How can I exit a while loop at any time during the loop?
Pi B+ with TFT running Kali
Can Windows XP run on Raspberry pi?
Should I power my Pi and USB hub through the same power supply or separate ones?
In monitor mode but not sniffing packets :(
Python: Is there any way to get a list of IPs connected to a network
What size screws does the Raspberry Pi board use?
Raspberry PI will not boot unless I apply pressure to SD card
On RetroPie is it possible to speed up the time needed to switch from an emulator back to emulationstation?
Can't install software in raspbian
Connecting to Pi over the internet - Already tried a lot of things
Pi NAS: Access over internet
Render a HTML5 Website with no interface
Stop Pi from searching for ethernet connection on startup
Can I Use this Relay Board with pi?
Raspbian Linux: No WiFi scan results from “iwlist wlan0 scan”
Does Raspberry PI Model B+ Works Over 24*7 and 365 days continously?
How can I get tightvnc to start automatically on startup?
Reading NOOBS SD Card on my Mac
Best practices for "hardening" an RPi for embedded applications (unattended operation)?
"Could not resolve" errors with wicd-curses static configuration
UPS for raspberry pi
My 3V relay doesn't work on GPIO but works on 5V pin with resistor
miniDLNA & srt files
9 One-Wire Temperature Sensors - Intermittent Response
Connecting B+ to Serial Port
Script to retry wifi 10 times then force reboot if connection cannot be established
Using Raspberry Pi as an SVN server?
What methods are there to connect arduino to a raspberry pi
RetroPie missing 'emulator' folder
cec-command to switch to TV 0 from raspberry pi not working
Is it safe to post entire syslog to the net?
What format should my SD card be?
16 channel relay for RPi
5.3V power source w/ 24kohm resistor
Is it possible to power a raspberry pi using android phone in USB host Mode?
static eth0 adress
mounting content of pendrive to mobile phone via bluetooth
TL-wn725n V2 driver needed for Linux 3.12.28
TeamViewer on Raspberry Pi
Python serial permission issue
Building a remote drone with a pi
Root file system corruption of RO partition
My sdcards won't boot
Is Raspberry Pi powerfull enough for commercial web development?
How can a USB Bluetooth Dongle be used as login TTY
Data transfer from arduino to raspberry pi wirelessly?
Simple Relay Control
Camera doesn't work with GPIO PIR Sensor
How to run a (java) application at boot time on RaspberryrPi B+?
Can't shutdown eth0 interface
TTL serial connection weirdness
Control sensor: SainSmart TGS-2600
Raspberry Pi disable ssh without screen
Is it possible to power a model B+ via the 5v pins on the GPIO header?
using a SSH and can't login on my raspberry
Motion - grey screen with camera module
Raspberry Pi SSH works fine, but console commands not visible on HDMI output
Supporting multiple monitor EDID override profiles
How long have you run your Raspberry Pi since its inception in 2012
I have tried to connect my Raspberry Pi using the HDMI lead, but it says no signal on the monitor and on the tv
USB Modem rebooting problem
Powering Raspberry pi with 12 volt input
How to share my internet connection on a (Windows) computer with a Raspberry Pi?
Installing opencv (C++) on Raspberry pi and other misc packages
apache subdomain setup
Force 1080i VGA on hdmi output
Good way to start python script at startup with automatic restart if it crashes?
Portable power supply for a PiHub?
Raspistill slow to trigger?
Using the camera with uv4l
What is the maximum number of DS18B20 probes that can attached to one input port?
Sensor to detect water/liquid level
How can I put RaspberryPi to Shut down and wake up later?
Is it possible to make a fully automatic installation of raspbian?
unmount root on headless pi
Optimising raspbian performance for python script
Shrinking partition for backup
Use interrupts in i2C between Ardiono and Raspberry Pi
PiCore not working
Access Raspberry Pi connected to 3G via Internet
Would a Raspberry Pi be strong enough to work as a web filter?
Android on Raspberry Pi
Same SD card working in one PI but not in another
Barcode Scanners compatible with Raspberry Pi
GPIO communication between 2 Raspberry Pis?
how is my IP being set?
Interfacing with a Winbond W25Q64BV flash chip via SPI
contact pin 1(3,3v supply) pin 6(0v ground) reboot
How do I fix this 'transmission-daemon: command not found' error?
Raspbian won't boot
Force IPv4 address
Question about ssh
Cronjobs not working
The Composite Video on my Raspberry Pi isn't working
Is it possible to use the Raspberry Pi to automate backups from Dropbox to an external hard drive?
How can I make sure that wlan0: becomes ready before it tries to get an ip from DHCP on boot?
sleep() affecting only one certain output
Will attaching an Adafruit TFT consume/block all the GPIO pins
Precautions to be taken while using the GPIO pins
RPi B+ not booting and green led flashes 4 times,with 4 different micro sd
Lamp or language best for raspberry pi
hostname.sh ... failed!
Can I use the output of one pin as VCC?
only got 56mb left on 8gb card after RetroPie install
Compiling WiringPi (GPIO input) into raspistill/raspivid
Turning LED light on with Pi
Can the GPIO`s pins be used as another RX and TX?
Power supply for raspberry pi model b+
Installing Tracks 2.2.3 on Raspberry Pi
UPS with battery reading
What is a failproof method for testing a GPIO pin?
Node.js v0.11.14 exits with "Illegal Instruction"
Speed up game ROMs with RetroPie
Netflix on Raspberry Pi (2014 version)
Connect RPi to laptop through Ethernet cable
GPIO Pin 17 does not trigger RPi.GPIO callback
Mount windows share: Bad UNC
Kernel .config necessary options
How to install stripped version of GTK (without *dbg files)?
Starting raspberry pi from button
Develop Raspberry Pi setup on the PC and then flash the SD card?
Wake up 'sleeping' wlan-connection
Best way to stream video over internet with RPi?
change keyboard layout in console
How to get microcontroller connected to WiFi - no keyboard, screen, or native app
Raspberry pi B+ first boot
How to add os manually to berryboot
Streaming Audio and Video from a remote Raspberry Pi to my computer
How do I monitor the temperature ever 3 seconds without entering new commands?
Car computer how to connect to car battery and also not drain battery when the car is switched off
Powering a stack of Raspberry Pis
Picamera taking pictures fast and processing them
USB ports unrespnsive after dist-upgrade
Detect Power Loss in AC outlet
Turn LED on and off with switch
RPi can't connect to internet via Mac internet sharing
How can I save images of the RPi camera on a network drive?
5.3v power source into the GPIO
Can't format my Raspbian SD Card
unable to resolve host
Why don't I get all available packets from apt?
Driving 12V relays from Raspberry Pi
shell creation report boost::interprocess::bad_alloc error
How to control multiple raspberry pi's at once over ethernet?
External USB 2.5" HDD's with the Raspberry Pi B+
omxplayer video position and dimension
cannot connect ssh between wifi and ethernet
Speech Recognition
Run script at bootup
Can't connect to Ethernet port on RPI
Two GPIO-based TFT screens?
Should I expect an error message if booting without SD card?
NFC emulate TAG ID to Keystroke
Will reformatting external hard drive to Ext4 from NTFS speed up data transfers?
Is it possible to add an ethernet port to raspberry pi a+?
I2C receive handler, as seen on I2C for Arduino
How to measure DC current RPi?
How to update multiple Pis at once?
Monitoring Network Traffic
How can you preset the IP address (and other parameters) of a Raspberry Pi?
Change incoming downloads folder in OpenELEC
How can I combine many inputs on one pin?
eth0 interface not starting on boot
Play music stream via node
How to connect a 12V fan sensor wire to the Pi
Mount error (112) : Host is down
Is there a display that can be turned on/off via a Pi?
No Video on 4.3" TFT using RCA composite cable on B+
What's the best way to interface RPi with an Android app?
Read load of battery via USB
Resistor calulation for two LED
may connect 26 pin touchscreen display to a 40 pin raspberry pi A+?
ttyAMA0 disabled but still shows one boot message
Pi Permanent Wiring
External shutdown (properly) button?
What register do I use to control the PWM clock on the BCM2835 used in the Raspberry Pi?
What steps can be taken to use the Pi as mission critical hardware?
Switching power source from power bank to mains without interrupt
What is the best power supply for the Raspberry Pi B+?
Push buttons getting too many events
Can I connect two Linux systems via USB?
Virtual machine from SD card
Problem using startx on raspbian
How to do a repeated start with the Raspberry Pi to get the MMA8452Q accelerometer working?
Why is Python the preferred language for the pi
Can I connect a Raspberry Pi to the VGA port on my laptop, like a projector?
Unstable perfomance with Seagate external HDD
how can i connect to internet via usb dodge of a wireless keyboard?
Rpi+, Volumio, 64gb micro SD and PiDAC+
Create Startup Sound
Headless RaspberryPi Network Login [Proxy]
Determine if running on a Raspberry Pi in Node.js
Settings for Transmission reset after reboot
Using git to version control the Raspi OS
Using Raspberry Pi as a Tunnelbear sharing device
Transmission not reloading after reboot
Change/reset password WITHOUT monitor/keyboard
Finding a relay capable of being constantly switched?
apt-get install/upgrade 403 Forbidden
Hardening Raspberry Pi performance for reliable 24x7x365 use
ssh to raspberry pi with laptop as monitor
9 Data Bits on UART pins?
automatically restart service on boot
Can the Raspberry Pi power this 2.5" drive without a USB hub?
Is it possible to run only the kernel?
Raspberry Hardware simulator to practice on
Executing bash script in python language
ARMv6 Instruction set for getting timestamp counter (TSC)?
Raspbian often boots to a blank screen, however the Pi is responsive and accessible from SSH and the network
I am getting ghosting/bouncing on my digital input
Plymouth on Raspberry Pi
raspberry pi os programming
Can pins 18 and 21 be used to power two DC motors with one L293D
Proper hardware debouncing my interrupt driven digital electrical meter input?
How to connect to a headless Raspberry Pi A+?
How to start up with a raspberry pi b+ with a laptop
Install golang the easy way
Running raspbian from usb stick, does it matter what kind of usb stick I use?
AC 230 V dimmer for Raspberry PI?
RPi B v2.0 P5 header on RPi B+
Default duty cycle of hardware PWM using wiring-pi
Compiling TP-LINK TL-WN725N v2 Drivers - make errors
Is it possible to expand the PWM signal?
How to stream Internet videos (e.g. Netflix) on a Rasberry Pi media player?
Designing Raspberry Pi Compute Module with Ethernet capability
Resolving Windows Shares
Connecting LED to GPIO pin without using jumper wire
How much current does the Raspberry Pi can handle?
Flowchart software for Raspbian
Make 'ifup eth0' permanently UP
Getting started with raspberry pi B+
SSH: connection refused - Server started but sshd not running?
Root access , nightmare when TRYING to learn the basics
Python in the latest Raspbian Wheezy
How can I create a gui for PiTFT?
Make a web server accessible only to specific MAC addresses?
Count RPM/Frequency/Pulses on GPIO ports (Maximum?)
Get Data from Pi without Network
GPIO pins: (3v3 and #pins) not providing power
Raspberry Pi cluster running as gaming server (TF2 modded minecraft)
Arduino to RPi serial Communication
Problem configuring WiFi
Confast WIfi Adapter WU810n for raspberry pi B+
Extend IO pins to 256?
Compile linux device driver in Raspbian
Can't find the right SD card slot
RetroPie no HDMI output and "The disk you inserted was not readable by this computer"
Raspberry Pi backup server (windows & mac)
Driving LED stripes as non-root user
Update Python version on Raspbian
115200 Baud Rate Problem for Raspberry Pi /dev/ttyAMA0 vs /dev/ttyUSB0 with XBee Radios
Drivers for dwa-171 wifi usb dongle
Raspberry Pi B+ not displaying screen
How do you hook up wifi to it? I keep trying and it will not work
Checking all the specific GPIO pins if it is HIGH or LOW and putting it in a CONDITION
Disabling start of services at boot
LED wont light up
Cannot install TightVNCServer
Level shifters for serial communication to an arduino
Error when running a program to test library that write values on GPIO
Problem installing aircrack-ng
Raspberry PI A+ Power requirements
Installation of “monitord” under Raspberry PI
Automatically starting VNC server doesn't work
Apache internal host of repository for Raspberry Pi
Use a servo right from the GPIO without a breakout board
How to Connect Raspberry Pi with GSM sim900a mini rs232
automatically uninstall all non essential packages
VPN - Route some traffic not through VPN
Homemade Raspberry Pi television remote?
How to run 2 scripts together?
Permission denied for GUI operations
What are the Specs of a 2011 Raspberry Pi?
Epiphany Browser is unable to display HTML5 Video
Installing the "Inconsolata" font as the default console font - or any other font
Current draw for +/2/0 models
How should I install drivers for my wireless adaptor on raspi B+ mode?(raspbian OS)?
design a hardware whether to base on arduino or raspberrypi
Remote Connection to Pi to same Display as HDMI Port
Connect DVD Drive to Rasberry Pi and Share
Is it possible to flash the Pi's firmware live?
What is the maximum frequency to count the pulses?
Remapping keyboard
USB wifi won't connect after reboot
How can I test if the serial / UART is good on a Raspberry Pi?
How do I pass a variable to a python script run from crontab?
Power LED is very dim on RPi B+
i2cdetect strange output
Monitor an outlet to see when power switches on and off
Is it possible to create a keyboard shortcut that acts as an on/off switch?
Programming SPI display on Raspberry Pi
wlan repeater ip-address difficulties
What else can I do to maximize the RAM left for my application after all the services are started?
wireless was working but now the adapter isn't even recognised
Edimax 8192cu wifi dongle can't connect to hidden network
insmod segmentation fault error each time I insert a basic module
Popcorn-time or other media streamer
Cannot get IR-LED transmitter to work
Modern way to stream H.264 from the Raspberry Cam
Unable to send file from Raspberry Pi to my system through SSH
Pi B+ as a 24v motor controller, code written in C#(Mono). Power concerns
Why do I have to "flash" the operating system onto the microsd card. Why can't I just copy and paste?
Can there be an active input to the pi's GPIO before i/o set-up?
Will any external battery power a Raspberry Pi?
Can I record a 24 hour video on the Raspberry Pi with camera module?
Access denied when starting systemd service
noise on the analog jack shadowing the RPi activity
Which addressable RGB LED strips are beginner friendly and Raspberry Pi friendly?
Do we need to put i2c code into kernel?
I'm looking for a serial input type "polychromatic" LED as an output for my raspberry pi. Does such a device exist?
How can I get a clock in C accurate enough to control a servo?
Why are blue LED's glowing brighter than green and yellow LEDs?
Simple DC Solenoid Valve Circuit, How to size components?
Wifi stops working just after unplugging rj45 cable
Kiosk Webclient
Auto startup of the Midori web browser is not working on Raspberry pi
Best way to create a web frontend for Python-based automation project
Wifi on Raspberry Pi b+
How can a read-only SD card get corrupted repeatedly?
Will a Duracell 9V battery power my Raspberry Pi for 24 hours?
3V3 to 5V logic level shifter - looking for alternative to 74AHCT125
PiCamera not Working
Possible to reinstall X server and use graphical after having removed it?
Theoretical maximum data rate of GPIO pins
Programming a non-audio headphone jack peripheral
Can I get better performance on Raspbian if I blacklist a lot of kernel modules in raspi-blacklist.conf?
Raspberry Pi remote desktop
Wifi troubles on RPi A+
Output power of the Raspberry Pi Transmitter
How to install emacs24.4 on a Raspberry Pi Model B+?
Broken pipe when SSH using Mac OS X
Would a powered USB hub for Model B work to power Model B+?
Kernel not updating on Raspbian under QEMU
Connecting Raspberry Pi (running Raspbian) to open WiFi using only the command line
what would be the simplest way of reading about 50+ gpio inputs?(momentary buttons)
Why my Raspberry Pi cannot find Si7021 (temperature and humidity sensor)?
Node.Js on raspbian not found with Sudo
Headless wifi configuration ( AP mode )
How to create an GPIO event loop with C (Or Objective-C)?
Multiple Display Screens
Shutdown RPi by plugging power (SD card mounted read-only)
How is Raspberry Pi "open source" if it uses ARM?
Has Anybody Built A Raspberry Pi Inside A Mouse Yet?
What is the resistance of the GPIO outputs?
Raspberry Pi remote connection using Xming and putty
record and stream video from camera simultaneously
Can I use Raspberry pi as NAS with Raid 1 and encrypted file systems?
Soil moisture sensor compatibility
My speakers don't work on my raspberry pi but my headphones do. Why is this?
Firmware 3.18.x breaks I²C, SPI, audio, lirc, 1-wire (e.g. /dev/i2c-1, No such file or directory)
kodi (xbmc) on raspbian can't activate keyboard or mouse
How to stream raspivid to Linux and OSX using GStreamer, VLC or Netcat?
External FDX and LNK LEDs
How to make folders writable?
Flashing raspbian-netinst image results in "Superblock last mount time is in the future."
How to SSH into rPi in this setup/config?
Ant and termite detection using PIR
loading programs onto SD card and installing. No Network
How Can I Uninstall Shairport?
How to hook up an AM2302 temperature & humidity sensor several feet away from the Raspberry pi?
why two RPis show quite different ntp results?
Cross-compiling with Windows using Eclipse
Issue with MT7601U usb dongle wifi driver
Using Ralink RT5370 on Raspbian is causing hangs and kernel panics
Automatic mounting of NAS drive fails
spidev.xfer2 in python gives IOError: [Errno 22] Invalid argument
Controlling a continuous servo with raspberry pi
installing OpenCV 3.0 on raspberry pi b+
SSH host unreachable on PI
Python script always throws exception the first it is ran after reboot
How to control omxplayer via LIRC?
New Raspberry Pi B+ is dead after 30 minutes, any ideas?
Is the new raspberry pi 2 software compatible with the old raspberry pis?
Do the GPIO registers have the same addresses on the new Raspberry Pi 2?
Raspberry Pi NoIR hangs. Only a physical power off solved
Cloning SD card on the raspberry pi
OpenELEC and Kodi 24/7
Edimax EW-7811Un Frequently Drops SSH Connection
Looking for Optically isolated input board for Raspberry Pi
New Raspbian(Pi2) Image on Model B
Is there a 802.11ac dongle with drivers ready for the raspberry pi?
Playstation 2 emulation
Does Raspberry PI 2 supports H.265 hardware decoding?
Why is my Raspberry Pi 2 with OSMC slow?
Problems with installing Node.js NPM package
Unable to find a compatible palette format
VPN Not launching on boot
Cannot update Arch Linux
Raspberry Pi GPIO pins stuck high after using L239D chip
Cron for Raspberry Pi
Getting "sh: can't access tty; job control turned off" with fresh NOOBS
Streaming from RPI over VLC
Faster Way To Transfer Video FIle
Raspbmc not booting on Pi 2
libCEC not working on LG TV (LD330)
ImportError: No module named GPIO
TL-WN725N v2 WiFi adapter not working on Raspberry Pi Arch Linux
Minimize Kodi to run full screen X on OSMC Alpha 4
Configure Xbmc/kodi via command line
Recording Temperature and Humidity Data to a Memory Stick
Do I still need to purchase the MPEG-2 and VC-1 license keys for the Raspberry Pi 2?
Power regulation circuits on B+ vs 2 (light sensitivity)
Odd ethernet problem - slow write speeds
Will gcc produce ARM7 code
Streaming From Pi Camera Module
Raspberry pi 2 1024M Increase Gpu Memory to 512 at least
DS18B20 Sensor not detecting
Where is cmdline.txt located on the NOOBS SD card?
What is windows 10 like for the Pi 2?
WiFi disconnects after period of time on Raspberry Pi, doesn't reconnect
cannot connect to mirrordirector.raspbian
Raspberry pi power cable is unstable
MPU6050 gyroscope not responding
How to install and use GStreamer on latest Raspbian?
How To Start Learning Python For Raspberry Pi?
Samsung Multifunction Printer with CUPS failing to print
How can you mirror the raspberry display?
Raspberry not booting w/ older Raspbian Release (only Red LED)
Upgrading from Pi to Pi2
Can I use Fedora on the Pi 2?
Is it possible to connect to a display port?
How do I delay transmission-daemon startup until all shares are mounted?
Dropout Wi-Fi USB dongle
Raspberry Pi Ethernet port not working after thunderstorm
how can I install php5-readline in Raspbian?
How to run the NTP daemon automatically?
How can I send commands from Arduino to raspberrypi
Does a browser exist for the Pi 2 that supports both WebRTC and HTML5 Canvas?
Raspbian: Start X11VNC on boot
Raspberry pi as public web server
Boot from usb if available
/sys/devices/virtual/gpio dissapears after installing RPi.GPIO on Archlinux ARM
Epiphany & Proxy Server
How do I discover and control what channel my WiFi adaptor is running on?
Auto start TightVncServer on Raspberry Pi 2
How to set up visual studio to write programs for the Raspberry PI in c/c++?
Automatically restart Tomcat on system reboots
How to install Waveshare SpotPear 4 inch LCD in RaspberryPI 2?
Is the Docker framework planned for Snappy Ubuntu Core on the Pi 2?
Powering several LEDs from GPIO output
DS18B20 temperature sensor not registered - debugging?
Raspberry Pi failing to read sensors in -20 degree F
How can I access to /etc/network/interfaces in my sd card?
Command apt-get upgrade crashes Raspbian
sudo apt-get update problem
Upgrade to Raspbian Jessie
Creating an Android "remote" app for Raspberry Pi (Raspbian)
Can I have multiple Pis chained together?
Can I run a terminal command from ssh to open the browser on X server?
Utilising extra memory on SD card
USB power cycling problem
Unable to connect Seagate external drive
RaspberryPi 2 and GitLab: "No such middleware to insert before: ActionDispatch::Static"?
How to change gpio directory for node.js pi-gpio?
Internet and Remote Acess via Wi-Fi & Ethernet Cable
Cron error with Python script
Raspberry Pi static IP address Ethernet timeout
Assigning write permissions to a group
Raspberry Pi as USB serial device
Is there a way to see if a GPIO pin is on or off using the python RPi.GPIO module?
Power led randomly blinking every 1 minute on b+
RPi b+ randomly close the browser on a few
Driving mini stepper motors from raspberry pi
Building a Raspberry Pi network monitor. My code is not working
Pi 2 CPU Documentation
can't ssh to pi via wlan0
Can I connect 2 pi's together via Ethernet cable?
Disable Raspi-Config
How to create a shrinked image of my working Rpi SD card
How can I modify interfaces file of Snappy Ubuntu on raspberry pi 2?
How can I quit omxplayer in full screen?
Will I be able to install the latest version of Chromium or Firefox on Raspbian?
Where can I find good Open Source UAV software for a raspberry pi?
GPIO is not working, 5V working, 3.3 V working, Raspberry Pi B+
can't install npm onoff on raspberrypi
Raspberry Pi 2 ITX motherboard conversion
TightVNC connection refused
Raspberry Pi 2 - Model B - no boot with Raspbmc
Rasberry pi noobs sd card shows /dev/sdb6 with fdisk when there are only /dev/sdb and /dev/sdb1 exist?
Receive FM Radio on Raspberry Pi
Python and OpenSSL error on import
Install NZBGet on Raspberry Pi 2 on OSMC
Rasclock does not store the time
Raspberry Pi starting programs automatically on startup
Retrieve RTC time from DVB-C
Safest way to switch off uncleanly
Take snap from Raspberry pi using motion
RPi HDMI to RCA
dd for image backup
Raspberry Pi Frozen
Developing for the Raspberry Pi
What happens if I try to read an analog pin's value?
EDITING RC.LOCAL for NZBGet and Sickrage at startup on OSMC
Cannot ssh via ethernet, but can via wifi
LAN on RPi2 not working
Fastest 2-to-1 simplex connection of 3 pis
Python script with loop that detects keyboard input
Multiple (dumb) wireless buttons to one RPi
DWA-171 using 8812au.ko does not seem to work on Linux kernel version 3.18.8+
Can you use a micro SD card from raspberry pi B+ on the raspberry pi 2 model B?
What's the problem with backfeeding?
Raspberry PI 2: Installing mysql-server
OSMC has mounted 2 versions of my External HD
How to safely do a headless Raspbian install with WiFi only network
What do I need to do to stream two USB webcams with my Raspberry Pi B+?
Pi2 won't start when connected to breadboard via ribbon cable and gpio-to-breadboard interface
Load limit of Raspberry Pi 2
"Inappropriate ioctl for device" error since upgrading Rasbian & firmware
What are the possible OUIs for the Ethernet MAC address
How to control pi HDMI output from laptop via VNC
Glade UI Python serial read loop
Run a minecraft server at boot
Recover Console Text Output after Using fbi App to display image on /dev/fb0
Can you use a Raspberry Pi to write code that powers an onboard LED or motor or fan?
code works on windows laptop but not on PI
Comfast Wifi Adapter WU810n - Raspbian
Raspberry pi camera module very slow with SimpleCV
Can I view/copy the contents of an img file from Windows?
Is there a way to shut down safely without being logged in?
cgps : GPS timeout
Writing OpenELEC Image on top of NOOBS
Is it possible to use a Pi to "look" for other devices on the same network?
Running a JAR file in Pi results in following error "can't find the main class"
Problem when transferring to a bigger SD card for my Raspberry PI 2
New PI 2 B+ unusably slow, CPU and RAM not being used?
How can I connect am RPi A+ to a Macbook Pro with a USB/Ethernet adapter?
Unable to see Temp sensors at /sys/bus/w1/devices which was working until SD card got corrupted
Controlling kernel interface 4DPi-32 display
Raspberry is not booting up
Raspberry Pi 2 - Are 64GB UHS-I Class 1 SDXC cards supported?
Python Script Stops Running After about 3 Hours
Is there a Win32 Disk Imager equivalent, or an easy way to create .IMG files with a GUI on Mac OS X?
Is the 26-pin Pi cobbler compatible with the 40-pin Raspberry Pi?
How much power can the Pi supply?
Extremely slow wifi, wired connection is fine (OSMC)
Timestamp of the image being captured?
Qt for Raspberry 2
How can I wire this SD card reader to RaspberryPi?
Reading GPIO status only works outside of PHP if statement?
SSH keys not working on OpenElec (login without typing password)
Is it possible to make Javascript interact with the GPIO pins?
Noobs boot - no other systems visible internet connection through WiFi
Installing an ISO from USB
How does the Raspberry Pi differentiate between multiple expansion boards?
Should GPIO pins 13 and 14 be soldered together?
rc.local only runs manually, not on boot
Why doesn't GPIO commands work?
How to get a read-only Raspbian not to corrupt SD on power-loss
Underclock raspberry pi without rebooting
Can't login via SSH after restart
Using Wi-Fi Adapter reboots Pi
Run two python script automatically on Headless raspberry pi project
How to change the default baudrate of raspberry pi's serial port?
what if my charger output is 5V 750mA for pi 2?
What is the meaning of put a docker in the PI?
Taking advantage of multiprocessing with OpenCV on raspberry Pi 2
TV probably doesn't have HDMI CEC - Unable to control OSMC on Pi 2 thru TV remote. Help
Struggling with installation of Raspbian on SD card from a Windows 8 machine
Raspbian Jessie - How do I properly setup A2DP with Bluez5 and PulseAudio
Host Authenticity is questioned in terminal while trying to SSH
Pi / Pi 2 using modern 'smart' USB Power Adapters to supply power to the Raspberry?
Is there any way that you can receive radio signals on your raspberry pi?
I2C LCD detected, code runs, but no display
Locally static IP address
Setting up wifi on network with no passkey
433 Mhz transmitter on RPI always sending 00000000
How do I compile gcc 5 for my Raspberry Pi 2
How could one automate the raspbian raspi-config setup?
Edimax EW-7811UN not detected by Pi, works fine on a PC
Is raspberry pi 2 model B a good candidate as a "Download Box" or NAS
How to get the most out of the raspberry pi 2 GPU?
How to connect 7-segment 4-digits display with Pi?
ptxdist and Rpi
Why Raspberry Pi camera "no device found" in Cheese or IceWeasel?
I2C not working as expected
Multiple partitions on Raspberry Pi memory card
How to make ssh process not end when connection is lost
Unwanted multiple presses when using GPIO button press detection
Simplest way to play videos stored on a NAS
Resetting I2C? Or did I break my chip?
How to blink LEDs on/off continually, while continuing execution of a script?
How can I use a LCD display with a I2C adapter?
What software do I need for Raspberry PI 2?
Which version of java to install on PI?
Is there a way to Mirror the HDMI TTY Terminal over the Network (i.e. Not Desktop and Not SSH)
Static over composite audio
How should I properly communicate 2 Raspberry Pi via UART?
Can't run python script from cron
Locating I2C pull-up resistors for RPi2
Raspberry pi always stops responding to SSH after some hours powered
How do I make a copy of a NOOBS SD card?
Raspberry Pi not getting DHCP lease
Move (not sync) files from Raspberry Pi to some cloud solution
Pi 2 Model B, display and TNC-Pi
Process terminate with SIGILL using valgrind
Modular Raspberry Pi Model
Screen Flashing
Not able to fetch register values using Mike M's BCM2835 C code
System information on ssh-login suddenly disappeared?
Keyboard and mouse stopped responding in GUI after apt-get upgrade
Stuck in boot after trying to work with init.d script to run at boot
Access pi from the outside
Re_expanding the SD-Card after raspberry pi start-up
Can I use a standard PC power supply to power a Raspberry Pi?
How to force rsync upgrade
MongoDB on Raspbian
Copy Protection, Intellectual Protection and Deployment Issues
Data collection from raspberry pi and send to computer (without using Ethernet or Wifi)
Detect stall current from motor and send gpio signal
unable to change wlan0 mac address on raspberry pi 2
Can't access motion server
Maximizing the performance + life of an unsupervised RPi
Is there any versions of NWJS and Atom-shell available for Raspbian armhf?
Why is my Webcam image all black?
Raspberry Pi 2 Model B 1GB not booting - RED and GREEN leds on
which windows 10 is for the raspberry pi 2?
Raspberry Pi 2 b+ + windows 10
How to make backup Raspbian image?
How can I add another Operating System onto NOOBS?
Share Raspberry Pi writable folder on network
Paper printable case for Raspberry Pi 2?
What are the RUN pin holes on Raspberry Pi 2?
Determine current download speed using ssh on Openelec
Keep process running after close session
Raspberry Pi and Amazon Cloud Drive, is that possible?
Is it correct to power the Raspberry Pi this way?
Python taking pictures with raspberry pi camera
Strange IP connected to ssh?
Using Python to control the Raspberry Pi Camera
Compiling TV Card Drivers on Raspberry Pi 2
Permanent Fix "error in check_disks" on reboot
When i set the GPIO pin as output in my python cgi script, after that line my browser does not execute the cgi script. Why?
Soil hygrometer without adc
Bad performance transfer file with samba
Changing the aperture of the raspberry pi camera in python
Native C access to wiringPi from PI4J
Raspberry Pi: ssh connection refused
Drivers for TP-LINK TL-WN723N v3
Motion filming can't get on real speed
ruby on rails in RPI
Can't get GPS to automatically work after reboot
Kernel Configuration for CAN-Bus
Persistent rainbow test pattern
nginx on raspberry pi
How to have a Raspi trigger a Remote Control physically
USB camera compatibility
Snappy Ubuntu - reasons?
What is Iced Web Control Panel
SSH into my Raspberry Pi 2@Optimum WiFi
How to relogin to same session
How to change the clock to 12-hour format in Raspbian?
Rapsberry Pi Mini-fan not working
Samba and usbmount: can't write on automounted device
Power Raspberry with LiPo battery
Raspberry Pi Recognizes Logitech C920 Webcam But Can't Do Anything
Can we determine the mode of a GPIO pin?
No internet access when using wireless
How to setup Network Manager on Raspbian
New to Raspberry Pi -- Won't boot after a shutdown -h now
Power Bank + raspberry pi 2, any throughts?
Have images for Windows 10 IOT been delivered yet?
Cross-compiling to Raspbian
RPi can't access files stored on USB-drive from CLI
How do I upgrade to Mathematica 10.1?
SSH terminal plugin for OSMC on Raspberri Pi
Cannot connect to RPi with SSH
How to build Native WebRTC?
Android can't find Raspberry Pi with Samba/ Zeroconf Avahi
Advice on 3.5inch GPIO Touch Screen
Is it possible to install pcsc-lite 1.8.13 on raspbian OS?
Pi boots to a white login screen instead of desktop after making tightvncserver boot at startup
What is the difference between running Linux a Raspberry Pi VS a regular system?
Powering the Pi with 2 AA batteries
Raspbian wpa_supplicant fails, which service to (re)start?
VGA to HDMI Converter
Can I stream video call from pc to pi?
Raspberry not working though ssh and cannot mount with usb
How to make Wi-Pi work?
Raspberry Pi passwordless SSH - refusing key
Service like TeamViewer for Raspberry Pi to access without IP
Port forwarding router for outside local network access to pi
Pigpio initialization failing with init mbox zaps failed
What firmware version will rpi-update install?
Official Resellers of Raspberry Pi Boards
First Time Boot Screen Configuration
Camera Interfaces can be used with Raspberry pi
Is it to possible to have parallel access of Pi's camera to take stills, when it is streaming through FFMpEG video streaming?
Safely transferring specific content from a raspberry pi to my mac
Raspberry PI not booting Snappy Ubuntu Core
How do I retrieve data from another Pi on the same network?
Raspberry Pi Raspbian Multiple Desktops
Control Pi Audio via bluetooth from phone
Mobile power source for RPi?
Make VNC login as User Pi rather than ROOT
Raspbian OS vs. Mainstream Linux distributions
CPU Performance Graph
Epiphany Browser in full screen mode
NOOBS Where is Config File
Is it possible to install the Plex Media Server on the Raspberry Pi?
What non-viral-licensed free open-source OS to use?
Connect raspberry pi to pc (ubuntu) with ethernet
Why do I have to connect from my RPi via ssh to another device, before I can connect to my RPi from that device via ssh?
OSError: libportmidi.so: cannot open shared object file: No such file or directory
SSH freezing randomly
Extend my project to multiple remote Pis
GPSD Data Receiving Issues
Can the Pi run an embedded RTOS other than Linux?
Need more Space, deleting other distributions, how?
RPi.GPIO under Python 3
Arduino sends different numbers over serial to Raspberry Pi than Linux/Mac
Compile linux module on Raspbian error
Is it possible to make the raspberry pi add to current cpu of ubuntu laptop
Ideal etc/network/interfaces file for static IP ethernet AND wireless
How to disable a GPIO pin?
How can I convert a .img.xz file to .img to transfer it to my SDCard?
remote deploy .NET on Raspberry Pi 2
Autoremoved certain packages from raspberry pi
How to make 3.5" Resistive Touch Screen Usable
Do Google Play Apps Work on the Pi
Terminal command will not execute after boot
Where is the Raspberry Pi 512 MB memory located on the board?
Create a home network monitor
Streaming the video being recorded to remote computer?
Raspberry Pi streaming without being connected to Monitor or TV possible?
Controlling 64 parallel LEDs using using Raspberry Pi
Pi nRF24L01+ error
Timeout issues with Raspberry Pi 2 on network
Cannot open 12V Solenoid Valve
Unable to Find RPi on Network w/ New Router
Trying to turn off X11 in Jessie
How do I make a linux image which is of my current system?
Best way of communication for embedded RPi
How is a Raspberry Pi different from an old phone
How to connect Relay module to a Power Strip Outlet
Raspberry Pi has two ip addresses
Random Freezes on B+
What instruction set is used on the Pi's ARM/Broadcom chip?
What file is responsible for the login script
Raspberry Pi 2 flashing Rainbow Screen during setup
GPIO Signals Over Long Wires
What are the possible ways to control raspberry pi over internet rather than static ip?
Network doesn't work, new raspbian on pi2
SPI Interfacing of MCP3903 with Raspberry pi Python Library
Problem wpa_supplicant rapsberry pi 2
Picamera Module not imported?
WiFi turns off automatically on raspberry pi
Is it possible to install gns3?
Is it possible to wirelessly turn the raspberry pi on/off?
Why is Real Time Software an Issue?
GPIO Pin Explanation
RaspberryPi (Rasbian) name resolution does not work in a non-internet network
OTA Update of Multiple Raspberry Pi's
NRF24l01 Raspberry Pi and Arduino
What is Mathematica for?
Securing GPIO groups vs gpio-admin
Reconnect of multiple RTSP streams on omxplayer and screen
Ethernet and wifi together
Raspberry B+ remove USB ports
Can I login using something other than a password; i.e. a keypad using GPIO pins?
/dev/null folder doesn't exist. Should I create it?
Measure the frequency of a 555 timer
Add more than 2 SPI slaves
Use a USB MIDI controller as an input
Internet connection with SSH
Functions and limitations of Windows 10 IOT for Pi 2
How to install Programs on Pi Without Pi Store
Raspberry pi Model B - Control a mini fan
Wifi raspberry pi 2 problem
Electronics of a water pump
Cellular Modem Data Usage
Is the Raspberry Pi suited for sensor and voice recognition project?
Is Raspberry Pi 2 better than Raspberry Pi B+ for controlling RGB LEDs via software PWM
how to start xclock (or something else) to be displayed on my HDMI device on Raspbian console session?
Why does shairplay quality on raspi decreases when using system wide airplay?
Controlling a fan on a relay with python
Can I use the 3.3v pin instead of the 5v pin?
Read-write filesystem + no problem when halting the Pi by removing the power cord?
Set up my Raspberry Pi B+ with my using my laptop's keyboard and monitor
Can a 10 node raspberry pi cluster use a single hardrive as storage
Emulating raspbian with QEMU
Can the Pi Emulate an HID device with via USB?
How do I write the RetroPie img file to my SD card?
Is it possible to have separate settings for composite and HDMI video?
RPi restarts when driving 28BYJ-48 (ULN2003) stepper motor through LM2577 Step-up converter module
Run code on Raspberry Pi without gui
How do I do an internet speedtest from CLI on Raspbian?
File Transfer Problems
Realtek RTL8153 Ethernet Doesn't work on Arch Linux
Is this possible to read internal CPU temp sensor directly from cpp code?
Performance of a raspberry pi as a firewall
What would I use to let me use the GPIO pins on my RPi without soldering directly onto the pins & without a breadboard?
Max number of RC motors controlled by Raspberry PI
Trying to install Wolfram Mathematica on Jessie
Safe shutdown button not working
Fail to load Chromium with URL
Self healing SD Card partitions
How to create serial cable for Paspberry Pi with arduino micro?
Windows 10 IoT on RPi2 as a small HTTP / REST Web API Server
SSH into Raspberry Pi with 3G modem connected
Is my code too intensive on the cpu?
How to increase the camera exposure time?
Simple temperature monitor Raspberry Pi 2 + GPIOs with DS18B20 on WIndows 10 Universal App
Are there any wifi/bluetooth combo adapters that work with the Pi?
How to diagnose problem with OpenCV face tracking
Red LED blinks twice on boot with 5V/5A power adapter!
Problems FT5306 USB Touchscreen
Connect GPIO output to second Raspberry Pi input
reboot raspberry remotly from webserver
Error when running pyaudio test file
Is it possible to setup a wireless file server and access the drives from a Windows PC?
Not able to use Raspberry pi as a FM transmitter
Why does the Raspberry Pi not have a power button?
SSH not working
Power and Internet over a 15m distance
Multiple IP addresses being assigned
How to make a high powered USB hard drive work with the Pi?
all commands in raspbian terminal stop working
rPi2 + Sandisk Ultra/Extreme plus/Extreme pro: would it work?
Is it possible to power 2 devices using a powerboost charger?
How to make the Raspberry Pi consume less power
Are there any damaging effects to leaving the Raspberry Pi on all the time
How did the Raspberry Pi get its name?
RPi2 raspbian I2C error - BMP180 sensor
When using display_rotate=1 half the screen is black
Issue scheduling a task in raspbian to email my out facing ip
On OSMC, how do I get to NOOBS?
Raspbian image based on Debian 8 (jessie)
Timezone correctly set but incorrect output
SSH to RPI using android hotspot and PC
Why are some GPIO pins HIGH when the Raspberry Pi boots up?
Large Monitor on Ubuntu Mate
Do I Need To Replace My Raspberry Pi Camera?
How to get write access to an sd card which already has an image burned onto it.
Setup microphone stream and turn your raspberry pi into a baby phone
Change default HDMI mode of monitor output
Connecting a SainSmart 9-in HDMI Touchscreen?
Audio amplifier hardware
Adafruit FONA 808 GPS
can't load IA 32-bit .so on a ARM-bit platform
When is it safe to switch power off after halting Pi
How can I install PHP 5.6 (instead of 5.4)?
Using my Raspberry Pi without HDMI TV
NOOBS preloaded SD Cards and OSMC
Can I determine the MAC address without booting up?
Save an image of a RPi thats booting from a hard drive
Where are the python picamera docs?
How to resize epiphany web-browser
RPI 2 B freezes when Wi-Fi dongle is inserted and doesn't detect it
send gpio commands from rpi python script to another rpi
How to configure pi to preferentially choose network adapter on startup on Raspbian?
Latency variation
Plug a 5 V fan to GPIO 1 and 2
How to debug crashing Pi?
Error on sudo apt-get update
crontab job not working properly
How do I connect a raspberry pi to a hidden network with no passkey using a static ip address
Using a raspbian image, on various raspberrys
How to mount NTFS drive on a Raspberry Pi B
Can't get VGA monitor to display anything with passive adapter
Script works on laptop, but not on PI
Is there a program (like Filezilla) to transfer files by schedule to the Raspberry Pi?
How can I terminate program running continuously via rc.local?
Output text over MIDI to DX7
TL-WN725N not working
Cron job doesn't work, but runs successfully manually
Pi camera synchronization
"Purpose of "" 127.0.1.1	raspberrypi "" entry in file /etc/hosts"
Raspbian, no audio HDMI, have tried all the troubleshooting I can find
Ridicoulus File Server performance
Buffering issues with kodi (on openelec)
/etc/network/interfaces missing on Raspbian
Distributing a Raspbian image
Can't edit files on SD card
How to read Analog 5V sensor ouput with Digital 3.3V GPIO?
New Project: Video intercom using two Pi's/cameras (with separate audio)
Setting a homeserver with Rasberry PI 2
run tunslip6 on bootup
Modifying "hosts file" on "Windows 10 IoT"
How to Add Delay at Boot
Auto start timer program with remote overide
SSH into Pi using Laptop Screen
SSH to raspberry Pi with Ethernet connection through wifi
Cannot open "idle" in root mode using python
HDMI switching Board
Raspberry Pi 2 + WD My Passport (external 2.5 USB 3.0)
nginx 1.9.2 on raspbian
Raspberry as dialin-server
Problem in connecting to Wi-Fi ,what is PSK?
Not booting when wifi is plugged in
Is it possible to control a stepper-motor with javascript?
Raspberry Pi2 not booting when I reference the USB drive by UUID (works fine when using /dev/sda1)
External SSD or External HDD more suitable for Raspberry Pi 2 Model B?
Share Raspberry pi's internet through router
Is it possible to trigger 10 (or 100) Raspberries to take photos at the same time using WiFi?
Log in to Pi static IP, but no monitor
8 Bit / 256 Colors
How to view outputs in a terminal window of a Python application launched at start-up?
Calculate Raspberry led strip's power need
Is there any "industry standard" for single-board computers?
Touch friendly OS or desktop environment
need an opinion for portable power
How to power Raspberry Pi 2 B with a powered USB hub that also powers peripherals?
Mount exteral drive on startup RPi 2
Develop a Raspberry python script from a windows
How do I add a task to Crontab
Do I need a resistor while connecting a Raspberry Pi to a breadboard?
Are there already "official" DSI screens available?
reconfigure locale failed
How to install NoMachine (NoMachine.com) on Raspberry 2
Help on powering 3.3V fans
Raspberry Pi 2 does not start SOMETIMES
Wake up Windows PC via USB event from a Raspberry Pi
Rotary encoder/monitoring multiple pins with Raspberry Sharp
How to connect a 24V input to my GPIO?
How to manually start uv4l MJPEG stream for embedding in a web page?
Connect to Raspberry Pi over ssh: connection refused (from putty)
Transfering mp3 files from a remote server to the RPi via cronjob without overwriting
Where does the Raspberry Pi store its network configuration?
HTML5 Video options
Access Raspberry pi (connected to Router) using hostname in Browser
Read status of power led using sysfs
Cannot install Puppet 4 on Raspbian Jessie
Running idle, with root privileges, while using TightVNC Server
Using I2C in C++ on Raspberry Pi
Can I design the program via JAVA on PC then transfer it to a Raspberry Pi?
OpenElec on raspberry pi 2 B struggling to play 1080p
Pi draws too much current
How can I put in the "@" sign on your Stack Exchange log In from a Raspberry Pi?
what app should I use to run a slide show on the HDMI out?
Replace /boot/cmdline.txt on RPi2
Raspberry Pi 2 will not boot Hyperion
Use laptop screen without dismantling the screen
Accessing a Pi connected to a router via windows
Raspberry pi location detection
Upgrading from Pi B+ to Pi v2
Infrared detection
Wifi cuts out after a few hours, have to restart Pi
Securing the PI against an attacker with physical access
Can't apt-get install libssl-dev
Powering Pi from Ni-MH batteries
Installing Kali Pi using all available storage space?
Install PHP 5.6 on Raspbian version 2015-5-5
PHP or jquery to execute python scripts for GPIO
Unable to test SPI interface
Arrow keys output scancodes in ucblogo
Pure Python vs. Django for Web Services?
Can't connect to the Pi after cloning the SD card
Raspberry Pi's Power LED does not light, heat and no boot!
Kernel log ONLY on serial console (UART)
using wiringPi and bcm2835
How many DHT22's can be connected to a RPi?
RPi not visible from LAN but works as an AP
The power LED will not light- power supply is fine
Can RPI be connected to 3G network 24/7
sudo without password: More of an issue on Apple?
Issues connecting via ssh to raspberry pi
How can I make my raspberry PI like the one that was sent into space?
Suddenly unable to get usual static IP over wifi
Multiple webcams on a single Raspberry Pi
configure setup to install apache, php, and then copy in /var/www/
Use /boot/cmdline.txt for creating first-boot script
RPi web browsers that work on YouTube
Can I execute a script before every login
"shutdown now" or "shutdown -h now" to power off Raspberry Pi?
Make a Raspberry Pi reliable on remote place
I am attempting to create a WiFi gateway
Error installing OS with Noobs
SPI library installation error
How many buttons at once?
Adafruit 16x2 LCD not displaying properly
Raspberry Pi shuts down when not in use?
Attempting to ssh from Mac Terminal
Is it possible to shut off a Raspberry Pi 2 b using the GPIO pins?
GPIO - RuntimeWarning: This channel already in use, continuing anyway
Can the raspberry Pi 2 B be used as a media centre?
Raspberry Pi 2 wont turn on, just blinking green
Python Serial library for RaspberryPi2 tutorial/command list
Automatically copy files from Raspberry Pi to Mac
How to read Wiegand card ID?
Raspberry Pi jumper
Grab HDMI/VGA in video feed
Connect to public wifi hotspot
How likely is a Pi to be damaged when it is plugged out
Can I use Raspberry Pi in commercial production?
Is it possible to install or move my installed Linux to another partition?
Upgraded to Pi2 - no network connectivity
PowerShell can't connect to Windows IoT
Emulating a bluetooth from a Raspberry Pi
Raspberry Pi USB microphone 1 Khz background noise interference
gpio library on windows while developing
Raspberry pi stops process after a few hours!
SSH into Pi, why static IP 169.254.149.192 always?
I accidentally deleted the Wifi icon on my desktop. And now I can't find how else to connect to a network. Can you please help?
Cannot get graphical program to start up on boot
Can zram improve performance when running RPi2 OS partition from USB?
How many simultaneous users can a Raspberry Pi handle?
Cannot install code blocks on Raspbian
Emulating a keyboard with the Raspberry pi Issue: Bluetooth instance has no attribute 'cinterrupt'
Timeout when connection to a page but ping works?
Temperature Sensor for use with Nagios
Raspberry Pi's clock and perfect timing
Special characters show as question marks in the shell
Need to connect 60 input LED and 60 switch
Reading incoming voltage
Programming servo - What to use?
Wifi adapter detected but doesn't work
White screen on touchscreen display
model B+ config and ssh without mouse and keyboard
How to upload program from web server to Raspberry Pi?
Undervoltage rainbow despite good power supply
Can I re-use the GPIO pins that are driving an LCD display?
PWM on Raspberry Pi 2 and Windows 10 Core IoT RTM
Raspbian without a GUI and other programs I don't need
Install older kernel (3.6.11+) on Raspberry Pi 2
Android on Raspberry Pi 2
Where is the best place to share RPI Image files?
Windows 10 WiFi Adapters
Why cleanup the GPIO pins?
SPI SDA GPIO Rspi
Can I use usb port for display purposes?
Which port of Debian Jessie to install on Raspberry Pi 2?
What bare minimum knowledge should I know before working with hardware on the Raspberry Pi?
Minecraft Pi Edition Performance on Pi2 Compare to Pi1?
Does Windows 10 IoT support Java on the Raspberry Pi 2?
How to use internet in raspberry pi when it is directly connected to my laptop via Ethernet cable?
GUI on HDMI monitor doesn't work after installing the LCD display drivers
Can't get a CIFS network drive to mount on boot
Raspberry Pi 2 not booting connected to network
SSH Internet Connection
Does Minecraft-pi Require an Internet Connection
Picamera stream frame
How do I use different DNS with multiple networks?
Can I safely remove non-free software on a Raspberry Pi 2 running Raspbian?
Testing Raspberry Pi scripts on a PC
Raspberry Pi not booting and all LED is dead (also the red LED)
ERRORS when Installing mongodb on the pi
Raspbian/Octopi and the TL-WN725N v1 wifi adapter; drivers included?
Connecting WS2801 LED strip to my Raspberry Pi
Raspberry pi model b waveshare spotpear 3.2 inch lcd touchscreen is not working
How can I avoid wearing out flash memory by frequently changing symlinks?
Python, Pi Camera and Keyboard input
using try-catch to catch gpio interrupts
I need help powering a raspberry pi by a solar panel
Real Time Clock Module Will it fry my pi?
Control physical switch with raspberry pi and read the state of the switch
how to connect to the Raspberry Pi through 3G dongle?
Does a Raspberry Pi 2 Model B (quad-core ARM Cortex-A7) have 4 program counters?
Using a keyboard/mouse with an xbox 360
Safe operating parameters for GPIO pins
I want to get tor-browser-bundle to run on an RPi2 B. What OS can I use? What are the steps?
How to backup Pi microSD card intelligently
Python run script in new console on startup
Is it possible to build a Raspberry Pi yourself?
I get error while installing Raspbian
Pip exception while installing matplotlib on raspberry pi
Missing 'combined' file in '/sys/module/i2c_bcm2708/parameters' directory
Increase raspberry pi voltage
how to ensure that burned sd card image will work
Raspberry Pi 2 stuck on rainbow screen
boot up rasbian into gui program, no interaction
How to connect the Pi to a PC?
Is raspbian for the Raspberry Pi 2 B 32 bit or a 64 bit OS?
The R-PI can't handle improper shutdowns?
Why is Internet connection slower on RPi2 than on Win PC?
Debian Jessie or Raspbian Wheezy for Raspberry Pi 2
Pi randomly dies after few days, stops responding and blinking green LED continuosly
What are pin headers and what are they used for
Alternative to java for an embedded system
How to disable Wi-Fi Dongle sleep mode
No sound with Rpi 2
How can I connect an internal 3.5'' SATA HDD to Raspberry Pi
How to find distance and direction of IR signal?
Failed to start package Window10 IoT
3.5inch RPi LCD display - detach from RPi2
OpenHAB to I2C instead of Internet/Ethernet
Emulating Raspberry Pi 2 (ARMv7) on OS X
Connect Raspberry Pi to NRF24L01+
How to troubleshoot power issue on RPI2?
Connecting Multiple Raspberry PIs via LAN and Known which Port it is connect to
How do I make hostapd run at startup?
How to remove and add features from OSMC and Openelec on raspberry pi?
Combining two Rasberry Pi's together for single application
How often can I switch the micro SD card?
Run Windows 10 IoT app at startup?
How can I configure PI to connect through WiFi dongle to a network while still using direct cable connection?
Pi is connected to laptop via ethernet cable, but ifconfig is showing only l0 and eth0 , not wlan0?
Reed switch wiring
Which PSU should I use? 5.35v 2A or 5.1v 2.1A
Is it possible for a bluetooth dongle to receive audio input from two different devices at once?
qt5 adafruit touch screen on raspberry pi moves pointer too fast
Power supply for Raspberry Pi 2 Model B
How to install fresh Raspbian Jessie on Raspberry Pi 1B
Tapping into 5v power
My pi 2 doesn't fit into my B+ case
Can connect to PI via eth0 in SSH but not wlan0
How can I get media files to display in a library style?
PHP USB serial port call from Windows to Linux
Trying to use TMP36 via MCP3008 on Windows 10 iot
How to force Rpi to use usb soundcard
Locking a C++ binary to the RPi serial number
How to get remote controlled raspberry pi to play music/video out of its OWN speakers
fatal error: bcm_host.h: No such file or directory compilation terminated
Access my Pi from another network for file transfers
Where to put heat sinks on Raspberry Pi?
Forgot my password
Why won't Linux Applications run when the file is executable?
How many sensors I can connect to one breadboard ? (raspberry pi 2)
how to create new user in Raspberry PI who has equal privileges as default user: pi?
Can Raspberry PI function as SPI slave?
Max gpio input current
Pi not booting, no ACT LED, not the polyfuse
Is it possible to store data in Raspberry Pi?
Why is Component not working for Raspberry Pi 2?
Raspberry Pi - 4 blinks
Version for `uname -r` remains despite successful rpi-update
How to use logical operations with GPIO of raspberry pi
SSH connection and filling out a field in a browser
SSH not working with Raspbian
Power Pi from 7A power supply
Windows 10 IoT Core Simple Serial Sample not working
Can I prepare an Ubuntu SD card for my Pi 2 B on a Windows 10 machine?
Force Raspbian to display everything a little bit smaller
Shutdown Raspberry over ssh
Creating GUI window visible above RPi Cam preview window
Python - GPIO PWM control backlight LCD display
How can I use a usb barcode reader with my raspberry pi
Cannot access raspberry pi by hostname
How can you SSH into your raspberry pi with x11 forwarding enabled on mac?
How can I install Teamspeak 3 on Raspbian?
Raspberry Pi 2 pinout - what are GCLK, SPI_CE0, and SPI_CE1?
Controlling external appliances with external switches?
Development on Raspberry Pi
how can i make my python program run as raspberry pi boots up?
possible to ssh with Ubuntu MATE
Build a patch panel for the GPIO ports on a Pi
Is it normal when a pin goes low it triggers a interrupt on an another one?
pwm fan on pin 18 help!
Where is the clock?
Analog input with MCP3008
Cannot Install Node.js. Error: "GLIBC_2.16"
Help mounting a network drive
How to shrink an image file after allocating full space
Advanced IP scanner unable to detect Raspberry Pi
How to repair login loop bash error
LCD display not working Raspberry Pi
System for 2 Raspberry Pis to wirelessly communicate about 100 meters apart
How to download an XML content to string variable from web address on Windows IoT
How to continiously monitor Wiegand readers using pigpio library?
Wifi dongle - wlan not listed
Power usb short circuited my raspberry pi
2004-LCD with PCF8574-I2C and wiringPi (Python)
Properly wiring a solid-state relay to the GPIO pins?
Raspberry Pi 2 Error accessing GPIO with SUDO for AdafruitDHT and AM2302/DHT22 sensor
How can I replace "Wireless Remote Control Switch" with Raspberry Pi?
calling Python script with GPIO module over apache2 web server
Unable mount SD card and access files on Raspbian partition after one successful mount
Can I use the Ethernet (RJ45) port on the RPi to place telephone calls?
Pairing the Pi over BT 4.0 LE to a MS Universal Foldable Keyboard fails
VPN connects, but no internet access
Connection to raspicam as event trigger
Raspberry Pi B+ dead on arrival
How can I preconfigure wireless?
Pulling Data from Python Script for Webpage on RPi
Is Asus USB-N10 Nano compatible with Raspberry Pi 2?
Database for raspbian accessed with the same raspberry pi
Can I use a Galileo Gen 2 6 pin FTDI 3V3 Serial to USB cable with the raspberry pi?
Hide Complete Boot Message from RPI booting
Raspberry pi frequently disconnecting and reconnecting from wifi network
Reseting Bash Prompt Text(Not the color) on RPi
Can't connect to my RPI access point
No video output for raspberry pi 2 model B with Jasper image
wifi stops working after a few seconds
Replacing damaged ethernet port
Is there a way to get a usb external drive automounted on connect and boot?
Enable monitoring mode for RTL8188CUS via USB on Raspbian
How best to extend the PI with hardware decryption/encryption, TPM/HSM?
Limiting GPIO input voltage
Backlight control for official Raspberry Pi 7 inch touchscreen
Fast reinstall of rPi with desired dependencies
My GPIO is not working correctly
Unable to connect to Apache 2 server on Pi externally
Under powered Raspberry Pi B+
Can rPi control a computer and provide backup?
Automounting USB drive on boot
Windows 10 IoT Core Needs Explaining
Switching Micro SDs
GPIO pins NOT working when using touchscreen
Taskbar flashes grey
How do I get the configuration and Module.symvers for a Raspbian kernel to compile a loadable module for my RPI 2?
Build a web program with raspberry pi,offline
Problems with TPLink wifi dongle on Raspbian (linux kernel 4.1.8+)
SD card questions
What is the difference between Raspbian Wheezy and Raspbian Jessie?
Why is the L2 cache disabled by default on Raspbian Jessie?
PWM Fan causes clicking sound
Static IP internet connection only connecting to router on Raspberry PI
Using Pi to read 1 MHz Analog Ultrasound signals
Getting RFID-RC522 to work with Raspberry Pi 2
Arm ESC RPi.GPIO
Using an L293D chip (to control a motor) with a separate power supply
Python GPIO buttons blocking Lirc
How do I display a message on the screen
Creating FTP for my public web server
Number of maximum inputs i can get on a Raspberry pi
How to make xtightvncviewer fullscreen
GPIO kills Pi when connected
Controlling a stepper motor with javascript
Enable 2 screens on raspberry pi2
How to detect, if something is not working properly?
Raspberry Pi connected to internet but can't SSH or Ping
DS18B20 no longer working
Raspberry Pi 2 Functionality
Disable UART at boot time
What's wrong with this Pi?
I can't expand my root space
raspberry pi 2 model B hdmi to vga converter
How to control a 3V laser from GPIO
Raspberry pi 2 heats and does not boot (Power LED doesn't glow) after over-current dmesg
WebIOPi can't be downloaded from The Pi Store
RPI2 raspban wheezy on can't install autoconf
Global name GPIO is not defined errors on WebIOPi
Raspbian - unable to locate package mysql-server-5.6 after adding repo
How to use raspistill on Ubuntu
Have people tried doing comparisons between Intel Celeron and Pi Model B+?
Error installing OpenVPN - Files missing
How to upgrade VSFTPD on Raspberry Pi to latest version?
How to program a Raspberry Pi 2 (Really basic question)
How do install Chromium on openELEC?
Is it possible (doesn't completely break your system) to use stretch (Raspbian testing) now?
How do I setup RDP server for the Windows 10 OS?
Which OS would run faster in image processing? Is "RISC OS" is well suited for this task?
.profile/bash script only run locally
How do I create a custom OS image to be installed on several Raspberry Pi?
Spotify 'one touch' player for disabled user
USB passthrough with monitoring
Defect Raspberry Pi as source of fire
Can I use airmon-ng via SSH?
Changed to static IP in Raspbian, yet old IP address continues to exist (alongside new)
http://ip doesn't work, while https://ip does. What do?
Should I entrust a home server role to a Raspberry Pi 2?
Differene between Pidora and Fedora ARM?
Strategy for controlling one Pi's outputs from another Pi's inputs via network
Samsung Portable DVD Writer
How do I use the /sys file to control the GPIO pins
Local network between two RPis?
How to troubleshoot a headless Pi that boots into emergency mode
How to connect a regular CPU-Fan to the Raspbrery Pi 2 B
--banner-colour not working on fswebcam
Where do I find the linux headers for an image?
How can I disable autoconfigured networking on Raspbian?
Connected to internet via WIFI but not with Ethernet
Alternative Storage Options
Detect 240v using GPIO
Installing new OS over ssh
Use PuTTY & winSCP to SSH using .local domain
noobs reset password Debian
How to get devices IP address in Windows IoT C#
Raspberry Pi Camera Rev 1.3 is not detected
Ssh connection refused
Best way to make python script and server communicate
How the data transmission of the non-ir-filter-cam works
RBP 2 Power supply and outputs
Ubuntu Mate not using all its storage
Spotify for RPI
Raspberry Pi sensor error with high CPU
Is it safe to drive a current between a GPIO output at 0V (LOW) and the 3.3V supply?
Turn LED on after a particular time for a particular time period
Cannot get Synergy to start with Raspbian
Custom splash screen on Raspbian Jessie?
Official WiFi dongle - No Blue light
GPIO High Low not switching in Python
Cross compiling Java application using different APIs to access device's peripherals
Backup Raspberry Pi automatically, with incremental backups
Raspberry Pi Voltage Input
cannot install python-dev
How to set up a RaspberryPi(B) as a 4 year-old's PC?
Raspberry Pi and serial only working one shot
Connect switch to gpio
GPIO cleanup via terminal
How do I set up networking/WiFi/static IP address?
Raspberry Pi 2 not booting, USB port appears to be dead
Can I use any GPIO pin as an input
Is it possible to connect a raspberry pi to an apple cinema display?
How to install InfluxDB and Grafana?
configure monitor to allow rotation
OpenVPN on startup fails
Pi keeps crashing. Where should I look
Cannot Emulate Raspberry Pi using Qemu: Kernel Panic
locale settings Issues
3.5 mm jack starts to "hiss" after sound is played
Did MySQL server cleanly install?
RPI - Which GPIO pins are 0V at statup?
Raspberry Pi - Rainbow screen
Stream Airplay Video to Raspberry Pi without raspbmc
GPIO - Is there someway to make the GPIO mode permanent?
How do I tint my monitor red for nighttime use?
How to use Bluetooth to send audio on Windows IOT
How to install Raspbian without an SD card reader
Getting a command prompt on OpenELEC
Backup power for pi 2 model b
Easy way to switch on and off of 12V DC current
Raspberry pi 2 with new raspbian can't startx
How to install Real Time Clock (RTC) on Raspbian?
Is there a component out there that can push a button i.e. will extend a rod about 1 inch and then retract it?
Raspberry Pi 2, not booting, PWR & ACT constantly on
Check performance of SD card and USB flash drive
Does a RasPi case exist that utilizes a key and lock for unattended datacenter usage?
XTightvnc font path error
How to display real time on a Pi
How can I use RPi2 only to download Steam games?
RPi 2 SD card becomes write-protected
Raspberry Pi Wifi not scannning
How to send audio to BOTH headphone jack and HDMI simultaneously?
Communicating with RPi at home without port forwarding
Get files from raspberry Pi SD card
Error when attempting to create Python GUI using Tkinter: "no display name and no $DISPLAY environment variable"
Wifi connection problems (different behavior with / without cables)
Connect two devices to the same GPIO pin
How to read/write directly to SD card, using Windows 8?
Raspberry Pi lifespan reliability
When to call script that can capture IP in python
SD card corruption
Unable to connect WiFi to the Pi
Which GPIO pins on previous modela are equivalent to those on the B+ model?
Is it worth it to upgrade to Jessie on a headless Pi2?
WiFi not working on Raspbian Jessie
SSH connection refused windows 7
Undefined reference to raspicam::_private::Private_Impl[...]
Using the Raspberry Pi as Webserver and btsync
using laptop display with raspberry pi using HDMI connector
Unable to SSH to raspberry pi from external connection
Project text-to-speech for a blind parent
Recording video using Motion regardless of motion detection
How to start OpenVPN at boot on Raspbian Jessie
bluetooth connection with Iphone
win32diskimager not enough space
Auto reload new images in feh image viewer
Java is crashing my Pi
Auto-start chromium on raspbian jessie - 11/2015
I Cannot Change the State of the GPIO Pins
Data Exchange Between two Raspberry Pi?
SSID retrieving in raspberry
RPI Forever On?
Can the Pi Zero act as an USB peripheral device?
IDLE not opening from terminal
Schematics/Drawings of the Pi Zero?
Raspberry Pi Zero actual price?
Which RF transceiver to use for a network using Rpi or Arduino?
How do i force the Raspberry pi 2 to use the 3.5mm 4 pole video out
True 9-bit serial port data?
Can the Raspberry Pi Zero be powered by a real usb port?
OpenVPN Site to Site client on raspbian
What can I remove from raspbian to boot faster?
Rotate Display Depending on HDMI or Composite Output
Will downloading items to a network location wear on the SD card?
Pi as HF ham band transmitter and FM repeater
Remote controlling the PI
How to set Raspberry Pi GPIO pins to input or output using clean C?
Is there an addressable LED product that I can wire to a Raspberry Pi where all the LEDs are separate?
Any remote sensors for the Raspberry Pi?
NTFS USB HDD Read-Only - How to enable write permissions
PiFm dBµV/m without an antenna
Dimmer - How synchronize PWM with 230V power supply?
Why can't I connect to my Pi via VNC?
ALSA - piezo buzzer directly on PWM pin?
How do I add analog audio out to the Raspberry Pi Zero?
Can raspberry pi 2 take more than one input
Enable num-lock at boot Raspberry Pi
What's the smallest wifi connector for the Raspberry Pi Zero?
Powered USB hub for Pi Zero
Pi Zero Video out header
Voltage conversion & input circuit for Raspberry Pi
R-PI 2 data bus capaciy
RPi pin being tripped by static electricity?
How to connect Raspberry Pi Zero to PC
Serial Communication C/C++
How to prevent /etc/resolv.conf from being overwritten?
Raspberry Pi Operating system transfer
Rainbow square and influences of disable_splash=1 (or: how to get rid of the colored square)
how to inspect Rasperry Pi 1A from Laptop (Ubuntu Linux 14.04)
Binary garbage on the UART when powering the RPi
Recording video in Python and storing it in any format until I press 'q' or 'Esc'
RPi.GPIO not working
Overclocking capabilities of pizero
GPIO Broken - cannot power - depower pins
Raspberry Pi; blank desktop
No Internet Connection
How do I set my Raspberry Pi to automatically update/upgrade?
Convert python to rpi-gpio nodejs
How to build My own OS for the raspberry or configure an existing one
Driving a Sainsmart Relay using Raspberry Pi
Are the SPI pins 5V tolerant?
Raspberry PI not booting and no lights
How to use 2.4" TFT LCD Shield with Raspberry Pi?
CEC-Client does not find devices but RPi controls my TV
Realtek USB wifi module - RTL8188EUS is not working and also it is disconnecting LAN connection as well on Raspbian Jessie
Minecraft-pi on headless pi using ssh -X
Raspberry Pi wifi won't work
No audio output using raspberry pi and pygame.midi
Mac El Capitan X11 Forwarding not working
USB Cables... Why are some of them bad for Raspberry Pi?
Program won't run after tightvncserver auto start at boot. No probs if started manually
Can I use a cable such as the ones linked to connect my Pi Zero to the network?
Underclocking PiZero for power saving worth it?
Proper way to connect 5v device out to 3.3v RPi input?
How do I start two different Python scripts with rc.local?
My Pi freezes during install
Use Rasberry Pi's Usb Ports for Broken Computer
What operating systems allow ssh connection on first boot (with no configuration)?
How to detect what kind of HAT or GPIO board is plugged in - if any?
Access shell while music playing
How can I stop auto login console and getty in raspbian jessie?
Energy profiling tools for linux
strange characters (@) in .dtb files in /boot/overlays/
how to use overlays for ads784 joy-it 3.2 " tft screen
16gb image to a 15.9gb card using windows only
Can i install a whole debian8 for arm in raspberry pi?
Connecting smartphone to raspberry pi via usb
How to resolve a short circuit?
On-board LED connection to GPIO
Updating BlueZ 5.23 => 5.36
Powering the Pi from battery (power consumption)
How to determine the problem in HDD reconnection?
How to control the 5v output from raspberry pi to open and close a relay
Raspberry Pi Web Server Users?
TLS handshake failure for VPN
Raspberry pi 2 not being able to connect to WI-FI
Jumper function on relay modules
Compatible microSD Card SanDisk
/etc/init/d/tightvncserver script fails at boot
What is the byte order for the WiringPi 16 bit I2C reads and writes?
Holding the PI in reset?
Can't stop script from running at start up
Cannot make Pi visible on network
How do you connect 81 LEDs to as few pins as possible?
Raspbian Jessie SSH cant connect
Raspberry Pi Email Notifier Python Script not working
What GPS dongle / device works with Windows 10 IoT and Raspberry Pi 2?
Raspberry Pi2 not booting when linux being ported using buildroot
How does init get to know about power events?
Raspberry Pi Cluster Computer
GPIO Display an Buttons dont work
Build custom Raspbian Jessie distribution image from source
What is the difference between Model B+ v1.2 and Model 2B v1.1
What can damage my Pi or make it unusable?
Possible to power a Raspberry Pi Zero or B+ plugged in via an Ethernet port?
Can the OS run from a write-protected SD card?
Online Storage that I can mount on my mac
How to make startx open new X Session in tty7?
Raspberry pi power
Sharing internet with Rpi
Configuring uv4L for webRTC using USB camera on RPI2 raspbian
Powering Raspberry Pi Zero and a HUB with one charger (3 in 1 cable)
Installing MongoDB On Raspberry Pi 2
URL to grab stillshot from camera?
Can you put Windows 10 IoT Core on Raspberry Pi Zero?
Display goes blank periodically on LG TV
How to connect a headless Raspberry Pi at coffee shops?
How can I use multiple LCD with connected via I2C on same Raspberry project?
dhcpcd vs /etc/network/interfaces
Raspberry Pi Zero - Is it USB OTG, or just a female micro USB connector?
Can't access command line of Raspbian/Kodi on boot by pressing ESC
How much current should I supply my 2 model B?
How compile a loadable kernel module without recompiling kernel
Raspberry Pi 2 Model B and External 2.5 USB3.0 HDD
GPIO.cleanup() doesn't clear my screen
Make sntp run on boot in Jessie
Unable to set default input and output audio device on Raspberry jessie
Differences between Raspbian Jessie and Raspbian Jessie Lite
How do I install/run kodi on raspbian?
Why there is a collabora.list on my raspbian wheezy source repo?
Raspberry Pi 2 works with 1A supply but not 2.5A or 3A supply
Raspbian boot process and the partition table
Touchscreen w/ HDMI output only when a display is attached?
Sensor Question
About Raspberry Pi mote in Contiki OS
No ad-hoc compatible Wifi dongle
Installing GitLab messed things up, how to get it out?
SCP File Transfer Between Pi and Windows
Raspberry Pi B+ can't install node-red
Raspberry pi with drone for live streaming
startx command not working
Can I connect my Windows 8.1 laptop to my Pi via WIFI?
Unable to switch to normal user in command line
Can I edit cmdline.txt on a Mac?
# symbol not on my keyboard
Make Raspberry Pi 2 into a video capture card
Pin applications to task-bar on Raspberry Pi 2
Log correct boot time
Access GPIO pins without root. No access to /dev/mem. Try running as root!
White TFT LCD touchscreen isn't functioning on Raspbian or Ubuntu on a Raspberry Pi 2
How can I drive a RGB led strip on SPI with chip select and another SPI item?
gpio not working
Ping not working as excepted
Problems with Pi Model 2B Boot
Can I get the full version of Windows 10 on Raspberry Pi
Cannot get my PiTFT screen working
How do I get RCA video out of OpenELEC?
What does ^[[A mean in the terminal?
Install of Raspbian Jessie does not work
Using jumper cables to turn on LEDs
What can I use to power my Raspberry Pi Zero with rechargeable battery?
convert a pic to bit stream and write it to gpio
Pi 2B not producing picture on screen
Pinout difference
Share internet between 2 RPis
I'm having trouble setting up my config.txt file to work with hdmi display
The transfer of files using the afp:// protocol from OSX10.11 to a RPi using its root password
Java and DS18B20
Raspberry Pi B won't recognise DS18B20 sensor
How to find the config.txt on noobs
Make permanent change in the routing table
SSH to Pi through putty Connection Refused (Raspbian Wheezy)
Wiping an SD card using my Raspberry Pi
Visibility in network after internet sharing
Use Arduino code on raspberry pi?
Use existing OS or create a new one?
Different audio output on hdmi and jack
How can I add an On-Off switch to my Raspberry Pi 2
Connecting Raspberry PI 2 to WIFI
Raspberry PI 2 can GPIO Pins 29-40 be used GPIO_GEN input output configurable in Python?
Error in reading data with pymodbus
Cannot get USB audio (Generalplus Technology Inc) to work
Mysterious RPi wifi problem -- No wireless interfaces found
How do I remove OSMC from a Raspberry Pi 2?
reverse engineering: Transcend digital photo frame display to Raspberry Pi
Autolaunch Programs on LXDE startup
Expanding size of the root / using external HDD
Can I use a DC-DC step up module to power a Raspberry Pi from 2AA batteries?
Connecting with VNC causes white flickering menu bar
How to enable auto-login?
OpenVPN setup issues
What is the function and purpose of the GPIO connector on the official display?
OpenCV display image: window system doesn't support opengl
How to read values from an clamp-on ammeter with an raspberry pi?
Gertboard or similar for Raspberry Pi 2?
Reverse SSH to remote host
Log output of background or boot script
Java native code
Disable LED for Edimax EW-7811
Please help - How do you get Raspberry Pi out of the rebooting screen and onto the desktop?
RF or WiFi for remote lighting?
Is there a Pi Simulator application for Debian?
Access Windows 10 IoT device from internet
PHP-version on Raspberry Pi different in phpinfo()
raspistill annotation timestamp not updating
Basic question on powering multiple Pi's
Raspberry seems to ignore static ip setting
Raspberry pi 2 wont show anything on screen, help?
setting up a kiosk with chromium
Restart mplayer stream process on loss of internet connection
How can I use youtube in pi?
Can I backup my SD card with Disk Utility on OSX?
Upgrade from one Jessie to another
Pi freezes while "Updating SDK" with ACT light on steady
Audio goes in and out on Retropie
How to reinitialize HDMI without rebooting the RPi
How often to reboot raspberry and is it even necessary
How to serially communicate between raspberryPi and arduino using usb to serial converter?
Cannot connect to raspbian jessie lite but to raspbian jessie
Raspberry Pi 2 support PXE booting or network booting without an SD card
auth.log sshd entries
How to install cups-driver-gutenprint?
Jessie: cfg80211: Calling CRDA to update world regulatory domain
Jessie: Default route fail when disconnecting eth0
Is it necessary to resize the file systems on Ubuntu MATE?
How can I install Lantern on Raspbian?
Can I use my old smartphone like raspberry pi by installing raspberry pi OS to it
Raspberry Pi Touch LCD Screen problem when GPIO connected
Tkinter on linux start up
USB Rx from GPIO
Pi DNS Resolution
500 Internal Server error when logging in to Raspberry Pi Store
How can I power the pi safely?
RPi 2: spi_bcm2708 or spi_bcm2709?
How do I configure my sound for Jasper on Raspbian Jessie?
Is 8gb enough to support Ubuntu MATE without storage issues?
Colored console over serial connection?
Kernel panic-not syncing: VFS: unable to mount root fs on unknown- block(179,6) running Raspbian on top of NOOBS
Raspberry Pi Noobs Static address config
SSH session keeps exiting my terminal
Connecting RPi to an iPhone through Bluetooth using an iOS app
How to run a mono exe file?
Nginx "Out Of memory: Kill process"
Java headless or headful?
Do You HAVE To Use SDFormatter Before Installing NOOBS?
Connecting raspberry pi 2 to pc without internet
Re-configure Raspberry Pi as if it was new
Raspberry Pi 2 Media Server
How do I stop HDMI powering my Pi?
Where to find libraries for using existing popular sensors?
Resizing a SD card with NOOBS installed
RPi2 not booting when the HDMI is pluged in
Air pressure switch for balloon
VNC problem on Mac and Pi 2. No .xsession file
How learn about TightVNC on a Pi
Can I connect any ADC to RPi?
Creating Disk Image of SD Card
How do I use the command line to check which WiFi network I am connected to?
I changed my Raspberry Pi default keyboard settings. How can I reset this change?
How do I configure wpa_supplicant with default iPhone SSID?
Set up RPi2 as a local website for I/O control
Raspberry Pi is not found on local network
How to know the input voltage on Raspbian?
Sparkfun ADXL345 wiring issues
Raspberry pi class 4 vs raspbery pi 2 class 10
No Internet Media Player
GPIO library for C
Problems creating desktop shortcut to Tkinter script
How To Switch On/Off A Circuit using GPIO
Raspberry Pi out of disk space
Unable to locate "fim" package
Raspberry Pi Model B 1GB version has both solid lights without SD Card
Getting the latest version of R on the Raspberry Pi
max length of wire w/ 3.3v or other issue
nl80211: Driver does not support authentication/association or connect commands
looking for a compiled version of postgreSQL 9.5 for rpi 2
Project needs multiple PWM
Slot car races time recording
how to run GDM on raspberry pi 2
RPIO Module installation
Raspberry Pi Camera Module slower than Desktop Webcam
Nginx Default Sever Config
Ethernet stuck in cycle of "carrier acquired" and "carrier lost"
I2C using wiringPi or IOCTL in C, more than 2 bytes
NOOBS multiboot - resize partitions
I need help to finish installing the latest version of Chromium
hdmi2vga or raspberry problem
Why can't connect to RaspberryPi on different network using the same static address
Does "Connection Refused" and success of PING command means that RaspberryPi is connected?
Using flask to play videos
How can I switch between a built in display and HDMI?
Reliable browser/OS for use of showing webpage?
Raspberry Pi Not Working
Two Wi-Fi networks. One preferred. Connect when it comes in range
How to access Raspberry Pi when it has a private address while using university Internet
Can I get elementary os freya on my raspberry pi 2 model B?
Raspberry Pi 2 Arduino Mega USB Communication
Allow remote users to shut down Raspbian jessie
Rasberry Pi's usb limitation when using web cams
How to know if you're writing on your SD Card?
2 amp power supply for RPi2. Too much current?
Low Enery Consumption Kernel
Material that can be used as a switch for an LED
How to connect and use ssh without a screen using BUILDROOT
can't find ipaddress of my raspberrypi
What vulnerabilities, if any, are inherit to an open samba share on a home LAN?
Why doesn't Pi browse the internet? I get the "Oops!" comment
Two servos connected causes shaking
Why can't I SSH to Raspbian anymore?
Trying to port an Eclipse RCP application to Raspberry Pi
Is it possible to access Raspberry pi 2 ubuntu 14.04 without usb-keyboard?
Installing Chrome on Raspbian
How do you get C# onto your raspberry pi?
How to connect a graphic card to Raspberry pi?
wireless Controlling of a servo motor using Raspberry
Bcm 43143 Hostapd Driver Problem
Crashes under load – how to investigate?
Why does apt-get upgrade cause blank screen after reboot on Raspbian?
Change permition of a mounted external harddrive for all users?
Windows 10 IoT Dual Boot
Alternative way of providing uninterrupted powersupply
C# implementation of MS5637 sensor with I2C on IoT
WiFi with Ethernet?
Mac Clone SD with dd failing during boot
Will expanding the file system affect how wear leveling is implemented on the SD card?
Visual Studio Code & .Net Core ARM support
Why is very little capacity available on my 8GB SD card?
Camera Module take pictures every 30 sec to SD card
Problems with SD card
How to install seafile client
Retro Pi expand filesystem keeps reverting
While statement checking for button press while accepting raw input
What are the differences between the models A and A+?
Raspberry Pi 2 - Help with Wifi Access Point
Can I power a DC motor with the Pi's 5 volt pin?
Raspi won't start apache2 after I power cycled
Initial setup without a monitor or keyboard
What components are required for connecting servo motor to PI?
Not able to Install openCV 2.4.9 on raspberry pi 2 model B
How to abort or cancel LSB job on boot?
Should running VNC on Jessie Lite "just work"?
Communication between radio transmitter (device A) and receiver (raspberry)
Chat on raspberry pi using ssh
Touchscreen display turns off whenever audio plays (RPI2, DAC+, PITFT)
Direct network access (ethernet) to RaspPi2 from PC Linux
Can I run Ubuntu Server on an Raspberry Pi 2 Model B?
sudo apt-get not working
Error on Boot. 'No working init found.'
RaspberryPI with Windows 10 IoT Core can use Silverlight?
Raspbian jessie - cronjob doesn`t work
Turn on TV without HDMI-CEC
Module loads with modprobe but doesn't in boot
Initial startup blank screen
Wooden clock with LED: which components?
Where to set TCP server and where to set TCP client?
Installing VNC on a new headless Pi 2
Apache server "403 forbidden, you don't have permission."
Is the GPIO configuration changed for Raspberry Pi Zero
Can I power a Pi with a ribbon cable AWG 28?
Error : DEP0700 : Registration of the app failed
how to make radio wave with pi2
Wifi randomly not working and working (carrier lost)
Can I use a Y-cable or Dual-Power cable to get additional power for a single USB powered hard drive?
Performance with an encrypted disk
Wireless networking of multiple Pis without internet
cec-client on Wheezy (retropie) not finding TV
Is it possible to install .exe file in Raspberry Pi running Windows 10 IoT Core?
Static vs Dynamic IP for Pi
Raspberry Pi hardware ID
Driving a 4 digit 7 segment common cathode from GPIO
Windows 10 IoT Wrong Time
Keyboard and mouse stops working after connecting usb hard drive
Running Raspbian Jessie from SD in Mac OS
Use ssh as substitute of serial
Red LED after `sudo halt`, may I unplug?
Getting kernel headers for raspberry pi 2
Raspberry Pi with camera module as webcam?
RetroPie pre config image
Are there any battery packs than can act as a UPS?
Can I use the USB Hub to power the Raspberry Pi Zero?
Accessing files on Pi over HTTPS
File transfer 8 GB to 32GB SD card
Laptop display connection
CentOS Development Tools "No package kernel-devel available."
Installing CentOS 7 on a Raspberry Pi
Use Pi as internet gateway
Disk Migration between same model rPI
Pi can't find Wifi Dongle Upon Turning On/ Rebooting/Ifup
Serial write 1,000,000 baud slow
Can't compile OpenCV 3.1 on Raspberry PI: Missing videoio.h, videodev.h,
Putty error while connecting Raspberry Pi to my computer
PiCamera and Flask - Start and Stop Preview/Record
Tips for keeping a motor in sync?
What's the difference between aplay -l and aplay -L?
Raspberry Pi- Arduino Serially driven servo problem
Win10 IoT +Raspberry PI 2 official touch display support
real time clock puzzle with new rasbian jessie
Port forwarding on a tethered RPi
Raspberry Pi Zero not booting?
Raspberry Pi Time is off by 45 min
Raspbian ignores /etc/network/interfaces
Connect a processor board to Raspberry pi
What is the best supported microSD card's with it class for Raspberry Pi2 Model B?
Wifi stick for Raspberry Pi 2
Exiting OSMC to RBPi Terminal
Power consumption of Pi Zero in Headless mode
GPIO=webiopi.GPIO, attribute error : module object has no attribute 'GPIO'
Web controlled OMXPlayer
Driving 32x32 LED grid via GPIO preventing other processes from running
Accessing GPIO from lighttpd server not working
Sending IP address by email on boot by executing Python script
Does it matter which pins are used when powering the Pi from the header?
How to indicate read / write disk operiation via LEDs connected to GPIO
Can I power a 3V water pump using the 3V3 pin?
Want to put a variable into os.system command on Python 3, but it doesn't work
OS and script advice
EDIITCan RPi2 be used as an IP cam viewer?
Sonic Pi, defining my own classes
how to create an id system for raspberry pis that is not hardware dependent?
Share a folder between three accounts created on the Raspberry Pi
Raspberry Pi - TSL2561 Lightsensor
Correct wiring for 433MHz transmitter/receivers?
Accidentally Removed SD Card
Autorun browser kiosk with Jessie Lite
Pulse Audio has no output but Alsa does?
RPi Streaming Audio Server
RPi2 - No HDMI signal only on monitor
PHP Script to Change DHCP Configuration
RPi OCR or how to read a number from the camera
Is there a max current that can be supplied when powering the Pi from the pins?
Raspberry pi autostart of LXDE does not work
Static IP (wlan0) initially not reachable from other intranet machines
How to connect with SSH to RPi through hostapd hotspot?
Can pulling the power cause any problem *except* with the SD card contents?
Smartcard Reader not detected on boot
Can different raspberry pi models share SD cards?
Launch terminal ro run hangoutbot on raspberry start
Raspberry pi computer monitor
How can I disable GPIO warnings?
Can a raspberry pi hw/sw combination retract and extend a linear actuator?
Raspi Config on Ubuntu Server 14.04
Raspbian Jessie Lite Boot Delay - Long Wait for DHCPCD
500 OOPS: could not bind listening IPv4 socket (vsftpd in raspbian)
Transfer time, weather and notification data from Android device (rooted)
Reset Wi-Fi dongle
GPIO TXD0 vs RXD0 vs SDA1 vs SCL1
Wiring diagram software
Can the Raspberry Pi Zero run Java 8? And on which OS image?
Apache2 apparently not working
Camera on Raspberry Pi Zero
Different voltages across circuit when 3v3 to ground than when 3v3 to GPIO in
Removing HATs from the Pi
Can't connect to Pi through SSH (Putty)?
I want to switch between versions 2 & 3 of Python. Both are installed
Controlling a common RC car
GPIO.wait_for_edge on 2 channels at once?
Difference between Servo hat and driver?
Do I have to buy a powered USB hub?
How to stream low-latency video from the RPi to a web browser in realtime
Typed in startx and now I can't log in
Which sensor should I use to detect a table tennis ball bounce in a table?
Apache Server - Hosting 2 domains
R-pi2 Raspbian (Debian Jessie) won't connect to the wifi hotspot it finds
Show login prompt on boot
Using two Raspberry Pi to display an output on the monitor wirelessly
Install git Raspbian Jessie lite
Pi does not pick up my Wi-Fi but sees neighbours Wi-Fi
How to safely switch off the Raspberry Pi?
Raspberry pi 2 blinking ACT LED at boot
Running a Java Swing GUI on start up
Automatic shutdown of Pi Zero on low battery
Is this the correct usage of rsync to create a Raspberry Pi backup?
Clone Raspberry Pi SDCard to file on Mac OS X?
How to make a Raspberry Pi SD partition accessible from windows and raspbian?
Issue keeping attached HDD online
Cannot access internet wlan0 WiFi Adapter
How to install node.js with GPIO
Making input device for Raspberry Pi
Raspberry Pi A+ is saying WiFi is connected when it isn't
Lighting 5050 led and learning to use spi
Wifi Hotspot problems with wifi driver
Cannot deploy to Raspberry Pi from Visual Studio
DS18B20 w1-gpio Device Tree gpiopin NOT = 4
Kiosk mode, but URL from a file
Need a way to pull MAC Addresses from my Router for a "Who's Home" project
samba server - share root
how to use two rfid rc522 nfc tag reader with a raspberry pi?
Raspicam images are way too dark when raspistill is not used
Is UHS-I U1 or U3 a useful feature for a microSD on Raspberry Pi 2 B?
Raspberry Pi : listen online radio streaming
Streaming iTunes Library from Raspberry Pi to AppleTV
Has the Raspberry Pi already been used to build a proprietary product?
Should I expect major differences between Raspbian and Ubuntu?
Ethernet not working because of power supply wire length
Raspberry Pi 2 - power circuit
Error The action "Run Shell Script" (Image to Card)" encountered an error
Raspberry Pi showing 0 Available space
SD card is titled “RECOVERY” and only has 1GB after using RPi
Ultrasonic sensor code disambiguisation
Hostapd No such device
How likely is SD card corruption?
What are the differences between the Model 2B and 3B?
OpenCV Installing (make) errors on /modules/objdetect/
How do you compile a c++ programs to use Hard Float in Raspberry using Debian OS?
Connecting relays to a Raspberry Pi via radio
omxplayer doesn't play audio when streaming
Why my HDMI->DVI converter works only when powered from PC?
MMA845X accelerometer mapped at 1C
Unable to connect to Pi over SSH (no keyboard, no monitor)
'Zoom out' on 3.5 inch LED screen
Raspberry Pi 21, 22, and 80 Ports Acting Up
Permission denied opening UDP socket with static IP
powering RPi from touch screen usb out
Virtualization on Pi 3 Raspbian
Windows 10 IoT / Raspberry Pi 3
Raspberry Pi 3 vs Pi 2 power consumption and heat dissipation
Raspberry Pi Model B 3 Overclocking?
Does Pi3 Wi-Fi support 5 GHz and does it need an extra antenna?
Add an external antenna to a Pi 3
Raspberry Pi 3 audio input?
Raspberry Pi 3 Web Browsing
Raspberry Pi USB Bus Speed
Triggering two USB cameras connected with single Pi at the same time
RT patch is freezing
Bluez 5.37 install problem
Connecting to universities WPA2-Enterprise Wifi Network
Install libapache-mod-fastcgi on RPi 2
SSH into a running instance of an application
How can I connect a Raspberry PI Zero to a Windows Computer via USB?
Powering multiple PI's with one power source
Windows PC tether for internet connection over USB to micro USB without any adapters?
How to determine why Raspberry Pi 2 restarted
Does the BCM43438 WiFi chip in Raspberry Pi 3 support "monitor" mode
Ethernet port on Zero and A+?
Unable to Compile and Run Object Files on an RPi
Does the BCM43438 WiFi chip in Raspberry Pi 3 support power management setting?
How to enable Wi-Fi channel 12 on Raspberry Pi 3?
Can not make directory on my USB disk connected Raspberry Pi 2?
Raspberry Pi 3 usable with fully free software?
How to free the UART pins of Raspberry pi B+ from acting as a kernel console?
Read value from IR break beam
Controlling a water valve
Raspberry 3 - Boot From USB - but how?
Eth0 doesn't keep it's settings after reboot
Maximum current on each GPIO pin for Raspberry Pi 3 Model B
Why is python3 stopping without an error message durring a spidev xfer2 call?
Cores on the Raspberry
Jessie in Kiosk mode on the Pi Zero, the proper way
Unable to reconfigure locale in raspberry pi
Raspberry Pi 3 - eth0 wrongfully named 'enx...'
HifiBerry DAC+ or Digi+?
Raspberry Pi 3 - internal Wifi wont connect to network
Screen is not working please help ;-;
How to download Iceweasel
Can I Install Debian 64 bit on RPi 3
Raspberry Pi 3 micro SD card speed
Linux headers generic package not found
Pi 1 B, Jessie Lite, SPI doesn`t work
Sonar & Rotary Encoder processes running at the same time, in the background (multithreading? subprocesses? asynchronous?)
Sending files (Documents, videos etc.) Raspi to Raspi
What is the maximum number of modules I can connect to Raspberry Pi 2
How to get Raspberry Pi irc server to work?
Local apt mirror just for a single release
web.skype.com for Raspberry Pi Zero
Scraping game info in RetroPie
Disable WiFi (wlan0) on Pi 3
SSH hung after entering password just when using wlan and disconect eth0
Using Pi 2 as feedthrough of mouse/keyboard to computer
How do I change runlevel on model 3
How to remotely access a database on the Raspberry Pi?
Do I need to use a heat sink?
Connect via SSH to the main display active terminal
Car Parking Management using Raspberry Pi
How to Copy files Off a Raspberry Pi
Apache web-server interface to schedule GPIO tasks
Cannot perform echo command to load driver for rtc module
How do I make a device tree overlay for just a single GPIO?
Cannot SSH to my Raspberry Pi over Wi-Fi
startx: command not found
Can This UPS(UNINTERRUPTIBLE POWER SUPPLY) Run a Raspberry Pi for 24hours?
why has ssh stopped working on my raspberry pi?
Raspberry Pi VNC no action from keyboard or mouse
Automatically running a python script after boot
Can Raspberry Pi B+ run Kodi efficiently?
Raspberry Pi 3 Bluetooth
USB driver for HP C4280
Raspbian moving to 64-bit mode
I2C not working on RPi 2 B
Install GPS Receiver - GP-735
How to locate files for GPSD in Raspbian?
Raspberry Pi3 Bluetooth
Is it possible to use Raspberry Pi as keyboard/mouse/joystick to control a Windows PC?
Raspberry Pi Sense HAT on Rpi 3?
No video output on Raspberry Pi Zero, LED flashing
'xeyes' : how to start 'undecorated' : and at boot?
Wi-Fi on RPi3 not working
Control PWR and ACT LEDs on Raspberry Pi 2 B from Python
how to install android debug bridge (ADB) on raspberry pi?
Jessie: RPi 2 - USB audio input does not work (output works)
Switch to newer kernel installed via .dpkg
I am looking to control an inverter with Raspberry PI
On the Raspberry Pi 2 Model B, Where do I plug the Energenie module?
NGINX and uWSGI work but don't begin at startup
Using GPIO pins 14 and 15 as general purpose
Raspberry pi 3 - why the FAT partition?
How do you stream to a bluetooth speaker?
Can Raspberry Pi 3 do 4K Video?
Wireless issues headlessly setting up Pi Zero
sudo apt-get update Not working
Can the Raspberry Pi 3 be used to create an iBeacon?
Can a Raspberry Pi handle 2 external HDDs and a keyboard/mouse?
Dual booting a Linux and Windows OS
How to make my raspberry pi download my files at specific time?
Youtube TV - HTML 5
Verified 4G USB dongles
Ethernet set up for VNC
How can I control the red LED again
Run something after login
Connection guide for GT-511C3 Fingerprint Scanner and Raspberry Pi 2 Model B
RPi 2 and 3.95 TFT ili9488
Host Unreachable until I send some pings
WiFi country code resetting
How should I connect a pH electrode to my Raspberry Pi 2?
USB ports stop working after a week, needs restart
Could not write pid to lock file
Installing Google Chrome
WNDA3100 Drivers
Raspbian migration from Raspberry Pi 2 to Raspberry Pi 3
Pi Crashes After Reboot
startx through SSH gives 'not autorized error' although 'allowed_users=console' is set
Raspberry Pi Zero and USB camera Issue
switching between multiple keyboard layouts
Reading 'Weird' Serial Communication GPIO
SPI: Raspberry PI master and Arduino slave
Default gateway gone after restart
Forwarding audio signal through GPIO
Preparing MicroSD card for Raspberry Pi 2
Error when installing OpenCV on RaspberryPi 3
It is possible to run Raspberry Pi 3 with a 64-bit kernel and 32-bit user space?
java code help for temperature sensor(DHT11)
Create network if one doesn't exist
How to get Chromium on raspberry 3
Raspberry Pi randomly crashes due to python script
opencv raspicam configuration C++ Example
Polling GPIO pin from C, always getting immediate response
How to connect a Raspberry PI 3 to USB TTY cable
Current concerns regarding Raspberry Pi
Is the Raspberry Pi 2 Model B or B+ case compatible with the Raspberry Pi 3?
Peripherals not working after install of Raspbian
Can't send data from the Raspberry Pi via rs485 and serial port
Cron not call sh script
Ultimate GPS hat gets a lock, but no data shows on ttyAMA0
KODI and analog audio
Having an issue with Bluetooth Manager/Pairing on the Pi
Vagrant on Raspberry Pi
Strange rebooting on RPi 3
Playing various video formats in Raspbian on an RPi 3 B
SSH to Raspberry Pi Remotely
Pi 2 Raspian @ on keyboard not working
No space on 8gb usb stick shows 100% du shows 3.5mb
FreeBSD and Raspberry Pi 3
Long distance use of an RPi 3 B
Raspberry Pi Connect to PC via Ethernet
Raspberry pi camera module libavformat
GPIO status after python code is closed
What areas of the Raspberry Pi are useful to analyze with an oscilloscope?
Making Raspberry Pi 3 a wifi hotspot
Can I use a relay board safely without an external power source?
Dual boot for the rpi
Looking for a simple RaspberryPi keyboard with USB hub to connect mouse to
How to build a directional antenna for a Raspberry Pi
Raspbian Jessie Static IP Config
Move a raspberry disk image from sd card to .img file with only linux and boot partitions. Not the empty space!
How to get RISCOS running on Raspberry Pi 3?
Can I control a DC 3-6v Gear Motor without any driver?
Running a Script 5 Mins After Bootup
Pi 3 WiFi with airmon-ng
Pi 3 does not boot
False positive press of a button
Raspberry Pi 3 first boot issues
Add your own bash commands?
How to run an installed program that is not in the main menu?
How does the Arduberry work?
Is there a way to use Raspberry Pi for a pinball machine?
Where has all my free space gone?
Why do I have so many RAM disks?
How can I install the bootloader manually?
wiringPi cleanup command
Shell_exec is not working!
USB Hub to power 8 Pis
How do I make “startx iceweasel” launch full-screen?
Pi power from a PC?
How to transmit a binary bit stream from a GPIO pin?
Pi hangs when booting
How to find out my Raspberry Pi IPv6 address in local area network?
RasPi sees keyboard but does not accept input
how to save IP address of raspberry pi to a text file
Issue setting up Wi-Fi on Raspberry Pi 2 (Model B)
Create WiFi Access Point with Hostapd
WEP with Raspberry Pi 2 (Model B)?
Cannot ssh to or from Raspberry PI 3
config.txt : Hostname
9 bit serial communication and parity error detection
How to install Tor on Raspbian such that I get an icon?
How much current can I draw from each model's HDMI socket?
Can the Pi 3's internal Wi-Fi chip act as an Access Point?
Garbage on Raspberry Pi console
Linux headers in Raspbian Jessie
Why doesn't the Picamera suffer from a CPU interrupt made by linux?
Video transmisson using NRF24L01+?
Sharing Laptop WLAN through Ethernet with a Raspberry Pi
"chmod u+w config.txt" results in "Operation not permitted."
Raspbian wpa_supplicant problem
Raspberry Pi HDMI not Working
How can I run my windows application on Raspberry Pi2.?
Using GPIO to emulate another device
Using /etc/rc.local to execute an .exe
Space of filesystem on SD card used for a Raspberry Pi
Raspberry Pi 3 onboard Wifi only slow bitrates
Why do the USB ports and Ethernet port share the same controller?
How to disable DMA when using UART on the Raspberry Pi 2
Install Chromium on Ubuntu MATE (Raspberry Pi)
Set up C-media USB soundcard for microphone input on Raspberry Pi 2 with Raspbian Jessie
sense hat sample "snake" returns "event device not found" error
Use raspberry pi 3 on-board wifi module with Windows 10 IoT
Error: Couldn't resolve host
1000 GPIO Pins Microcontroller
Can Raspberry Pi 2 connect to a printer directly via ethernet?
Why my RPI in showing black screen and two icons?
Raspberry Pints will not unzip or transfer from computer
How to read a long int via i2c?
GPIO Output Backwards
Kali Linux Wifi Monitor Mode
ITEAD PN532 on Pi 3 with libnfc
Raspbian Auto Login
Is there any limit for micro SD card size in PI3?
Install Newer Node Version on Pi 3
What happens if I put 3.9V into the GPIO Pin?
Samba installation nightmare
Set multiple static ip in dhcpcd.conf - Raspbian 8 (jessie)
NFS transfer speed Raspberry Pi 2 vs 3
Unable to install SimpleCV on Raspberry Pi 3
Start python script at startup using SYSTEMD in RPI jessie
RPi GPIO initial working but output not
Why won't my Raspberry Pi display?
Can I plug GPIO pins directly to a breadboard?
How to set up KODI (OpenELEC) for any remote to control the media player
Microphone via SPI
Slow Boot: Ethernet Wait
Connect to Raspberry PI 3 over Wi-Fi direct
Raspberry Pi 3: wrong tx-power in iwconfig
Connect raspberry pi to 20 arduinos
Can the code running on Rpi1 run on Rpi2?
Cannot connect to raspberry pi using ethernet cable and putty
What can Raspberry Pi do that my Linux desktop can't
How do I access the serial ports on the RPi in LXterminal?
PN532 in Raspberry Pi 3 is not working
How to uninstall python apps?
125 kHz USB RFID
Cannot SFTP into Retropie
Can't connect via SSH to Raspberry pi 3
NOOBS doesn't work! The worst! (My research!)
Login automatically as root at startup
How do I make serial work on the Raspberry Pi3
need help getting the pi to work as a bluetooth source
How to Get Device Name of my Raspberry Pi2
Disable or catch touch screen events
The purpose of the orange tape on the HDMI connector
Is there an Raspberry Pi OS designed for a small screen
Windows 10 IoT to play videos?
hostapd status active(exited)
PiCam Not Working (At All)
How to install OpenCV3 for Python 3 on Raspberry Pi 3?
Read Supplied Power to Raspberry Pi
Kodi update for complete novice
How do I unzip a file?
Looking for lab test results for the PI's random number generator
Removing Chromium B.S.U
I want to use a common power supply to pi and sensors BME280 and BMA180 (sensor modules). Is it possible?
Problem about installing mysql in my raspberry Pi 2
Pi3 built-in WiFi and buildroot
Raspbian fails to boot after fresh install
i can't connect to page of webiopi
Why does the Sense Hat / Astro Pi show the wrong temperature and humidity?
GStreamer video on DSI screen without X
fidisk is successful but partitions do not change
Crontab on Rpi not running Python script
When a device says it's "Linux-compatible," does that mean it is compatible with Raspbian?
Launching applications from GPIO button presses via a python script
Does the RPi support hardware virtualization?
Is it possible to let my rPi connect to a Wifi with a given SSID without a monitor, keyboard, mouse and LAN?
Multiple questions about power and USB hubs
New Touchscreen Project - GPIO or HDMI
No wireless interfaces
Raspbian graphical login screen stuck! Can't login!
RPi 3 NAS vs WD EX4 vs old Desktop
Hat for shutting down the Pi with a button
PIR Sensor Consistent False Positives
Wire raspberry pi tft display, so as to keep the GPIO pins available for use
Is it possible to use any virtualization technique with the Raspberry Pi 3?
Running Multiple Programs at once
Has anyone managed to run Raspberry Pi 3 with KVM enabled?
How to automatically run a python application on boot to desktop?
How can i set up a point to point connection over wifi, without a router or pre existing network?
Play music from raspberry pi to pc
Detect milisecond on hardware
How do I update Java 8 in Raspbian
Running a CoAP client on Raspberry Pi
Raspberry Pi 2B not powering up
What games can be run on the Raspberry Pi 3 Model B
Controlling an Arduino UNO from Raspberry Pi 3 (Controlling not programming)
How to stop auto program raspberry pi
Blank Gui screen, mouse pointer ONLY!
`Segmentation fault` on every sudo action
How do I know which USB device is my device?
Raspberry Pi 3 getting hot
control external peripherals over serial from Raspberry Pi 3
Composite video out not working
RPi 3 WiFi configuration from Android
20x4 LCD Shield for Pi?
FATAL: Module bcm2708_wdog not found
If Raspberry Pi 3 is connected to PC over serial, then are both devices able to connect to each other simultaneously?
Unable to deploy to Raspberry Pi from Visual Studio with error DEP0001 : Unexpected Error
How do I mount my NAS?
Rpi3 missing spi-bcm2708 module
Remote Control a Raspberry Pi (currently behind a restricted wifi network)
How do I get weight sensor's data to Raspberry Pi (HX711 Load cell)?
How can I triple boot operating systems?
raspberry emulation / nested virtualization - issue when booting with qemu-system-arm
How to find my web server FTP Info
Adjusting the Brightness of the Official Touchscreen Display
Cannot boot raspberry Pi 3 connected to DVI with SDXC class 10 sd card
Berryboot stuck on rainbow screen after update
Download Problems
Sensitivity of GPIO pin
How to send temperature and humidity sensor data from a raspberry pi to a pc wirelessly?
Restore PI from Pi itself
How to automatically mount a drive?
How to access a Samba shared folder from a Pi
Raspberry Pi 2 GPIO and 5V HC-SR04
Is it OK to install Jessie Lite on a Raspberry 1 model B?
Error Install OpenCV 3.1.0
Python code for SW-420 vibration sensor
Increase current output at USB for Raspberry Pi 2
Raspberry Pi not booting and may be damaged
Veracrypt installation a nightmare on Jessie
Headless Torrent Server - Permission Denied
GPIO to hifi amplifier's trigger input (remote power on). Protection? Circuit?
Clustering the 3.3v and 5v rails
cost of Windows 10 on the Pi
Measure RPi3 power consumption without external hardware
How do I install chrome?
max_usb_current possible values
Reduce Ubuntu mate 16.04 img file size
recording a video with picamera
python library to generate pulse frequency of "n" hz
How to use eth0 for local internet access while using wlan0 for ad-hoc network with DHCP?
Graphical interface
GSM/GPRS & GPS Expansion
Issue with apt-get update, Jessie repeats
expand file system kali linux on SD card of 16GB
Raspbian removes dotted directories from /, why?
NOOBS doesn't boot when fan is plugged into GPIO
Whats the difference between NOOBS and Berryboot?
Hosting Webserver with 3G connection
Make the raspberry Pi speak its dynamic IP address
GPIO pins stay on unless being used by a program?
How to operate a cooling fan using GPIO pins, RaspPi2
Sending extra power to PI3 over USB, will it damage the device?
Is it possible to add RAM to Raspberry Pi?
Raspberry Pi 3 - WiFi Stopped Working - How to debug and fix without restarting
How do I detect the type of camera installed?
Connecting Raspberry Pi3 to L9110S H-Bridge
Raspberry pi how to restore original GUI theme
Audio not coming through to external earphones
I2C cannot get data
How to connect Solid State Relay
Connect to Raspberry Pi via SSH
Can I power a RPi3 from its USB ports?
Physical stress testing a Pi
Raspberry Pi SSH and ping not working
how to setup raspberry pi A+?
Choppy sound on MPD + Airplay, working pulseaudio
Why did my code not stop when I closed the terminal window?
sudo apt-get update issue & error
Compile and run Qt5 webengine on rpi2/3
RPi3 is not booting after editing /boot/cmdline.txt -- also unplugged the power after rebooting
Why raspberry has 5V output rail if gpio only works with 3.3V?
Why do the Pi GPIO pins use/give 3.3V and not 5V?
Is it possible to limit the bit rate on the BCM43438 chip via the BRCMFMAC driver?
Power Raspberry Pi 2 From vehicle battery
USB Microphone Raspberry Pi
Unable to get Raspberry Pi IP
Raspberry Pi 3 WiFi Driver
Send uart commands through bluetooth
Raspberry Pi 2 Camera and Alpinelinux
Raspberry Pi 3, can't connect to more than one bluetooth speaker via pulseaudio
Sharing ground with the outlet power source
Launch python file and run continually at start up and reboot
Raspberry Pi Power usage monitoring
Controlling Raspberry pi from website
Unable to integrate Fingerprint sensor in Raspberry Pi2
Installing OSMC as an executable instead of OS
Problems getting df to update on my raspberry pi
What can I use GPIO pins for?
Xinit/matchbox remove border
How do I do ssh "passwordless" login with raspberry pi?
Simultaneous SSH and monitor
Highest safe temperature for overnight operation
Losing access to Raspberry Pi after bridge br0 comes up
Printing with HP Envy 4500
Can the Pi camera module be used with a longer cable?
hcitool scan says No such device
Raspberry pi2 can't boot from sdcard
Raspberry Pi Direct SSH, unable to ping router
Raspberry Pi USB 3 HAT or alternatives
What is the mother-site for the Raspberry Pi?
Problem with MQ2 Smoke Sensor
Simultaneously use a HAT and breakout on a Raspberry Pi 2
Raspbian root default password
Using Kodi to access the internet
HTTP Server stops after some time
A guide or layout for the Eleduino GPIO Extension Board Layout?
Window IoT Core stuck while booting on Raspberry Pi 3
How to automatically connect to Wifi on boot for Pi2?
Restart Pi if not reachable (3G)
Use PHP to get callback from GPIO in
Read audio output from a TV to a Pi
Automatically accepting Bluetooth connections on a Pi 3
Dual touch screens , one for input and a second for output
Multiport power supply for powering multiple Pi's
Running Visual Studio Built C# GUI on Raspbian Jessie
Does the Raspberry Pi 3 support RTOS?
Conveniently devolop Java on my Desktop PC and testrun on Raspberry PI 3
How to PXE Boot a Pi 3?
Powering a Raspberry Pi from a vehicle battery 24/7
Execute Python Script in Chrome
Static IP for eth0 not working
Issues in cross compiling buildroot for Raspberry Pi 2
Unable to use SSH from internet though it works fine over local network
Media center and web server at same time?
New raspberry pi 3 issue with trying to boot of fresh raspbian image
What happens if you try to power a Raspberry Pi 3 with a <=1A charger?
Hooking up a speaker to the GPIO
Copy multiple partitions to one .img file
Problem with Raspberry pi camera
Pi4J ESC brushless motor is not running stable
Can I use 'dd' to clone the Raspbian image from the Pi itself?
Raspberry Pi not booting after I tried powering it through the USB port
UART problems on my Pi3
Reliablity for devices produced with a raspberry Pi
How to compile gutenprint in Raspbian?
Will the Pi Zero version 1.3 require a new case
Can I power Raspberry Pi (newer models) from 3.3v Supply Alone?
3V3 enough for a 5V relay?
SD card not booting
Output of thermal_zone0
GUI program for turning on/off a projector via RS232
Permission denied on everywhere
Is any of the new build of Raspbian, supporting multi core for the Pi2-Pi3?
How to set non standard serial port speed
What is the best way to send Data from Raspi(linux) to Laptop(windows) in realtime?
Has anyone found a tutorial on reading info directly from a Kill-a Watt with the Pi?
Connecting RaspberryPi to the network the static way
Where has the menu item for downloading games and apps gone in the Jessie update of Raspbian?
No methods for running python script on startup are working
LED Toggle Switch with GPIO
Raspberry Pi won't update time
Who controls what software is on raspbian & apt-get?
How to make motion camera secure with a custom login
Raspberry pi setting up static IP - address changes but no internet
Raspberry Pi 3 KeDei 3.5" TFT LCD Version 6.0 driver problem
Can the RPi Camera cable be folded/creased?
Sound output of the Raspberry Pi
Setup Raspberry Pi 3 as bluetooth speaker
Is it possible to write data directly from a mobile to a PC through the mobile's SD card slot?
Cheap USB hub with Pi Zero?
Is pigpio wave generator suitable for Position PID?
Does Raspberry Pi hold any data without a SD card?
Cannot ssh out of RP with fresh Raspbian install
I want to go back to Raspbian Wheezy: is it possible?
What is "action 17"?
Raspbian Wheezy, Raspberry Pi 3 and HC05
Vnc and Port Forwarding - Port and Display Number
Raspberry Pi 2 model B both lights on
update-rc.d: error: insserv rejected the script header
Why is Windows 10 IoT Dashboard unable to find my Raspberry Pi 2?
Software Flow Control in Serial communication
Raspbian Jessie GUI hangs after running matchbox-keyboard
Why does find command stop at the /run/wpa_supplicant directory?
What can I do if I can't use chromium?
Creating a pre-prepared SD card image
GPIO control relay with button
Raspberry breaks SD card -> 31 MB RAW
USB HDD on Raspberry Pi 2 Model B?
Remote debugging with Visual Studio 2015
Generating alternating current from GPIO – is it a misuse?
WLAN access point no internet connection
Raspberry Pi 3 Power supply - chargers for mobile phone
How can I stay updated with ownCloud with apt-get?
Detect water level
How to capture images from 2 webcams parallely using raspberry pi?
Rx/Tx login issue
SenseHat reporting temperature incorrectly - Can it be calibrated?
Application to know how long my batteries will last?
Pi Zero Raspistill error: Camera is not enabled in this build
Login as root not possible
Alternative to mencoder and ffmpeg for timelapse in Raspbian Jessie
Open Source Raspberry Pi software and SD card libraries
Raspberry Pi sensor
Will this MicroSD card work with my Raspberry Pi 3?
Can I use more than one USB Gadgets with the raspberrypi zero?
ownCloud setup: Can't write into config directory!
Pi3b vs hostapd: invalid/unknown driver 'nl80211'
How to type hash ('#') in the boot config
Raspberry Pi 3 Connecting to Bluetooth audio device on Raspbian Jessie
I am very confused about HDMI to VGA converting. Will this cable work?
Benchmark on one machine too extreme
How to configure auto-mounting of USB HDD
Is it possible to control DC motors without an Integrated Circuit chip?
Set permission for /dev/ttyAMA0 on boot
Is it possible to send notification if Pi gets unplugged
How can I measure current with RPi at high voltage/high current (100-120V / 0-30A)
What's causing these crashes after cross-compiling?
How to enable SPI on Raspberry Pi 3
Auto login in Jessie. How?
Booting from a USB
Is it possible to access pi on my laptop through wifi?
Raspbian Jessie, Route all traffic through VPN, Close if VPN goes down
I can not log in with the basic user and password
Raspberry pi time wrong
Can't receive data from Arduino to Raspberry via nrf24l01+
Running Debian (Debian, not Raspbian) on a Raspberry Pi 3
install nodejs for all raspberry pi
Error while running sudo apt-get upgrade command
Sharing the Pi's WiFi connection through the Ethernet port
Using PWM on raspberry pi 3 vs pi 2 with bcm2835 library
Undervoltage warning despite decent power supply
Unable to SSH into Raspberry Pi 3 Model B headlessly
Configure WLAN for RaspberryPI3 using image created with Yocto
Connecting DS18B20 temperature sensor with RJ45 connector?
IWebcam recommendation for Raspberry Pi
Kodi Black Screen, Not responding to turning off Hardware Acceleration
SD Card overheats - Pi3 Model B
Tasks that increase Temperature
How do I trigger multiple pis with one button?
Use 3.3V regulator on 5V rail with GPIO
Power USB device over Raspberry Pi GPIO Pin
Does the "Raspberry Pi Touch Display" work with regular kernel?
Raspberry Pi 3 and 64-bit kernel, differences between armv7 and armv8
Detecting 3.5mm insertion or removal for use in a script
Is there a limited number calling the PWM function from RPi.GPIO and does it interfere with video recording?
Which toolchain for Raspberry Pi 3 and Qt5
Noobs minimum/maximum partition size
Win10 tablet cannot ping RPi anymore
Powering the PI 3 Model B with a battery pack
Opengl supported version?
Is rPi3 binary compatible with rPi2?
Lost console log after running any app that takes over the screen (but not on SSH)
Why my Raspberry Pi (first version) not boot?
Bluetooth buttons and mpg123
Getting extremely low fps on Rpi 3 while image processing
raspbian + libavcodec + which source repository
Unable to mount external harddrive (Openmediavault)
How to output audio signals through GPIO?
Pi 2 rainbow square when external HDD is plugged
Pi with C# instead of Python
How to connect a transparent Oled display to raspberry pi using GPIO?
connect without router cable and without screen
How do I setup my Osoyoo touchscreen?
Stop update of programming language part
How do I install Open cv easily onto my raspberry pi? and so that it works?
Is there a snip equivalent on Raspbian?
How to play mp3 on background from command line
Ping on Raspbian
Ralink RT5370 wifi adapter
I cant get my Raspberry Pi B+ to connect to the internet through a static ip
How dow I install adobe flash player
SSH into Pi3 using WiFi - already set up static IP
Problems updating packages
Whenever I install Iceweasel it installs Firefox instead
Can't get Brother HL-L2300D printer to print from Raspberry Pi
How to define keys for changing pages of ROM/game list in an emulator for RetroPie?
Is it possible to add a bacula file daemon to Raspbian?
How to restart service
RPi 3 Model B: PSU, Measuring Voltage & Amps
Controlling the motor speed
Chromium Wont Open
How to power ten Raspberry Pi 3's?
How do I connect raspberry pi to PC using ethernet for file sharing, while still using wifi for internet access?
Why many RaspberryPi add on has pull up resistors?
Power up from USB Cable or GPIO?
Wifi Dongle TL-WN823Nv2 not is recognised
How to stream audio from raspberry pi to android phone?
SD card related random freezes
SSH not connecting with Raspberry Pi3
Board sign from LED strips
E: Package has no installation candidate
USB Mobile Broadband Modems is NOT compatible with WiFi Dongles? (WIndows 10 IoT Core)
16x2 LCD Display on RPi via I2C/SPI Backpack
How can I use fdisk in a bash script?
How to make my raspberry pi have a constant local ip?
Where exactly are these GPIO pins located on Raspberry PI 2 Model B?
Controlling 2 motors and a servomotor
Is it safe to purge nodejs when replacing "/usr/bin/nodejs" with "/usr/local/bin/node"?
successfully paired bluetooth apple keyboard with Pi but can't type
Is there a way to improve the performance of my Raspberry Pi B+ model
Raspberry pi's linked together for 360 video recording?
Frequent filesystem corruption (compute module, Raspbian)
Python doesn't recognize cv2 when running under sudo
Can I use this screen with the Raspberry Pi Model 3 B
How do I enable or disable GPIO ports at will?
How can I control a HomeEasy Light Switch with a 433MHz Module(GPIO)?
4g dongle internet connection problem?
Display disappears when I connect external HDD
Simulate Pi 3 to configure SD card
Opening Terminal From Kodi (OpenELEC)
Edimax Wifi Adapter does not work with Outsource Powering
Configure the keyboard for console in OSMC
Power an external target
Install Packages on Raspberry Pi2 without wifi
parse error in /etc/sudoers.d
Using a power supply meant for driving LEDs for Raspberry Pi
Maximum Wi-Fi clients on Pi 3 hotspot
Reading values from MCP3008
Raspberry Pi 3 Slow on Ubuntu Mate
How to know when the pi finished shutting down
Problems with adding 4port usb hub to Raspberry Pi Zero
RaspberryPi image size issues
How to connect Rpi-3 and Microstack GPS
Missing build file when building for rtl8812au driver
How do I remove 'Python Games' from Raspbian?
First and Last things it does
What happened to Raspberry Pi 2 and 3 Model A?
Rasberry Pi for a tractor
Fstab: Mount a shared drive using drive name (not ip address)
Eduroam, wpa2-enterprise, wifi connection - Configuration options for the wpa_supplicant.conf file
Accessing Pi remotely
View images without gui
Change raspberry pi 2 password and Root password on multiple Pi's at once
pulseaudio not autostarting on pi 3.
Can I power my rpi with netgear WNDR3700v5 router?
Can you run pfsense on a Raspberry Pi 3?
YouTube video choppy while playing on my Pi 3 browser
Is it okay to just pull the plug?
Does Raspberry Pi cluster make sense for a small rendering farm
handle two way of 1080p, 60fps camera feed to WIFI network in low latency?
Can I use Raspbian SD card on a notebook PC?
I want to make a wireless prototype of a Light switch using Raspberry Pi
raspberry pi live stream through webcam to android phone
How to copy micro SD card from a sealed raspberry pi 2?
Special configuration steps for RasPi 3?
Interfacing with CANBUS, screen and GPIO
How can i discover the current CPU load?
Driving 24VAC sprinkler solenoids through ULN2003A
Pi CAMERA OPENCV my python script test_video.py has black screen
Keeping the ACT LED always on using python
how can you recover your password?
Building a simple DIY rc car, am I missing anything?
creating command prefix for python 3.4
Automatically accept bluetooth pairings
autofocus raspi-cam
i2c Set Address Pointer
How to emulate raspberry pi 2 on Ubuntu 14.04 PC?
Connect raspberry pi to mobile through wifi dongle peer-to-peer
How to display gpsd.utc using paint or similar method
MFRC522 Not working over SPI Interface
Connected to network but no WiFi?
Sync Raspberry Pi with NTP Server on Boot
How to install Ubuntu on a Raspberry Pi 3
Control USB fan via relay
Raspberry Pi for connecting two speakers controlled by smartphone
Check if current if flowing through 220v ac wire
Create a destop shortcut to run sudo apt-get update -y
Raspberry Pi as a POS?
Private/Secure port forwarded Apache server?
Fresh guides to build an OS on Raspberry Pi
Internet connection via wired link to Wndows7 PC laptop with wifi connection
I am looking for a way to use my old samsung galaxy note 3 as the touchscreen for my raspberry pi
sudo raspi-config not working: boot partition not mounted
Raspberry pi 3 /etc/inittab empty
Start GUI while running a terminal aplication
C++ compatibility
Raspberry Pi 3 wifi cancellation
How to grant amule user to access /media/pi/ USB HDD folder?
One pi zero per customer
Disabling serial console/kernel messages on Pi B 2 while still being able to write/read to serial port
Build a customized Linux kernel for the Raspberry Pi
Raspberry Pi 2 not finding External HD
failure to shutdown from ssh when on wifi
raspi-config on Ubuntu 16.04
Is there a way to shut off power to the HDMI output?
Activate USB camera connected in Pi through laptop
Camera / raspistill - output image is black although preview worked
RPI 3 as bluetooth a2dp receiver sound cuts intermittently
Can't connect raspberrypi 2 with pc using ssh
Best OS for Raspberry Pi 3
SSH Key requiring passphrase when there is none
Connect headless pi to arbitrary WiFi network
LIRC won't transmit (irsend: hardware does not support sending)
Can not update or install after changing DHCP IP to Static IP
Why installing eclipse on raspberry pi required open-jdk?
Preconfig WIFI on Raspbian Lite
Speakers not working
Portable HDMI audio splitting?
Is there a software to see on my PC that mirrors exactly what I am doing on the Raspberry Pi touchscreen?
Raspberry Pi 3 component video output doesn't work
Raspberry Pi 3 WiFi, Flight Radar24 -
Overwrite SD card?
How do I setup retropie to work with a 2.8inch pitft
Can I use eth0 and wlan0 at the same time in diffrent purpose?
Raspberry Pi cooling; Blow cold air in or suck the hot air out?
Raspberry PI 3 MODEL B - Wireless Bridge to ethernet
RaspPi 3 does not boot (no ACT LED); trying to re-flash SD card, it shows up as '127 MB unknown'
can't access R-Pi after setting static Ip
Can I do anything with a pre-wired photo resistor and no additional A/D converter?
Multiple segmentation faults
Why is it necessary to "expand the file system"?
Trying to interface with the serial port with a simple program
Why two ground connections on solid state relay?
IOError: [Errno 5] Input/output error
DHT22 Raspberry Pi 2/3 questionable humidity accuracy
Ethernet speed / scp
Several devices on SPI bus
Installing chromium on Raspbian
Raspberry Pi 3 model B CentOS desktop installation
How can I stop the overlay of images between my pi camera and FLIR camera?
Stereo Vision Using Compute Module: Pi camera synchronization
How do you configure the Pi Zero to act as a USB webcam using the plug in camera?
Connecting a Raspberry Pi 3 to an iMac
Setting up ad-hoc wireless
Running shell script in cron
Pi 3 using windows iot, deployment failed
Cannot display gpio documentation over "man gpio" command
Farming and Aquaponics using the Win 10 IoT Core on the Raspberry Pi
Where do I put downloaded .tar.gz files?
Analog to Digital Converter (ADC)
How to allow I2C access for non-root users?
Cannot connect to PiCamera when using it with Flask
I knocked a part off of the Raspberry Pi Zero 1.3. Do I really need it? It boots up without it, is that bad?
Automaticly startup BASH script stop with work after 20min
Code/Cron to detect low power and safe shutdown on GPIO
Is it Possible to manipulate GPIO pins via a Configuration File (.json, .ini et.al)
how to read rfid tag using RC522 module with raspberry pi 3
Is the new 2nd gen Focusrite Scarlett 2i4 compatible with the RPi 3 B
Is the Raspberry Pi 3 compatible?
Which hardware to connect a MIDI keyboard to the RPi?
How do I free up ram?
Homebrew Security Camera Network
Ubuntu-Mate Ethernet cable SSH
How much mA or A does the USB ports on the raspberry pi 3 supply?
Raspberry Pi 3 bluetooth pairing issue with tablet
Am I using the Correct GPIO Pins?
I lose all audio when I install the Waveshare drivers on my Raspberry Pi 3
Multiple Raspberry Pi 3 Server monitoring and job automation tools with GUI
Amazon Echo DIY with Matrix Creator
How to control raspberry pi gpio pins over the internet?
RPi2 not booting when USB stick is plugged in
Can't load gui with Raspbian
Raspberry PI GPIO not working
Raspberry Pi Power Limitations
Installing all python modules
udev rules to auto mount usb storage while already running
Wifi Configuration wlan0 unassociated
C++ API for Raspberry pi camera not working
Building a Camera that tracks a target
SSH and VNC insanely slow on RPi 2
What should I use for wireless communication between an Arduino and a Raspberry Pi
Problem with everloop_demo from MATRIX Creator
Multiple rotary encoder raspberry pi 12C GPIO
How to reinstall 1wire support
Raspberry pi 3 no wlan0 listed - no wireless
How can I lower the USB voltage of my Raspberry Pi?
Steady Red Light With One Green Light Flash After Booting Pi
Autorun Firefox on startup...grrrrrrr!
Use Arduino shields with the Raspberry Pi
Comparison of terminal (non-gui) performance for Raspberry Pi 3 Model B on different Linux OS distros
Cron jobs and python scripts
One speaker system, multiple inputs
Raspberry Pi stable date time
Raspberrypi 3 camera port
Connecting the Pi3 automatically to Wifi
Picamera or Webcam Web Interface
Supply 3.3V via GPIO header (Pi3)
Can I have one raspberry pi access the memory of another pi?
How to run a script when a device is connected to USB?
Raspberry Pi 3B not booting
Raspberry Pi will not boot after configuring it
Raspberry PI Momentry switch - too many presses
Pi 3 Consistent Corruption Of SD Card
Controlling a 5m WS2812 LED Strip. Which power supply?
Using Ubuntu host to create/manage Retropie
USB hub powering the Pi and a HDD
Wiring a Fan via SSR to a Raspberry Pi3 GPIO
Multiple DHT22 sensors in different sets of GPIO ports
Syncing multiple Pis operations via GPIO
Making WebIOPi work on Raspberry Pi 3
How to change default username on Raspberry Pi when connected via ssh?
How can I wire a separate battery pack and control it with the 40-pin GPIO?
Raspberry Pi Web Server - how to forward traffic from router to RPI local address
Set static IP and stop DHCP on Jessie Lite
Best hardware+software to read UHF RFID tags?
Seems to work fine, but the red light is sometimes off
Is there a .exe alternative for Raspbian?
Can PoE ethernet cable damage raspberry pi?
Split HDMI output into two adjacent images
Bad Raspberry boards?
Pi3 WiFi extremely slow
PiFm on raspi-zero
How to install Google Cloud SDK on Raspberry Pi 2 Jessie
How to permanently hide mouse pointer or cursor on Raspberry PI?
Parallel data ADC with GPIO
How can you get video display using the FLIR thermal camera
Picamera Python Library Alternatives
Disable power on Wifi and Bluetooth interfaces during boot?
Making a simple graphical OS
I need the dimensions for the RPI Zero and RPI3
How do you run internet files
Where can I share my cool scripts?
Safely using the ground pin
dhcp obtains IP but no connection to Internet after upgrade to Jessie from Wheezy
Win10 IoT Screen Orientation Wont Change for Raspberry Pi 3 + RPi 7" Display
Strange behaviour in I2C baud rate - RPI2-B / PRI3
Toggle Switch for Flight Simulator
GPIO 02 and 03 seem always high when used as an input (with pull down resistors attached)
Samsung 3.8 v battery + adafruit usb boost
Pi 3 Raspbian "stretch" (testing) disables wifi
Raspberry Pi B+ Overclocking
Serial not work when running python script at pi boot
Hardware Issue - RPi3 renaming eth0 to eth1
Weird output on 7" HDMI/USB touchscreen
Setting up a WiFi-direct connection using pi3+arch linux arm and Android
Adafruit i2c LCD Plate wired to RaspberryPi only shows 2 lines of blocks
Trying to SSH in using urxvt gives error
Raspberry Pi 3 Model B - Windows IoT RDP Client
How to install RTC on RPi3 with Kali Linux as OS?
Raspberry Pi 3B refusing to shut down
Automatically connect trusted Bluetooth speaker
Door sensor data sent to pi wirelessly
Rpi3 Access Point/Hotspot Connects but no Internet
Can you replace a DSL modem with a Raspberry Pi?
Raspberry Pi does not boot properly after installing django
SSH over Bluetooth with iOS
Can raspberry pi generate many 40khz square wave on GPIO pin using package supported from simulink?
Disable Overscan not working
replicating one Raspberry Pi to many
I can't find the Raspberry PI Configuration on my Jessie setup
TightVNC Server - remove password
Using one Raspberry Pi as the Interface to trigger a camera on another Raspberry Pi zero
RPi2 : Kernel panic after updating, unable to mount fs on unknown block (179,2)
PuTTY X11 proxy: unable to connect to forwarded X server
Code debugging, led control by date from file, Python
interpret data from universal gcode sender on raspberry pi
Direct two-way communication between a PC Application and a Pi Application
Suggestions to monitor mains voltage from a heating stat
PWM output using RPi
It's possible to rewrite sd card image over the ssh
How to automatically run a Python GPIO script at boot?
How do I Install Kivy for python 3.4 on my raspberry? Is that possible?
Unable to create a bootable Raspbian Lite SD card with the `dd` command
When to power GPIO projects from external power source?
Microsoft Xbox 360 pad and Kodi mapping issues - Retropie 4.0
Sense HAT GPIO Pins Broke Off
How to label micro-SD cards?
Monitor HDMI compatibility
Pi crashing when powered through 5V pin
Use Android phone as display for RPi3
Getting Information from one Raspberry to another
Driving PWM output frequency
Raspberry Pi 3 USB booting
Creating multiple SD cards with varying config
basic ssh issue
Use nc pins of 5 inch HDMI touchscreen
tkinter on Raspberry Pi; Raspbian/Jessie Python 3.4
Make Geany the default
How do you fix the screen size of raspberry Pi 7" screen
Converting 24V to 5V for GPIO power supply
Why is my Raspberry Pi 3 display not filling the screen?
How to connect to raspberry pi outside of local network without port forwarding
Boosting FM range transmission from Raspberry Pi
Configuring audio to produce balanced mono output
How Much Current for GPIO Power Supply
TL-WN823N not working with Pi Zero
raspberry pi as input, changing input value to high
What is range of bluetooth in raspberry pi 3?
Cron job not running ruby script
Arduino Mega 2560 VS Raaspberry Pi 3
continue running after disconnect
Raspberry Pi not connecting to Wi-Fi (OctoPi)
Tell apart RPi 1 from RPi 2 via SSH only
What is the maximum frequency of a pulse width modulation signal for the raspberry pi 3?
Connect a pressure sensor with Raspberry Pi 2
Analog/Digital IO pins
my asoundrc is modified every reboot
Procmon equivalent for Raspbian
wiringPiSetup: Must be root (Did you forget sudo ?)
Raspberry Pi Cannot Boot, SD card loaded with NOOBS
Raspberry Pi 3 can't update IP address
Autorun c executable on boot
Check system name and kernel version in script
Portable power supply for RPI3 and official touchscreen requirements
Sharing folder with windows computer
Sensor to activate remote lights on Wi-Fi
How to remaster TinyCoreLinux for Raspberry Pi aka piCore Linux?
How to read the status of the Power-LED on Raspberry Pi 3 with Python
Raspberry Pi = Chromecast + Chromecast Audio (2-in-1)?
DIY USB 3 Way Splitter on Raspberry Pi Zero
can i build a cheap linear actuator
Raspberry PI and RFID within same case?
RPi3 Noobs with Raspbian
How to download and install Python 3.5 in Raspbian
Can i develop a wireless/Bt app for smartphone through which i can controll the raspberry pi gpio pins?
Fast interface to computer other than Ethernet
MPD hangs on song change
running a command on pi boot after IP is assigned
Cannot mount shared NAS directory with ownCloud
Force quit Python script / edit rc.local?
How do I pause and stop video of omxplayer by using python script?
wrong date after power supply interuption ( Sun 28thDec 2014)
Passive speaker connected to the Pi
What is the difference between the GPIO pins BCM 14 and BCM 18?
Implement a GPIO function with a callback calling a asyncio method
Raspberry Pi won't boot up after installing Adafruit's Jessie PiTFT image
RetroPie & PS3 Controller over Bluetooth
Are all arduino modules compatible with raspberry pi
second virtualhost causes apache2 failure
Sensor Bus for USB
connect to host port 22: Connection refused
Python Variable Invalid Syntax
When I try to connect to my Pi via ethernet, it gives me this error
Record two mics via pyaudio
How to emulate a Raspbian image on a PC to access the data?
Distance Sensor placement of resistor
transferring files from remote servers to local
Unable to apt-get update but connected to internet?
RPi 3 DHT22 question about the sensor
Unable to repair sd disk partition
Training Pocketsphinx on raspberry pi 3
Livestreaming video and saving it in the lower quality on the sd card at the same time
Installing sublime text on raspberry pi
Raspberry 1, no wifi dongle detected (TP-Link TL-WN823N)
How to make admin account
Where is my wlan password located on raspberry pi?
Autorun Firefox in fullscreen-mode on startup
Install wifi on minimum OS
Connect to secured and hidden SSID without manually editing config files
Raspberry Pi 3 not detected by pc
wifi dongle acknowledged but not transmitting
How to get Chromium working on Pi-3
Raspberry Date and Time
Reliable method to differentiate a Raspberry Pi 2 and 3?
How to SSH Into Pi Using a Script
SystemD unit dependencies to start wiringPi GPIO application
What version of Raspbian will Raspberry PI 3 run?
How do pull-down resistors work?
Raspberry Pi 3 Model B Timers
How to boot with customized image without the text to Console Autologin
DPKG failing with fail2ban
Terminal setup of Bluetooth tethering
Have I been sent a dead Pi?
How to autoplay an audio stream at startup?
How to Configure VNC to Parrot Security OS?
raspbian-output-video-camera-to-3-5-lcd
Where delete the parameter that references the UART serial port (ttyAMA0)?
What libraries do I need to write a desktop application for Raspbian with Visual Studio "C++ for Linux" and remote GDB Debugging?
Resistors on the RPI GPIO
How to connect about 50 Bosch BNO055 sensors to one RasPi 3?
How to make a Minecraft door in python on Minecraft Raspberry Pi edition
Library to allow use of Pi camera in projects?
GPIO: Warning Channel already in use
VNC on Raspberry Pi 3B
How much space do I need on my SD card for Raspbian?
Mirror display on a TV via wireless HDMI
Vehicle 12v detection or measurement
Can't access SD card contents (Ubuntu) after inserting SD into Android phone
Fast Copy from Raspi 3 to USB?
Can I boost up the GPIO 5V output to 12V
Play multiple different .mp4 videos without gaps
Hyperterminal for RPi: data transfer from device to RPi
How to connect raspberry pi to an open WiFi network (like in shopping mall)?
The static IP address does is not the sam as configure in /etc/network/interfaces file
How to set up a router and connect it to another wifi
Raspberry Pi uses wrong network interface
saving pictures file name as camera ID
Accessing a remote Desktop on a Raspberry Pi
Headless Raspbian Jessie 8.0 keeps crashing days apart
Can see neighbor's wifi but not mine
Raspberry pi 3 boot partition gets corrupted over and over
In Windows IoT i get taskInstance.TriggerDetails is null
Temporary blocking all network access for a limited time while a CPU sensitive task is running
Which directories of a Raspbian installation can be deleted safely
Serial Communication between Raspi and Arduino Mega
How to connect SIM800 GSM ADD-ON to RaspberryPi 3
2 wireless dongles in an access point issues
GPIO pin voltage is too low to energize relay
Read keyboad input from background process
Easiest way to delay shutdown by a few ms after power loss
Have I destroyed USB power? Ethernet & USB devices powering on & off constantly unless keyboard connected
protobuf 2.5.0 and raspberry pi 3
Unable to delete files from my Pi
Restore deleted files on Raspbian Jessie
do I need radiator for Raspberry PI 3 model B
How to run pulseaudio -D from boot
Pi 3 Model B does not boot. Shows only 2 multicolored squares
How much connection speed can I except using Pi 3 in this setup?
Switching Audio Sources by time
Is halted a viable state for a battery powered pi zero long-term?
Snappy Ubuntu Core Lose Ethernet Connection After Updating
Permission Denied - Raspbian
How can I install the KUMAN 3.5 inch-display?
Connect DHT11 and Raspberry Pi without a breadboard
My Raspberry Pi doesn't detect i2c BMP085 slave
Unable to boot Ubuntu Snappy on Pi 3
Setting up raspberry pi camera to view on a Web page
Interfaces besides sysfs for GPIO programing in C
Inconsistency in continuous data acquisition on RPi
How to install Eclipse Luna or later on Raspberry Pi 3
Simple data transmission from multiple Arduinos (client) to Raspberry pi (server) wirelessly
Controlling Raspberry Pi over WiFi in LAN
confused about how control multiple home's accessories with least GPIO
Temperature sensor
Can I have an Apache Server on Pi 3 if it's working as a WiFi AP
Kernel panic, corrupt filesystem, Raspberry Pi not booting
Why in Raspberry Pi 3 ACT blink 2 times then stop & PWR always RED?
dpkg error when trying to install mysql-server
DS18b20 sensor disappearing and turning into "00-00.."
Raspberry Pi 3 + DS3231 RTC
Why can't I get audio to play with pygame only once?
Is there a way to have Multi-Condition Interrupt
Is it safe to plug Raspberry Pi 3 to 6V?
RPi.GPIO library working in python 3.4 but not in python 2.7
WiringPi: change output of GPIO pins synchronously?
MCP23017 (ControlEverything) - Output Pin Status always 0
Attaching second raspberry pi to a USB hub already connected to a Pi
No targets. Stop. error when installing emqttd
Raspbian with kernel 2.6.18 ~ 3.10.10
How to set up WiFi on Raspbian 4.4.13
12V DC buck converter to power Raspberry Pi
Nextcloud Box Performance
What does raspi-config's Expand Filesystem option do?
RealVNC Viewer connection refused when headless
Getting accelerometer reading from LIS2DH sensor
SSH the Pi from computer with a USB cable only
3.5 Kuman touchscreen rotation
Power multiple Pis through 5V GPIO and 5V wall wart
Zoneminder installation. What version?
Making a battery pack UPS with GPIO signal
I2c device not detected by Raspberry Pi
Monitor doesn't detect my Raspberry pi 3
Files edited with nano are corrupted after reboot or shutdown
New Raspberry Pi won't boot Raspbian on brand new MicroSD card
"Activating" a button upon other buttons being pressed
Regulate the voltage
Serial communication between arduino and rpi using tx/rx pins
I got a white screen with vertical lines on it when I booted my Raspberry Pi
Max frequency can created by wave function in pigpio library
RPi Zero vga display problem
How to connect to a RPi with new-ly flashed SD?
How to revert firmware?
Raspberry pi HAT device-tree
Root file browser for raspbian jessie
Raspberry Pi Has Severe Issues and Won't Boot
Drive DC motors using L293d motor driver board
Raspberry Pi 2 Crashes, ACT light blinking
Multiple cameras on Raspberry Pi
Cooling fan powered directly from GPIO?
Raspberry Pi 3 has less than 1GB memory available at OS level
Is it possible to connect a second wifi card to a raspberry pi 3, VNC to it using one and then use the second to connect to another wifi?
Possible to route audio directly from usb-audio line-in to same usb audio line-out?
Edit and executable linux script from Python 3
Windows 10 bridge creates duplicate IP
Motion sensor (abnormal behaviour)
Why is my random command not playing a random file?
VNC Server not autostarting on RPi3
LIRC won't transmit irsend: unknown remote
Launch kodi from startup and play track
error - problem connecting to Raspberry Pi 3 with xrdp
How to increase resolution on latest Raspbian Pixel while connected to VNC client?
Chown permission denied on samba share
Raspberry Pi 3 Can't Login anymore
DNS with Raspberry as Wi-FI AP for local users
Use bluetooth controller to execute shell script
Raspberry Pi Zero Battery Life With 4400mAh battery
7 color flash sensor does not blink
Wifi doesnt connect to internet with static ip
Having trouble with device or resource busy error in aircrack-ng; raspberry pi 3, raspbian
PWM with a MOSFET won't power on LEDs
how to set up a cron job twice a day to save what was installed using sudo apt-get install to a text file
PN532 NFC module not working on Pi 3
how to enable spi1? / pi 3 and two rc522 RFID readers
Connection between Raspberry Zero and Raspberry Pi 2 or 3
notro rpi firmware not working on rpi B+
No communication between GPRS module RaspberryPi Zero serial GPIO ports
Strange behavior with GPIO serial connection
Inconsistency between GPIO block diagram and interrupt table in the BCM2835 datasheet
Can you mount/unmout hard drives that are powered and connected to the raspberry pi via a usb hub?
PHP can't execute sudo script (www-data is allowed to sudo commands)
Ethernet not working, sometimes defaults to random IP - raspberry pi 2 model b
Tutorial to use Raspberry Pi to control wall socket switch
script not executing after boot
How to debug video via ssh
Accessing raspberry pi remotely without static IP?
Raspbian Jessie lite Ethernet defaults to random ip fresh install
Is this idle temperature normal for the RPi 3?
Ok to use 2 port USB Power adapter?
Raspberry Pi Alexa Echo Startup from Desktop
communicate with arduino over serial
How do I create a live video stream with a Raspberry Pi and a Java tomcat server?
Is my RPi using a lot of electricity?
How can I ouput my rdp session to the local monitor?
sudo apt-get update error, connection failed
My RPi 2 Model B will not detect the keyboard or my mouse?
What technology allows the Raspberry Pi Zero to be used as a USB device?
Why use Raspberry Pi as a supercomputer?
Encrypt specific directory on raspberry pi
2016-09-23-raspbian-jessie.img Pi 2 Model B headless set-up - SSH connection refused
After installing and customised how to make an distribution image (size of only data)
How can I hide files on desktop
How to stop raspberry pi from disabling WIFI SSH access when ETH0 is plugged in
Unable to get i2c working
Is it possible to use Raspberry PI for contactless payments?
Cannot ssh into RaspberryPi from Windows
How to use Rpi3 to receive I2C data from Arduino-based sensors
GPIO Python strange difference
I2C problem sending from Pi to Arduino
Will this Arduino module work with Raspberry Pi 3?
RPi3 - Raspbian Pixel WiFi Connect not working
Pi Zero overlay to swap power and data usb ports?
Official Raspberry Pi 7 inch display power consumption
installing Android Studio
Does the Raspberry Pi 3 regulate the voltage on its 5V pins?
Bought simple board with three RGB LEDs. How to control it via Pi?
How to boot into own python script (GUI) only?
Raspbian, Kodi uses keyboard as a remote, not to type
raspberry pi 3 multiple cameras with recording function
OSMC: how to execute a script with systemd at shutdown
Need help setting up SSH Tunnel with Motion Pi surveillance system
When trying to use Python 3.4 to import RPi.GPIO I get "ImportError: No module"
Raspberry Pi and DoorBell Video Camera
QR code scanner with Raspberry Pi3
What are the basics needed to learn Raspberry Pi?
Raspberry Pi 3 Use WiFi for web, and Ethernet for local access?
PIR motion sensor
Protecting the breakout pins
how to control WIFI using Raspberry Pi (running Raspbian ) using only C programming
How to make a Raspberry Pi Hub yourself?
Raspi3 audio sounds like rubbish
Arduberry integration between the Arduino part and the Rpi3 file system?
Installing Atom text editor on Rasberry Pi
SSH connection refused via ethernet cable
Can GPIO pins be used by more than 1 equipment?
Can't get "sudo apt-get update" to work! [NOOB]
WiringPi error etates I'm not Using an RPi
Circuit to detect a 3.3v signal
How to disable I2C pins in Raspberry Pi 3 (jessie)
Cannot install programs
How to configure Raspberry Pi in my car
What is the best distro or way to have a Raspberry into a Kiosk Mode?
Admin access on Pi 3
How to update a program on Raspberry Pi?
Can I use a transistor as a relay with the Pi?
what is password with new installation
trying to get SSH over USB to work (Raspberry pi Zero)
Connecting 15V to GPIO w/o dividing voltage
Two soundcards on RPi3?
How to connect Raspberry Pi to 3 stepper motors
What is proper driver board for 7" 40-pin TFT lcd for raspberry pi?
How to use Adafruit TCA9548A 1-to-8 I2C Multiplexer Breakout in C#?
How to have access to a USB port from inside the case?
Can no longer send emails with Python
Can I have two languages on Raspberry Pi
Controlling 1800W heating element
Making a Raspberry Pi 3 accessible w/o configuration via WiFi and static IP/URL
Using the ALSA dmix plugin on Raspbian Jessie
LCD RGB Grove with RPI
Will there ever be an updated Compute Module?
Disable sudo for user Pi (or require root password)
Omxplayer change volume when playing
Waveshare 4inch LCD drivers, error after installation: PANIC: VFS: Unable to mount root fs on unknown-block(179,2)
UART interrupt in Raspberry PI with c or c++
Raspberry Pi image files - is .img created by dd the same as .img used by Win32DiskImager?
Can I send a Text file using the Audio Jack of the Raspberry Pi 3
What does the lightning bolt mean?
Formatting 64/128gb microSC card to run on RP3
Python parallel processes for raspberry pi zero...possible?
Is there a way to run the Macpup 550 Distro on a Raspberry Pi (E.g. Raspberry Pi Zero)?
UV4L can not be started : <alert> [core] No device detected
How can I send commands to a Raspberry Pi via internet?
rpi 3 : combine wifi and ethernet networks
Network configuration timed out in Ubuntu core-16
How to create duplicate images, but change a couple of files
Chromium Browser keeps crashing after update
Disk image writer - duplicating a Pi image to identical SD cards, one says it's too small
What would it take to run android on rpi3
Which remote desktop renders fast
Powering Raspberry Pi 3 alternatives
How do I share files with a Mac?
RPi.GPIO not found in virtual environment
How to move to a newer Raspberry Pi model without a full reinstall
need 1 Wire read / write functions
Raspbian download on Windows
Automatically disable wlan0 on startup
DHT11 or GPIO Library to Use in C
Powering Raspberry Pi 24/7
Sync a small folder between my Mac and Pi 3
How to use 'Connect to Server' on a Mac to access /var/www/html/ on the Pi
Is it legal to use Raspberry Pi to develop a product and sell it?
How to set WiFi network priority?
Connect with SSH
Can two Pis have the same IP address?
su -s ignoring specified shell
Difference between using wpa_supplicant and /etc/network/interfaces
how do I change screen resolution in Pixel?
Auto-login for Raspberry Pi
Pi3 has 7 pullup resistors, I need 8
How to use RC522 RFID on spidev1.x on Raspberry Pi 3
Strange grep /etc/shadow command appearing in my logwatch
Is the pi-zero capable enough to play video?
SSH not working with fresh install
LIRC remote control won't send (irsend: hardware does not support sending)
What is this cable called?
Impossible to view Raspi on laptop in PuTTy nor TightVNC
How do I turn my pi3 back on?
Add script to boot image
GUI with integrated Gnuplot
Bash video script stops working after a week
How to set up Raspberry Pi without a microSD adapter?
Which kernel source is required to compile for Raspberry Pi?
Is it possible to power an orange pi/raspberry pi directly from a computer's power source?
External storage without supplementary power
How to read keyboard/barcode reader data and send it to another pc?
Raspberry pi control on/off switch with Relay
Cannot ssh pi 3 from Ubuntu via ethernet, but can from Windows 7 partition
Controlling a geographically mobile Pi 3 (using iPhone 6S)
Remove SSH warning about default password
Smoke sensor MQ-135
Retrieving AlarmPI (Arch) IP automatically by uploading file to an ssh server
Running an HDMI projector through SSH
How do I connect my raspberry pi to a landline phone to process calls?
Internet connection impossible through PC via Ethernet
Getting feedback from a hall sensor with Raspberry Pi
Python MCP23017 16 ch. I2C input loosing a bit
Raspberry Pi C++ IDE
Cannot execute binary file?
Compare and contrast Python GPIO APIs
Can Raspberry Pi draw power FROM an external HD?
Can't ssh into pi anymore
how to identify if ultrasonic pin is removed from circuit using python code
Pi camera v2 - fast, full sensor capture mode with downsampling
Any way to shutdown Raspberry gracefully in exceptional case?
Can I identify my PI by domain name in a LAN?
Run script in terminal after boot
Wireless USB Touchpad not working as mouse. Why?
What should I look for in a webcam with microphone?
Root filesystem usage at 100%, but I can't see why
Why is cron not showing a scheduled task when the cron file has the line shown below
Cannot Run a Python Script at Boot
Desktop looks different when running RPi on laptop over SSH?
Connect to Pi using SSH without having internet
What can I build with Raspberry Pi 2011.12 with minimum equipment?
OSMC does not list ALSA output when equalizer plugin configured
RetroPie along with NOOBs
Hearing loss -- need RPi Zeros to listen to bells, buzzers, or chimes and send some notification
Is a 2.4 A 5V USB charging port enough to drive a Pi 3?
Re-configure Raspberry Pi Boot Menu
Raspberry Pi 2 BCM2836 working but new Raspberry Pi 2 BCM2837 stuck on Rainbow Screen
No option to enable a camera in "sudo raspi-config"
Transfer a file from Raspberry to Mac
Is it possible to host a website on the Pi3 with 1GB ram?
Make a pin HIGH every time RPi startsup
Kiosk auto refresh
How do you force wiringPI library to use local time instead of UTC time?
Servos on Arduino run fine connected to Mac, poorly connected to Raspberry Pi 3
Compile kernel with overlayfs

'''

##sents = sent_tokenize(text)

for word in text.split():
    sentz = word_tokenize(word)  #return tokenized copy of text
    print(nltk.pos_tag(sentz))























##
##def entities(text):
##    return ne_chunk(
##        pos_tag(
##            word_tokenize(text)))
##
##
##
##tree = entities("When asked about comment, Obama blah blaj blak")
##tree.pprint()
##tree.draw()

##print("\nTEXT: " , text)
##
##print("\n\nSENT_TOKENIZE:" , sents)
##
##print("\n\nWORD_TOKENIZE:" , sentz)
##
##print("\n\n")
##
##print(nltk.wordpunct_tokenize(text))
##
##print("\n\n")

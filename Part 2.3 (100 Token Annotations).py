import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

text = '''

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


'''

tokened = word_tokenize(text)
print(tokened)
##print(nltk.pos_tag(sentz))



##for word in text.split():
##    sentz = word_tokenize(word)  #return tokenized copy of text
##    print(nltk.pos_tag(sentz))

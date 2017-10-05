# Code for Hawaii + ACLU
# Access to public lands in Hawai`i App
Welcome!  [Code for Hawaii](http://www.codeforhawaii.org) has partnered with the [American Civil Liberties Union of Hawai`i](https://acluhi.org) ("ACLU") to create an app.  The intent of the proposed app is to use your geo-location to assist understanding of whose land you are on and your civil rights there.

Please start by reading the [project proposal](docs/ACLU-Access-App.pdf).

*Questions? Want to help?*  
**Come join us** on Wednesday nights at the [Code for Hawaii meetups](https://www.meetup.com/Code-for-Hawaii/).  We meet the first three Wednesdays of the month.  (Contact Ryan for Saturday morning hack sessions too). 

**Quick Links**
* [General project board](https://github.com/CodeforHawaii/ACLU/projects/1)
* [Frontend project board](https://github.com/CodeforHawaii/ACLU/projects/3)
* [Data sources spreadsheet](https://docs.google.com/spreadsheets/d/1eDXV0qamY_5pcfe0SZbqs2PQXR_yJUs0-liX7sJo3wE/)


## Development / Getting Started
To provide a consistent development setup, we've made scripts to provision a Linux virtual machine that runs Docker containers. _"yo :dog:..."_

If you don't know what that means, read the sections below. :arrow_down:

If you do, just make sure you have `VirtualBox` (v5.0+) and `vagrant` (v 1.9+), then run `vagrant up`. :clap:

### VirtualBox
[VirtualBox](https://www.virtualbox.org) is a product from [Oracle](https://www.oracle.com) that runs an entire Operating System (the _"guest OS"_) inside the VirtualBox program on your computer (the _"host OS"_).

:question: _Why on :earth_americas: would you want that?_  
 **A:** This allows us to encapsulate the entire development environment in the _guest OS_ without having to modify your _host OS_. Thus, we can install all the development tools we need without worrying about potentially breaking any configuration on your computer. It also gives us a common OS (Linux) that we know things will work on. :smiley:

Please [download VirtualBox here](https://www.virtualbox.org/wiki/Downloads) for your _host OS_ and install it.

### Vagrant
[Vagrant](https://www.vagrantup.com) is a [HashiCorp](https://www.hashicorp.com) product that provides a convenient scripting interface to control VirtualBox and manage Virtual Machines.

:question: _Again, why do you need this?_  
 **A:** Vagrant allows us to automatically configure the _guest OS/VM_ exactly how we want it in a consistent fashion. This means you won't have to spend time downloading, installing, and configuring the correct versions of development tools (e.g. node, yarn, python, httpie, docker, etc..) to setup your build environment.

Please [download Vagrant here](https://www.vagrantup.com/downloads.html) for your OS and install it.

### Creating the VM
After VirtualBox and Vagrant are installed, run the following command from the root directory of the `aclu` repo:
```
vagrant up
````
...and maybe grab some :coffee: and :doughnut: -- depending on your internet connection, this may take awhile!

### Running a shell in the VM
```
vagrant ssh
```

### Getting the app up and running

After running `vagrant up`, you'll want to perform the following:

```
vagrant ssh
/var/project-aclu/etc/start.sh
/var/project-aclu/backend/etc/seed_fake_park_data.sh
```

After these commands are run, you should be able to go to
http://localhost:50808 and see something.

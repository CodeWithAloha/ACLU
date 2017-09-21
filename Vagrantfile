# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-gatling-rsync")
  raise 'This project needs a vagrant plugin, to install it run: # vagrant plugin install vagrant-gatling-rsync'
end

Vagrant.configure(2) do |config|
  config.vm.box = "bas/contrib-stretch64"
  config.vm.box_version = "9.0.0"
  config.vm.network "private_network", ip: "192.168.50.50"
  config.vm.synced_folder "./", "/var/project-aclu/", type: "rsync", rsync__verbose: true, rsync__args: ["--verbose", "--archive", "-z", "--links"], rsync__exclude: [".git/", "./frontend/node_modules"]
  config.vm.define "aclu" do |aclu|
  end
  config.vm.network "forwarded_port", guest: 8080, host_ip: "127.0.0.1", host: 50808 # nodejs-frontend
  config.vm.network "forwarded_port", guest: 50050, host_ip: "127.0.0.1", host: 50050 # eve-backend
  config.vm.provision "shell", path: "provision-debian.sh", privileged: false
end
